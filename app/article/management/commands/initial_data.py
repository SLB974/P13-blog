from article.models import Category
from django.core.management.base import BaseCommand, CommandError

category_elements = [
    ('Python','python.png'),
    ('Django','django.png'),
    ('Flask','flask.png'),
    ('Docker','docker.png'),
    ('FastAPI','fastapi.png'),
    ('Général','general.png'),
    ('WSL','wsl.webp'),
    ('Ubuntu','ubuntu.png'),
    ('VS Code','vscode.png'),
    ('Web3','web3.png')
]

class Command(BaseCommand):
    help = "This command creates initial data for the database"
    
    def handle(self, *args, **kwargs):
        try:
            self.stdout.write('Injecting data for categories...')
            self.add_category_data()
            
        except:
            raise CommandError('Something went wrong!')
        
        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))
        
    def add_category_data(self):
        for elements in category_elements:
            category = Category(category=elements[0], pic=elements[1])
            category.save()
            
            