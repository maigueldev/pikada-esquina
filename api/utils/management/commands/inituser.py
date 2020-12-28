from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.filter(username='antonio').first()
        if not user:
            User.objects.create_superuser(
                username='antonio',
                email='antonio@pikada.cl',
                password='antonio2020',
            )
            self.stdout.write(self.style.SUCCESS('Usuario inicial creado'))
