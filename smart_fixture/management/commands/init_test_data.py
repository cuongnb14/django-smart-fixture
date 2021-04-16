from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from ddf import N
from django_dynamic_fixture.ddf import DataFixture
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Init test data'

    def handle(self, *args, **options):
        self.init_model(User, 50)

    def init_model(self, model_class, number):
        for i in range(number):
            instance = N(model_class, fill_nullable_fields=True)
            instance.save()
