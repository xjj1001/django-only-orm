from django.apps import apps
from django.conf import settings
from django.core.management import call_command

apps.populate(settings.INSTALLED_APPS)


def migrate(app_name: str):
    call_command("migrate", app_name)


def make_migrations(app_name: str):
    call_command("makemigrations", app_name)