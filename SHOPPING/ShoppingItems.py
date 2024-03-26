'''this module will have all the items which can purchase in this shop'''

from payment import PaymentThrough,PaymentMethod

class Shop:
    def __init__(self) -> None:
        '''Creating a empty or to count he total things bought by consumer'''
        self.total_price: float = 0.0
        self.total_items = []
        self.total_quantity = []
    
    def BuyProducts(self,products: dict[str,int | float]) -> None:
        self.products = products
        
        '''applying discount'''
        self.applying_discount = self.apply_discount(self.products['price'])
        self.products['price'] = self.applying_discount
        self.total_price += self.products['price']   # adding to the total price
        
        '''displaying the product details'''
        for product,product_details in products.items():
            print(f"{product} <=> {product_details}")
        
        self.total_items.append(self.products['name'])    
        self.total_quantity.append(self.products['quantity'])    
        
        self.display(self.total_items,self.total_price,self.total_quantity)

    
    '''method which apply discount to the given price'''
    def apply_discount(self,price: float) -> float:               
        if price > 100_000:
            price *= 0.756
            return price
        
        elif price > 70_000:
            price *= 0.865
            return price
        
        return price
    
    def display(self,item_name: str,price:float,quantity: int) -> None:
        self.item_name = item_name
        self.item_price = price
        self.item_quantity = quantity
        print("[ItemName,Quantity]")
        self.item_quantity = list(zip(self.item_name,self.item_quantity))
        print(f"{self.item_quantity}")
        print(F"Total Price is: {"-"*5}> ₹{self.item_price}")
        
    def make_transaction(self,transaction_method: PaymentThrough):
        self.transaction_method = transaction_method
        self.payment = PaymentMethod(self.transaction_method,self.item_price)