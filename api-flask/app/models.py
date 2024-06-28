from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer)  # Calificación del 1 al 5

    def __repr__(self):
        return f'<Product {self.name}>'

