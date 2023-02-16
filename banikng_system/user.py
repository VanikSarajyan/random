class User:
    def __init__(self, name: str, amount: float) -> None:
        self.name = name
        self.amount = amount
    
    def get_name(self) -> str:
        return self.name
    
    def get_amount(self) -> float:
        return self.amount
    
    def set_amount(self, amount) -> None:
        self.amount = amount
