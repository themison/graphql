from django.apps import AppConfig


class PizzaConfig(AppConfig):
    name = 'pizza'
    def ready(self):
        import pizza.signals