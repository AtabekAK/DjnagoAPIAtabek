from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Category, Product, Order
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Generates fake data for testing'

    def handle(self, *args, **kwargs):
        faker = Faker()

        # Генерация пользователей
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=faker.unique.user_name(),
                email=faker.unique.email(),
                password='password123'
            )
            users.append(user)

        # Генерация категорий
        categories = []
        for _ in range(5):
            category = Category.objects.create(
                name=faker.unique.word().capitalize(),
                description=faker.text(max_nb_chars=200)
            )
            categories.append(category)

        # Генерация продуктов
        products = []
        for _ in range(30):
            product = Product.objects.create(
                name=faker.unique.word().capitalize(),
                description=faker.text(max_nb_chars=200),
                price=round(random.uniform(10, 500), 2),
                stock=random.randint(0, 100),
                category=random.choice(categories)
            )
            products.append(product)

        # Генерация заказов
        for _ in range(50):
            product = random.choice(products)
            quantity = random.randint(1, 5)
            Order.objects.create(
                user=random.choice(users),
                product=product,
                quantity=quantity,
                total_price=product.price * quantity
            )

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))
