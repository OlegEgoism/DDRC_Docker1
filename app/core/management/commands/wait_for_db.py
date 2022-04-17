import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         if Account.objects.count() == 0:
#             for user in settings.ADMINS:
#                 username = user[0].replace(' ', '')
#                 email = user[1]
#                 password = 'admin'
#                 print('Creating account for %s (%s)' % (username, email))
#                 admin = Account.objects.create_superuser(email=email, username=username, password=password)
#                 admin.is_active = True
#                 admin.is_admin = True
#                 admin.save()
#         else:
#             print('Admin accounts can only be initialized if no Accounts exist')