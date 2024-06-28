from faker import Faker
from app import create_app, db
from app.models import Product
import random

app = create_app()
app.app_context().push()

faker = Faker()

def add_products(num_products=50):
    for _ in range(num_products):
        name = faker.catch_phrase()
        description = faker.text(max_nb_chars=200)
        price = round(random.uniform(10.0, 100.0), 2)
        rating = random.randint(1, 5)

        product = Product(name=name, description=description, price=price, rating=rating)
        db.session.add(product)

    db.session.commit()

if __name__ == '__main__':
    add_products(50)  # Genera y agrega 50 productos

