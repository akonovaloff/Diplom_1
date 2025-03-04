from praktikum.ingredient import Ingredient

test_ingredient = {"type": "sauce",
                   "name": "hot sauce",
                   "price": 50}


class TestIngredient:

    def test_get_name(self):
        tested_name = test_ingredient["name"]
        ingredient = Ingredient(ingredient_type=test_ingredient["type"],
                                name=tested_name,
                                price=test_ingredient["price"])
        assert ingredient.get_name() == tested_name, "Ингредиент должен иметь заданное имя"

    def test_get_type(self):
        tested_type = test_ingredient["type"]
        ingredient = Ingredient(ingredient_type=tested_type,
                                name=test_ingredient["name"],
                                price=test_ingredient["price"])
        assert ingredient.get_type() == tested_type, "Ингредиент должен иметь заданный тип"

    def test_get_price(self):
        tested_price = test_ingredient["price"]
        ingredient = Ingredient(ingredient_type=test_ingredient["type"],
                                name=test_ingredient["name"],
                                price=tested_price)
        assert ingredient.get_price() == tested_price, "Ингредиент должен иметь заданную цену"