import re
from product_modell import Product
from product_dao import ProductDataAccess
from datetime import datetime


class ProductController:
    # region VALIDATION
    @staticmethod
    def is_valid_product(product, brand, number_of_product, expire_date, price):
        # product validation
        if not re.match(r"^[a-zA-Z0-9\s]{2,40}$", product):
            raise NameError("Invalid Product Name")

        # brand validation
        if not re.match(r"^[a-zA-Z0-9\s]{2,40}$", brand):
            raise NameError("Invalid Brand Name")

        # number of product validation
        try:
            number = int(number_of_product)
            if number <= 0:
                return False, "Number of product must be greater than 0"
        except:
            raise NameError("Invalid Number of Product")

        # price validation
        try:
            price_value = float(price)
            if price_value <= 0:
                raise NameError("Price must be greater than 0")
        except:
            raise NameError("Invalid Price")

        # expire date validation
        try:
            date_obj = datetime.strptime(expire_date, "%Y-%m-%d")
        except ValueError:
            raise NameError("Invalid EXPIRE DATE (YYYY-MM-DD)")

        today = datetime.now().date()
        if date_obj.date() < today:
            raise NameError("EXIPRE DATE cannot be in the past")

        return True, ""
    # endregion

    # region SAVE
    @staticmethod
    def save(id, product, brand, number_of_product, expire_date, price):
        valid, message = ProductController.is_valid_product(
                product, brand, number_of_product, expire_date, price
            )
        if not valid:
            return False, message

        # calculate of the total price for save
        total_price = int(number_of_product) * float(price)

        try:
            product_obj = Product(id, product, brand, number_of_product, expire_date, price, total_price)
            dao = ProductDataAccess()
            dao.save(product_obj)
            return True, "Product saved successfully"
        except Exception as e:
            return False, f"Failed to save product: {e}"
    # endregion

    # region EDIT
    @staticmethod
    def edit(id, product, brand, number_of_product, expire_date, price):

        valid, message = ProductController.is_valid_product(
            product, brand, number_of_product, expire_date, price
        )
        if not valid:
            return False, message

        # calculate the total price for edit the product
        total_price = int(number_of_product) * float(price)

        try:
            product_obj = Product(id, product, brand, number_of_product, expire_date, price, total_price)
            dao = ProductDataAccess()
            dao.edit(product_obj)
            return True, "Product edited successfully"
        except Exception as e:
            return False, f"Failed to edit product: {e}"
    # endregion

    # region REMOVE
    @staticmethod
    def remove(id):
        try:
            dao = ProductDataAccess()
            dao.remove(id)
            return True, "Product removed successfully"
        except Exception as e:
            return False, f"Failed to remove product: {e}"
    # endregion

    # region FIND
    @staticmethod
    def find_all():
        try:
            dao = ProductDataAccess()
            products = dao.find_all()
            return True, products
        except Exception as e:
            return False, f"Failed to find products: {e}"
    # endregion




