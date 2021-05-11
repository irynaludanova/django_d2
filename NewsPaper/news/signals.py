from django.db.models.signals import m2m_changed
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_managers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from news.models import PostCategory, Mail


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(m2m_changed, sender=PostCategory)
def do_mailing(sender, action, instance, **kwargs):
    if action == 'post_add':
        category_lst = list(sender.objects.filter(post=instance.id).
                            values('category'))
        for category in category_lst:
            mail_list = list(Mail.objects.filter(
                category=category['category']).values('subscribers__username',
                                                      'subscribers__email'))
            for mail in mail_list:

                html_content = render_to_string(
                    'mail.html',
                    {
                        'post': instance,
                        'text': instance.preview(),
                        'username': mail["subscribers__username"],
                    }
                )

                msg = EmailMultiAlternatives(
                    subject=f'{instance.header}',
                    body=f'Здравствуйте, {mail["subscribers__username"]}. '
                    'Для Вас уже доступны свежие новости!',
                    from_email='iludanova@yandex.ru',
                    to=[mail['subscribers__email']],
                )
                msg.attach_alternative(html_content, "text/html")

                msg.send()