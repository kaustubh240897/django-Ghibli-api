from django.core.management.base import BaseCommand
from movies.models import Movie, Actor
from datetime import date

class Command(BaseCommand):
    help = 'Add dummy data to movies app'

    def handle(self, *args, **options):
        # Create actors with auto-generated IDs
        actor1 = Actor.objects.create(name='Actor 1', species='Human', url='https://example.com/actor1')
        actor2 = Actor.objects.create(name='Actor 2', species='Alien', url='https://example.com/actor2')

        # Create movies with actors
        movie1 = Movie.objects.create(title='Movie 1', description='Description 1', release_date=date(2023, 1, 1))
        movie1.actors.add(actor1, actor2)

        movie2 = Movie.objects.create(title='Movie 2', description='Description 2', release_date=date(2023, 2, 1))
        movie2.actors.add(actor2)

        self.stdout.write(self.style.SUCCESS('Dummy data added successfully.'))
