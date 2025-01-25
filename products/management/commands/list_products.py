from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Отображает все товары с информацией о наличии на складе и категории'

    def handle(self, *args, **kwargs):
        products = Product.objects.select_related('category').all()
        for product in products:
            self.stdout.write(
                f"Товар: {product.name} | Остаток на складе: {product.stock} | Категория: {product.category.name} | Цена: {product.price}"
            )
