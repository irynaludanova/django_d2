from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

# Users
user1 = User.objects.create_user(username='author1', first_name='Иван', last_name='Иванов', password='1111')
user2 = User.objects.create(username='author2', first_name='Петр', last_name='Петров', password='2222')

# Author
author1 = Author.objects.create(author_id=user1)
author2 = Author.objects.create(author_id=user2)

# Category
category1 = Category.objects.create(category='Музыка')
category2 = Category.objects.create(category='Кино')
category3 = Category.objects.create(category='Искусство')
category4 = Category.objects.create(category='Путешествия')

# Post
post_a1 = Post.objects.create(
    author=author1,
    type='A',
    header='Beat Film Festival 2021 пройдет в Москве со 2 по 20 июня',
    text='В премьерном зале киноцентра «Октябрь» Beat Film Festival представит секцию гала-премьер. В нее войдут как картины, отмеченные наградами, так и громкие фестивальные хиты, которые олицетворяют современное документальное кино.Так, зрители увидят фильм «Аалто» («Alvar Aalto») — новый взгляд на жизнь и наследие знаменитого архитектора Алвара Аалто. Картина рассказывает не только о его знаковых зданиях, но и о взаимоотношениях архитектора с семьей.',
)
post_a2 = Post.objects.create(
    author=author1,
    type='A',
    header='Американский рэпер DMX умер в возрасте 50 лет после нескольких дней комы',
    text='DMX был госпитализирован 2 апреля после сердечного приступа, вызванного предположительно передозировкой наркотиков. Музыкант несколько дней был подключен к аппарату жизнеобеспечения.',
)
post_n1 = Post.objects.create(
    author=author2,
    type='N',
    header='"Годзилла против Конга"',
    text='"Годзилла против Конга" установил рекорд по сборам в Северной Америке, заработав 48,5 млн долларов за первые 5 дней',
)

# PostCategory
pa1_c3 = PostCategory.objects.create(post=post_a1, category=category3)
pa1_c4 = PostCategory.objects.create(post=post_a1, category=category2)
pa2_c1 = PostCategory.objects.create(post=post_a2, category=category1)
pa2_c4 = PostCategory.objects.create(post=post_a2, category=category3)
pn1_c2 = PostCategory.objects.create(post=post_n1, category=category2)
pn1_c3 = PostCategory.objects.create(post=post_n1, category=category3)

# Comment
com1 = Comment.objects.create(post=post_a1, user=user1, text='Интересно. Надо посмотреть')
com2 = Comment.objects.create(post=post_a1, user=user2, text='Уже видел. Так себе...')
com3 = Comment.objects.create(post=post_a2, user=user2, text='Сочувствую((')
com4 = Comment.objects.create(post=post_n1, user=user1, text='Когда у нас выйдет в прокат?')
com5 = Comment.objects.create(post=post_n1, user=user2, text='Эпичный фильм!')

# Like/dislike
post_a1.like()
post_a1.dislike()
post_a2.like()
post_a2.like()
post_n1.dislike()
post_n1.like()
com1.dislike()
com3.like()
com3.dislike()
com5.like()
com5.dislike()

# Rating
author1.update_rating()
author2.update_rating()

# best_author
best_author=Author.objects.all().order_by('-rating')[0]
print("Лучший автор:", best_author.author_id.last_name)

# best_article
best_article = Post.objects.order_by('-rating')[0]
print("Дата:", best_article.pub_date)
print("Автор:", best_author.author_id.last_name)
print("Рейтинг:", best_article.rating)
print("Заголовок:", best_article.header)
print("Превью:", best_article.preview())

# comments
comments=Comment.objects.filter(post = best_article)
for c in comments:
    print("Дата комментария:", c.pub_date)
    print("Автор:", c.user)
    print("Рейтинг:", c.rating)
    print("Текст:", c.text)
