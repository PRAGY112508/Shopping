'''This module decides which type of payment is applied by the user and proceeds the 
payment process'''

from enum import Enum
from customerdetails import CustomerDetails
from string import digits
from random import choices
from time import sleep

class PaymentThrough(Enum):
    DebitCard = 'DebitCard'
    CreditCard = 'CreditCard'
    AmazonPay = 'AmazonPay'
    GooglePay = 'GooglePay'
    PhonePay = 'PhonePay'
    
class PaymentMethod:
    def __init__(self,payment_method:PaymentThrough,total_price:float) -> None:
        self.payment_method = payment_method.lower()
        self.total_price = total_price
        
        self.payment_processing()
        
    def payment_processing(self):
        if self.payment_method == 'debit card':
            self.DebitCard()
        if self.payment_method == 'credit card':
            self.CreditCard()
        if self.payment_method == 'amazon pay':
            self.AmazonPay()
        if self.payment_method == 'google pay':
            self.GooglePay()
        if self.payment_method == 'phone pay':
            self.PhonePay()
        
    def DebitCard(self):
        self.card_payment()
        
    def CreditCard(self):
        self.card_payment()

    def AmazonPay(self):
        self.upi_payment()

    def GooglePay(self):
        self.upi_payment()
        
    def PhonePay(self):
        self.upi_payment()
        
    def card_payment(self):
        bank_name: str = input("Enter the Bank Name On the Card: ")
        card_holder: str = input("Enter the Name on the Card Holder On the Card: ")
        validity_date: str = input("Enter the validity date of the Card: ")
        self.withdraw_amount: float = float(input("Enter the amount to be paid : ₹"))
        cvv: int = int(input("Enter The CVV of the Card: "))
        
        self.checking_otp = self.generate_otp()
        sleep(3)
        print(f"One Time Password(OTP) : {self.checking_otp}")
        self.user_entered_otp = input("Enter the OTP provided to you by bank : ")
        self.otp_confirmation(self.checking_otp,self.user_entered_otp)
        
        transaction: Transaction = Transaction(self.total_price,self.withdraw_amount)
    
    def upi_payment(self):
        bank_name: str = input("Enter the Bank Name On the Card: ")
        upi_number: int = int(input("Enter the valid UPI number of NetBanking: "))
        if len(str(upi_number)) >= 12:
            self.withdraw_amount: float = float(input("Enter the amount to be paid : ₹"))
            
            self.checking_otp = self.generate_otp()
            sleep(3)
            print(f"One Time Password(OTP) : {self.checking_otp}")
            self.user_entered_otp = input("Enter the OTP provided to you by bank : ")
            self.otp_confirmation(self.checking_otp,self.user_entered_otp)
            
            transaction: Transaction = Transaction(self.total_price,self.withdraw_amount)
        else:
            raise ValueError("Invalid UPI Number")
        
    def generate_otp(self) -> str:
        self.otp = "".join(choices(digits,k=6))
        return self.otp
    
    def otp_confirmation(self,otp: str,entered_otp:str):
        if otp == entered_otp:
            return
        else:
            raise ValueError("OTP Not Match.Failed..")
        
class Transaction(CustomerDetails):
    def __init__(self,total_amount:float,paid_amount: float) -> None:
        self.total = total_amount
        self.pay_amount = paid_amount
        self.ValidTransaction()
        
    def ValidTransaction(self):
        self.customer_id: str = input("Enter your customer id to proceed the payment : ")
        self.from_payment(self.customer_id)
        if self.pay_amount < self.total:
            raise ValueError("Not Enough Money Transaction Failed")
        elif self.pay_amount == self.total:
            print("Successfully Transaction Completed.")
        elif self.pay_amount > self.total:
            self.balance = self.pay_amount - self.total
            print("Successfully Completed the transaction.")
            print(f"The Balance amount ₹{self.balance}")