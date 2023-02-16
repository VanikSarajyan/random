from user import User
class Bank:
    def __init__(self, amount:int) -> None:
        self.__amount = amount

    def deposit(self, amount:int, user:User):
        if user.get_amount() > amount:
            raise ValueError()
        else:
            self.__amount += amount
            user.set_amount(user.get_amount - amount)
        
        
    def withdraw(self,amount:int,user:User):
        if user.get_amount() > amount:
            self.__amount += amount
            user.set_amount(user.get_amount + amount)
        else:
            raise ValueError()
