from tkinter import *


# GUI
window = Tk()
window.geometry("1200x500")
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
Entry(window, textvariable=id).place(x=130, y=20)
Entry(window, textvariable=product).place(x=130, y=60)
Entry(window, textvariable=brand).place(x=130, y=100)
Entry(window, textvariable=number_of_product).place(x=130, y=140)
Entry(window, textvariable=expire_date).place(x=130, y=180)
Entry(window, textvariable=price).place(x=130, y=220)
Entry(window, textvariable=total_price, state="readonly").place(x=130, y=260)
# endregion


window.mainloop()