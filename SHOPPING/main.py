from customerdetails import CustomerDetails
from ShoppingItems import Shop
from payment import PaymentMethod
import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s -> %(message)s")


customer_name1: str = input("Enter your name:" )
logger1 = logging.getLogger(name=customer_name1)
logger1.info(f"Hello Mr/Mrs.{customer_name1}")
customer_details: CustomerDetails = CustomerDetails(logger1)

products1: Shop = Shop()
product_name1: dict[str,int | float] = {
    'name' : 'Mac book',
    'price' : 93000,
    'quantity' : 1
}
product_name2: dict[str,int | float] = {
    'name' : 'Samsung Ultra 24',
    'price' : 123000,
    'quantity' : 1
}
product_name3: dict[str,int | float] = {
    'name' : 'IPHONE 15',    
    'price' : 159997,
    'quantity' : 2
}

products1.BuyProducts(product_name1)
products1.BuyProducts(product_name2)
products1.BuyProducts(product_name3)

products1.make_transaction(transaction_method="amazon pay")
logger1.info("Thank You for purchasing in our Shop!!🤩🙏")


# customer_name2: str = input("Enter your name:" )
# logger2 = logging.getLogger(name=customer_name2)
# logger2.info(f"Hello Mr/Mrs.{customer_name2}")
# customer_details: CustomerDetails = CustomerDetails(logger2)

# products2: Shop = Shop()

# product_name1 = {
#     'name': 'hp laptop',
#     'price': 89000,
#     'quantity': 1
# }
# product_name2 = {
#     'name': 'iMAC',
#     'price': 489000,
#     'quantity': 1
# }
# products2.BuyProducts(product_name1)
# products2.BuyProducts(product_name2)

# products2.make_transaction("phone pay")
# logger2.info("Thank You for purchasing in our Shop!!🤩🙏")