from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)


# products_list = [
#     Products(1, "Laptop", "15-inch gaming laptop with RTX GPU", 1299.99, 5),
#     Products(2, "Smartphone", "6.5-inch OLED display, 128GB storage", 799.50, 12),
#     Products(3, "Headphones", "Noise-cancelling over-ear headphones", 199.99, 20),
#     Products(4, "Keyboard", "Mechanical keyboard with RGB lighting", 89.99, 15),
#     Products(5, "Monitor", "27-inch 4K UHD display", 349.00, 8)
# ]

products_list = [
    Product(
        id=1,
        name="Laptop",
        desc="15-inch gaming laptop with RTX GPU",
        price=1299.99,
        qty=5,
    ),
    Product(
        id=2,
        name="Smartphone",
        desc="6.5-inch OLED display, 128GB storage",
        price=799.50,
        qty=12,
    ),
    Product(
        id=3,
        name="Headphones",
        desc="Noise-cancelling over-ear headphones",
        price=199.99,
        qty=20,
    ),
    Product(
        id=4,
        name="Keyboard",
        desc="Mechanical keyboard with RGB lighting",
        price=89.99,
        qty=15,
    ),
    Product(id=5, name="Monitor", desc="27-inch 4K UHD display", price=349.00, qty=8),
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = session()

    count = db.query(database_models.Product).count

    if count == 0:
        for product in products_list:
            db.add(database_models.Product(**product.model_dump()))
            db.commit()


init_db()


# routes

# test route
@app.get("/")
def greet():
    return "hello world"


# fetch products
@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products


# fetch a single product
@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    print("product :", db_product)
    if db_product:
        return db_product
    return "product not found"


# create a new product
@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


# update a product
@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db_product.name = product.name
        db_product.desc = product.desc
        db_product.price = product.price
        db_product.qty = product.qty
        db.commit()
        return "product updated"
    else:
        return "product not found"


# delete a product
@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
    else:
        return "product not found"
