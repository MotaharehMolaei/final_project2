import sqlite3

# Create supermarket DB
with sqlite3.connect("supermarket_db") as connection:
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists products (
            id integer primary key,
            product text,
            brand text,
            number_of_product integer,
            expire_date text,
            price real,
            total_price real
        )
    """)

    connection.commit()

print("Supermarket database and table created successfully.")


class ProductDataAccess:
    def save(self, product):
        with sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "insert into products (id, product, brand, number_of_product, expire_date, price, total_price) "
                "values (?, ?, ?, ?, ?, ?, ?)",
                [
                    product.id,
                    product.product,
                    product.brand,
                    product.number_of_product,
                    product.expire_date,
                    product.price,
                    product.total_price
                ]
            )
            connection.commit()

    def edit(self, product):
        with sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "update products set product=?, brand=?, number_of_product=?, expire_date=?, price=?, total_price=? "
                "where id=?",
                [
                    product.product,
                    product.brand,
                    product.number_of_product,
                    product.expire_date,
                    product.price,
                    product.total_price,
                    product.id
                ]
            )
            connection.commit()

    def remove(self, id):
        with sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from products where id=?", [id])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from products order by product, brand")
            return cursor.fetchall()
