from prettytable import PrettyTable
def prod (products):

    table = PrettyTable ()

    table.field_names = ["Product Name", "Price $", "Quantity"]

    for p in products:
        table.add_row ([p ["name"], f"{p["price"]:.2f}", p ["quantity"]])
    print (table)