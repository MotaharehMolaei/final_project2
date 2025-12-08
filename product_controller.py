import re
from datetime import datetime


class ProductController:
    # region VALIDATION
    @staticmethod
    def is_valid_product(product, brand, number_of_product, expire_date, price):

        if not re.match(r"^[a-zA-Z0-9\s]{2,40}$", product):
            raise NameError("Invalid Product Name")

        if not re.match(r"^[a-zA-Z0-9\s]{2,40}$", brand):
            raise NameError("Invalid Brand Name")

        try:
            number = int(number_of_product)
            if number <= 0:
                return False, "Number of product must be greater than 0"
        except:
            raise NameError("Invalid Number of Product")

        try:
            price_value = float(price)
            if price_value <= 0:
                raise NameError("Price must be greater than 0")
        except:
            raise NameError("Invalid Price")

        try:
            date_obj = datetime.strptime(expire_date, "%Y-%m-%d")
        except ValueError:
            raise NameError("Invalid Enroll Date (YYYY-MM-DD)")

        today = datetime.now().date()
        if date_obj.date() < today:
            raise NameError("Enroll Date cannot be in the past")

        return True, ""
    # endregion

