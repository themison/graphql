from django.contrib.auth.models import Group, Permission 
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType 
from django.contrib.auth.models import User
  

def add_permissions_to_groups():
    manager, created = Group.objects.get_or_create(name ='manager') 
  
    ct = ContentType.objects.get_for_model(User) 
    
    permission = Permission.objects.create(
                                        codename ='can_add_manager', 
                                        name ='Can add manager', 
                                        content_type = ct) 
    manager.permissions.add(permission) 



class Command(BaseCommand):
    def handle(self, **options):
        add_permissions_to_groups()