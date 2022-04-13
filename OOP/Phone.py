from Item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, brokenPhone=0):
        # Call the super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to the received argument
        assert brokenPhone >= 0,f"Broken Phones {brokenPhone} is not greater than  or equal to 0"
        
        # Assign to self object
        self.brokenPhone = brokenPhone