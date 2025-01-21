from app import app
from models.usermodel import user_class

obj_product = user_class

@app.route("/product/add")
def add_product():
    return obj_product.getuser_detail()