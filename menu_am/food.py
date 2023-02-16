class Food:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def set_price(self, price: float) -> None:
        if price >= 0:
            self.price = float(price)
        else:
            raise ValueError("Price can't be negative.")

    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, quantity: int) -> None:
        if quantity >= 0:
            self.quantity = int(quantity)
        else:
            raise ValueError("Quantity can't be negative.")
    
