from django.core.management.base import BaseCommand
from explore.models import Category
import random

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete categories instances")
    Category.objects.all().delete()


def create_category():
    """Creates an address object combining different elements from the list"""
    print("Creating category")
    names = ["#221 B", "#101 A", "#550I", "#420G", "#A13"]
    icon_urls = ["https://i.ibb.co/XVqmRrF/ic-highlights1.png",
                 "https://i.ibb.co/XVqmRrF/ic-highlights2.png",
                 "https://i.ibb.co/XVqmRrF/ic-highlights3.png",
                 "https://i.ibb.co/XVqmRrF/ic-highlights4.png", ]
    category = Category(name=random.choice(names),
                        icon_url=random.choice(icon_urls))
    category.save()
    print("{} category created.".format(category))
    return category


def run_seed(self, mode):
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 addresses
    for i in range(5):
        create_category()

