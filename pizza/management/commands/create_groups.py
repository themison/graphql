from django.core.management.base import BaseCommand
from django.contrib.auth.models import  Group


def create_groups():
    group, created = Group.objects.get_or_create(name="client")
    if created:
        group.name = "client"
        group.save()

    group, created = Group.objects.get_or_create(name="manager")
    if created:
        group.name = "manager"
        group.save()
       
class Command(BaseCommand):
    def handle(self, **options):
        create_groups()
