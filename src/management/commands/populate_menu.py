from django.core.management.base import BaseCommand
from src.models import MenuItem

class Command(BaseCommand):
    help = "Populate the database with sample lemonade menu items"

    def handle(self, *args, **kwargs):
        items = [
            {"name": "Classic Lemonade", "description": "Refreshing and tangy", "price": 3.50},
            {"name": "Strawberry Lemonade", "description": "Sweet with a berry twist", "price": 4.50},
            {"name": "Mint Lemonade", "description": "Cooling and fresh", "price": 4.00},
            {"name": "Peach Lemonade", "description": "Juicy and sweet peach flavor", "price": 4.75},
            {"name": "Blueberry Lemonade", "description": "Bursting with blueberry goodness", "price": 5.00},
        ]

        for item in items:
            MenuItem.objects.get_or_create(name=item["name"], defaults={
                "description": item["description"],
                "price": item["price"],
            })

        self.stdout.write(self.style.SUCCESS("Menu populated successfully!"))
