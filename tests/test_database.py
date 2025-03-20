from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as sauce
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as filling

checked_buns = {"black bun": 100, "white bun": 200, "red bun": 300}
checked_ingredients_prices = {"hot sauce": 100, "sour cream": 200, "chili sauce": 300,
                              "cutlet": 100, "dinosaur": 200, "sausage": 300}
checked_ingredients_types = {"hot sauce": sauce, "sour cream": sauce, "chili sauce": sauce,
                             "cutlet": filling,  "dinosaur": filling, "sausage": filling}


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        for bun in buns:
            assert bun.name in checked_buns.keys(), "Каждая булочка должна быть представлена в базе"
            assert bun.price == checked_buns[bun.name], "Каждая булочка должна иметь соответствующую цену"
        assert len(buns) == 3, "В базе должно быть ровно три булочки"

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        for ingredient in ingredients:
            assert ingredient.name in checked_ingredients_prices.keys(), "Каждый ингредиент должен быть представлен в базе"
            assert ingredient.price == checked_ingredients_prices[ingredient.name], "Каждый ингредиент должен иметь соответствующую цену"