from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Pizza

from .helper import secret


@receiver(pre_save, sender=Pizza)
def saveBitch(sender, **kwargs):
    print (123213321)