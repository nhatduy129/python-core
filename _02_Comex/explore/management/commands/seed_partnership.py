# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from explore.models import Partnership
from explore.models import Category
from django.utils import timezone
import random
import string

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
    Partnership.objects.all().delete()


def create_db():
    """Creates an address object combining different elements from the list"""
    print("Creating partnership")
    categories = ["8vW5A967AnYQg2oE",
                  "8vW5A9EBFwRj4sQk",
                  "8vW5A9Fe8A3k0LP6",
                  "8vW5A9KiC-CZoJ88",
                  "8vW5A9PZQguY6DeT",]
    name = ["Calligraphy Lesson",
            "Cocktails with Christina",
            "Dumpling Making",
            "Face Painting with Chelcie",
            "DBS",
            "HSBC",
            "AIA",
            "Circles Life"]
    addresses = ["91 Ubi Ave 4, Singapore",
                 "145 Syed Alwi Rd, Singapore",
                 "21 Fernvale Link, Singapore",
                 "2 Ang Mo Kio Street 21, Singapore",]
    photo_urls = ["https://kidspartysingapore.com/wp-content/uploads/2016/04/Outdoor-Parks-west.coast_.park_.2.jpg",
                 "https://i.redd.it/5u2dr46saeh31.jpg",
                 "https://www.gannett-cdn.com/presto/2019/09/19/USAT/c1421ef3-cbdc-44f8-abda-7029d51f14d0-african_penguin.jpg",
                 "https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/Random-Oversampling-and-Undersampling-for-Imbalanced-Classification.jpg",
                 "https://pbs.twimg.com/media/EXprEogWAAELVsT.jpg",
                 "https://www.straitstimes.com/sites/default/files/styles/article_pictrure_780x520_/public/articles/2018/11/01/gn-dbs-0111.jpg",]
    short_descriptions = ["Hmlet and Full Circle Craft Distillers are taking over Fat Prince!",
                          "Remz Ocampo & head bartender at Fat Prince and resident funnyman, Shallum.",
                          "Special appearance by guest bartender for the night is flair extraordinaire.",
                          "We're coming together to bring you a night of good bites and specialty cocktails made with ARC Botanical Gin. ",
                          "Of course a takeover isn't takeover without some amazing bartenders.",]
    descriptions = ["Hmlet and Full Circle Craft Distillers are taking over Fat Prince! We're coming together to bring you a night of good bites and specialty cocktails made with ARC Botanical Gin. \n\nOf course a takeover isn't takeover without some amazing bartenders. Special appearance by guest bartender for the night is flair extraordinaire, Remz Ocampo & head bartender at Fat Prince and resident funnyman, Shallum.",
                    "Channel your inner Beckham at 5-a-side football. Recruit your fellow members and get ready for the most epic playoffs ever! Form up your teams and post on the Hmlet Members group on FB. We'll have 3 teams play on the 3rd and 17th June.",
                    "The Hmlet crew is joining Seven Clean Seas to give Changi Beach some TLC. Come with us and make our beaches a more beautiful place for everyone to enjoy! Click here to get more deets on how to register.\n\n\n9am: Meet @ Constant Wind (11 Changi Coast Walk)\n9.30am: Safety briefing then head to the beach \n11.30am: Finish up and refreshments",]
    links = ["https://hmlet.com",
             "https://www.facebook.com/hmletSG/",
             "www.facebook.com/hmletSG/posts/1641890992626715",]
    link_titles = ["RSVP", "Visit Us", "More Details"]
    category = Category.objects.get(id=random.choice(categories))
    photo_url = random.choice(photo_urls)
    partnership = Partnership(category=category,
                              name=random.choice(name) + " " + randomString(2),
                              date=timezone.now().date(),
                              address=random.choice(addresses),
                              photo_thumb_url=photo_url,
                              photo_url=photo_url,
                              short_description=random.choice(short_descriptions),
                              description=random.choice(descriptions),
                              link=random.choice(links),
                              link_title=random.choice(link_titles))

    partnership.save()
    print("{} partnership created.".format(partnership))
    return partnership


def run_seed(self, mode):
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 addresses
    for i in range(305):
        create_db()


def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))