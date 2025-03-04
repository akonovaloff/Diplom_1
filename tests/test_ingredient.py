import pytest
from praktikum.ingredient import Ingredient
from test_data.test_data import tested_ingredients


class TestIngredient:
    @pytest.mark.parametrize("test_ingredient", tested_ingredients)
    def test_get_name(self, test_ingredient):
        tested_name = test_ingredient["name"]
        ingredient = Ingredient(ingredient_type=test_ingredient["type"],
                                name=tested_name,
                                price=test_ingredient["price"])
        assert ingredient.get_name() == tested_name, "Ингредиент должен иметь заданное имя"

    @pytest.mark.parametrize("test_ingredient", tested_ingredients)
    def test_get_type(self, test_ingredient):
        tested_type = test_ingredient["type"]
        ingredient = Ingredient(ingredient_type=tested_type,
                                name=test_ingredient["name"],
                                price=test_ingredient["price"])
        assert ingredient.get_type() == tested_type, "Ингредиент должен иметь заданный тип"

    @pytest.mark.parametrize("test_ingredient", tested_ingredients)
    def test_get_price(self, test_ingredient):
        tested_price = test_ingredient["price"]
        ingredient = Ingredient(ingredient_type=test_ingredient["type"],
                                name=test_ingredient["name"],
                                price=tested_price)
        assert ingredient.get_price() == tested_price, "Ингредиент должен иметь заданную цену"
