from django.apps import AppConfig


class PeopleappConfig(AppConfig):
    name = "apps.peopleapp"

    def ready(self):
        import apps.peopleapp.signals
