import csv
import re
from signal import raise_signal

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received argument
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0,f"Quantity {quantity} is not greater than  or equal to 0"
        
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price
    
    def apply_discout(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, incrementValue):
        self.__price = self.__price + self.__price * incrementValue
    
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def is_interger(num):
        # We'll count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"
    
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.name} {self.quantity} times.
        Regards, LuuMinhThang.
        """
    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()