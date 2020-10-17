'''
UML (Unified Modeling Language) diagrams are a standard visual notation to express
object-oriented software designs.
'''


'''
Proposed class diagram for Credit:-

class: CreditCard

Fields:
_customer _bank  _account  _balance  _limit

Behaviours:
get_customer()  get_bank()  get_account() get_balance() get_limit()
make_payment(amount)  charge(price)
        
'''

class CreditCard:
    ''' Consumer credit card'''
    
    def __init__(self,customer,bank,account,limit): #constructor
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0
        
    def get_customer(self): #Accessors with read-only access to traits
        '''Return name of customer'''
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        '''Current balance'''
        return self._balance
    
    def charge(self,price):
        ''' Charge given price to card, assuming sufficient card limit
        return True if charge processed'''
        if price + self._balance > self._limit:     #if recharge above storage limit
            return False                                            #cannot recharge

        else:
            self._balance = self._balance + price
            return True

    def make_payment(self,amount):
            ''' Process customer payment and reduce balance'''
            self._balance = self._balance - amount
    
   
 
'''
a single leading underscore in the
name of a data member, such as balance, implies that it is intended as nonpublic.

The interpretter automatically binds the instance upon which the method is invoked to
the self parameter.

self._balance it represents an instance variable of the card
balance represents the local parameter
'''
    

''' Let's Test CreditClass'''
if __name__ == '__main__':
    wallet = []
    obj1 = CreditCard('Sathvik', 'SBI Savings', '9653 5687 4123', 5000)
    obj2 = CreditCard('Sathvik', 'ICICI', '4216 7842 5632', 2500)

    wallet.append(obj1)
    wallet.append(obj2)

    i = 500
    wallet[0].charge(i)
    wallet[1].charge(3*i)

    for c in range(2):
        print(f'''
Customer = {wallet[c].get_customer()}
Bank = {wallet[c].get_bank()}
Account = {wallet[c].get_account()}
Limit = {wallet[c].get_limit()}
Balance = {wallet[c].get_balance()}
''')
        while wallet[c].get_balance()>1000:
            wallet[c].make_payment(100)
            print("Making payment...")
            print("New Balance = ",wallet[c].get_balance())
        print("Min Balance INR.1000 reached")
        
