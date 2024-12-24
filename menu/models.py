from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
    ]

    DESIGN_CHOICES = [
        ('design1', 'Design 1'),
        ('design2', 'Design 2'),
    ]

    name = models.CharField(max_length=100)
    category_choice = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='drink',  # Default category is 'drink'
    )
    design_choice = models.CharField(
        max_length=10,
        choices=DESIGN_CHOICES,
        default='design1',
    )

    def __str__(self):
        return self.name


# Model for food items
class Food(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.title
