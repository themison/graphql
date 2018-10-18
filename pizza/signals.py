from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Pizza

from .helper import secret


@receiver(pre_save, sender=Pizza)
def pizzaPre(sender, instance, **kwargs):
    instance.secret_key = secret()

@receiver(post_save, sender=Pizza)
def pizzaPost(sender, instance, created, **kwargs):
    print(instance.secret_key)

