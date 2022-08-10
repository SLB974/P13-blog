from article.models import Article
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "This command erase all article data for the database"
    
    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Clearing data for articles...')
            self.add_category_data()
            
        except:
            raise CommandError('Something went wrong!')
        
        self.stdout.write(self.style.SUCCESS('Successfully cleared article data'))
        
    def add_category_data(self):
        
        Article.objects.all().delete()
            
            