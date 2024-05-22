from django.core.management.base import BaseCommand, CommandError
from ._create_fake_fill_database import main as create_fake_db


class Command(BaseCommand):
    help = 'Generate fake data for DjangoGramm'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS('Starting fill db...'))
            create_fake_db(3)
            self.stdout.write(self.style.SUCCESS('Database filled successfully!'))
        except CommandError as e:
            self.stdout.write(self.style.SUCCESS(f'Something went wrong with db fills! {e}'))
        except TypeError as e:
            self.stdout.write(self.style.SUCCESS(f'Something went wrong with db fills! {e}'))
