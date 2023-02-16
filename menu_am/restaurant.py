from food import Food

class Restaurant:
    
    def __init__(self, name: str, menu: list[Food] = []) -> None:
        self.name = name
        self.menu = menu
    
    def get_name(self) -> str:
        return self.name
    
    def get_menu(self) -> list:
        return self.menu
    
    def add_food(self, food: Food) -> None:
        pass

