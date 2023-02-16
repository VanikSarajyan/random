from restaurant import Restaurant
from user import User
from food import Food


class MenuAm:
    def __init__(self, restaurants: list):
        self.restaurants = restaurants

    def order(self, user: User, address: str, restaurant: Restaurant, food: Food):
        if restaurant in self.restaurants:
            if food in restaurant.get_menu():
                if user.get_amount() > food.get_price():
                    if food.get_quatity() > 0:
                        print(f"Food is in delivering to {address}")
                        food.set_quantity(food.get_quantity()-1)
                        user.set_amount(user.get_amount - food.get_price())
                    else:
                        raise ValueError("Not enugh food")
                else:
                    raise ValueError("Not enugh amount")
            else:
                raise ValueError("No such food in restaurant")
        else:
            raise ValueError("No such restaurant")
