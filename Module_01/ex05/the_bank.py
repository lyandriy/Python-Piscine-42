class Account(object):
    
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount
        
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        if not isinstance(new_account, Account) or new_account in self.accounts:
            return("False")
        for x in self.accounts:
            if x.name == new_account.name:
                return ("False")
        self.accounts.append(new_account)
        
    def transfer(self, origin, dest, amount):
        atr_origin = 
        if len(origin.__dict__) % 2 == 0 or len(dest.__dict__) % 2 == 0:
            
            

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name:
        str(name) of the account
        @return True if success, False if an error occured
        """
        # ... Your code ... 