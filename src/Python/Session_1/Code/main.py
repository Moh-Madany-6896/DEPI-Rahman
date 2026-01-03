from loginUI import login_sys

from products import prod

products = [{"name":"Water","price":80.0,"quantity":1500},
            {"name":"Soda","price":130.0,"quantity":1500},
            {"name":"Chips","price":75.0,"quantity":1500},
            {"name":"Eggs","price":200.0,"quantity":1500}  
]

if __name__ == "__main__":
    login_sys ()
    prod (products)
