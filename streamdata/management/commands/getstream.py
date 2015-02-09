from django.core.management.base import BaseCommand

from ...twitterstream import get_tweets

class Command(BaseCommand):
    def handle(self, *args, **options):
        get_tweets()
