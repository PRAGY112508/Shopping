'''This Projects is based on Shopping Gives better ideas in OOP Concepts and other 
                                                        important concepts with oops'''
from random import choices
from string import digits,ascii_letters

#creating a class CustomerDetails and its dependencies
'''This class will perform and create new id for customer for further processing'''

class CustomerDetails:
    customer_code = None
    def __init__(self,name: str) -> None:
        self.customer_info = { }
        self.name = name
        self.unique_id: str = self.customer_id()
        self.customer_info[self.name] = self.unique_id
        self.checking_customer_id(self.unique_id)  
        self.display_details(self.customer_info)
        
    def customer_id(self):
        id: str ="".join(choices(ascii_letters + digits,k=8))
        return id
    
    def display_details(self, customer_info: dict[str,str]) -> None:
        print(f"Customer Name : Customer ID\n{customer_info}")

    def checking_customer_id(self,custom_id):
        CustomerDetails.customer_code = custom_id
    
    def from_payment(self,payment_id):
        if payment_id == self.customer_code:
            return
        else:
            raise ValueError("Invalid Customer ID")
        
if __name__ == '__main__':
    customer1: CustomerDetails = CustomerDetails('allwin')  

