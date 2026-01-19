import os
import django
from PIL import Image, ImageDraw

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memory_core.settings')
django.setup()

from django.contrib.auth.models import User
from game.models import Card
from django.core.files.base import ContentFile
from io import BytesIO

def create_color_image(color, text):
    img = Image.new('RGB', (400, 400), color=color)
    d = ImageDraw.Draw(img)
    # Simple cross or circle maybe? Just text for now
    # d.text((70, 90), text, fill=(255, 255, 255)) 
    # Since we might not have fonts, just drawing a shape
    w, h = 400, 400
    if text == 'Red':
        d.ellipse([100, 100, 300, 300], fill='white')
    elif text == 'Blue':
        d.rectangle([100, 100, 300, 300], fill='white')
    elif text == 'Green':
        d.polygon([(200, 50), (100, 350), (300, 350)], fill='white')
    else:
        d.rect = d.rectangle([150, 150, 250, 250], fill='white')
        
    output = BytesIO()
    img.save(output, format='PNG')
    return output.getvalue()

def init():
    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', '1')
        print("Superuser 'admin' created with password '1'")
    else:
        print("Superuser 'admin' already exists")

    # Create Cards
    # Using simple solid colors/shapes as images
    card_data = [
        ('Red Circle', '#ef4444'),
        ('Blue Square', '#3b82f6'),
        ('Green Triangle', '#10b981'),
        ('Orange Box', '#f59e0b'),
        ('Purple Box', '#8b5cf6'),
        ('Pink Box', '#ec4899')
    ]
    
    if Card.objects.count() == 0:
        for name, color in card_data:
            card = Card(title=name)
            img_content = create_color_image(color, name.split()[0])
            card.image.save(f'{name.lower().replace(" ", "_")}.png', ContentFile(img_content), save=True)
            print(f"Created card: {name}")
    else:
        print("Cards already exist")

if __name__ == '__main__':
    init()
