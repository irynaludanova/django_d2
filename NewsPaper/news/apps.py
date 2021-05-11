from django.apps import AppConfig



class NewsConfig(AppConfig):
    name = 'news'
    verbose_name="Новости"

    def ready(self) -> None:
        import news.signals

        return super().ready()
