from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from product_controller import ProductController


def reset():
    product.set("")
    brand.set("")
    number_of_product.set("")
    expire_date.set("")
    price.set("")
    total_price.set("")

    status, product_list = ProductController.find_all()

    for row in table.get_children():
        table.delete(row)

    # Insert products, calculate the total price and find the highest ID to make it automatically
    final_total_value = 0
    max_id = 0

    if status:
        for p in product_list:
            table.insert("", END, values=p)
            final_total_value += float(p[6])
            max_id = max(max_id, int(p[0]))
    else:
        messagebox.showerror("Error", product_list)

    id.set(max_id + 1)
    final_total_label.config(text=f"Total Price: {final_total_value} $")


# region select product
def select_product(event):
    p = table.item(table.focus())["values"]
    if p:
        id.set(p[0])
        product.set(p[1])
        brand.set(p[2])
        number_of_product.set(p[3])
        expire_date.set(p[4])
        price.set(p[5])
        total_price.set(p[6])
# endregion


# region save click
def save_click():
    status, message = ProductController.save(
        id.get(),
        product.get(),
        brand.get(),
        number_of_product.get(),
        expire_date.get(),
        price.get(),
    )

    if status:
        reset()
        messagebox.showinfo("Save", "Product saved successfully")
    else:
        messagebox.showerror("Error", message)
# endregion


# region edit click
def edit_click():
    status, message = ProductController.edit(
        id.get(),
        product.get(),
        brand.get(),
        number_of_product.get(),
        expire_date.get(),
        price.get(),
    )

    if status:
        reset()
        messagebox.showinfo("Edit", "Product edited successfully")
    else:
        messagebox.showerror("Error", message)
# endregion


# region remove click
def remove_click():
    status, message = ProductController.remove(id.get())

    if status:
        reset()
        messagebox.showinfo("Remove", "Product removed successfully")
    else:
        messagebox.showerror("Error", message)
# endregion


# ------------------------------------GUI--------------------------------------
window = Tk()
window.geometry("1100x500")
window.title("Supermarket Product Management")

# region labels
Label(window, text="ID").place(x=20, y=20)
Label(window, text="Product").place(x=20, y=60)
Label(window, text="Brand").place(x=20, y=100)
Label(window, text="Number").place(x=20, y=140)
Label(window, text="Expiration Date\n YYYY-MM-DD").place(x=15, y=180)
Label(window, text="Price").place(x=20, y=220)
Label(window, text="Total Price").place(x=20, y=260)
# endregion

# region Variables
id = IntVar()
product = StringVar()
brand = StringVar()
number_of_product = StringVar()
expire_date = StringVar()
price = StringVar()
total_price = StringVar()
# endregion

# region Entry
# make the state of ID and TOTAL PRICe in readonly
Entry(window, textvariable=id, state="readonly").place(x=130, y=20)
Entry(window, textvariable=product).place(x=130, y=60)
Entry(window, textvariable=brand).place(x=130, y=100)
Entry(window, textvariable=number_of_product).place(x=130, y=140)
Entry(window, textvariable=expire_date).place(x=130, y=180)
Entry(window, textvariable=price).place(x=130, y=220)
Entry(window, textvariable=total_price, state="readonly").place(x=130, y=260)
# endregion

# region Buttons
Button(window, text="Save", width=18, command=save_click).place(x=50, y=330)
Button(window, text="Edit", width=18, command=edit_click).place(x=50, y=360)
Button(window, text="Remove", width=18, command=remove_click).place(x=50, y=390)
# endregion

# region table
table = ttk.Treeview(
    window,
    height=21,
    columns=["ID", "Product", "Brand", "Number", "Expire Date", "Price", "Total Price"],
    show="headings"
)

table.column("ID", width=50, anchor=CENTER)
table.column("Product", width=120,anchor=CENTER)
table.column("Brand", width=120, anchor=CENTER)
table.column("Number", width=100, anchor=CENTER)
table.column("Expire Date", width=120, anchor=CENTER)
table.column("Price", width=100, anchor=CENTER)
table.column("Total Price", width=120, anchor=CENTER)

table.heading("ID", text="ID")
table.heading("Product", text="Product")
table.heading("Brand", text="Brand")
table.heading("Number", text="Number")
table.heading("Expire Date", text="Expire Date")
table.heading("Price", text="Price")
table.heading("Total Price", text="Total Price")

table.place(x=350, y=20)
table.bind("<<TreeviewSelect>>", select_product)
# endregion

# region total label
final_total_label = Label(window, text="Total price: 0 $", font=("Arial", 14, "bold"), fg="blue")
final_total_label.place(x=20, y=40)
final_total_label.place(x=350, y=450)
# endregion

reset()
window.mainloop()