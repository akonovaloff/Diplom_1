import pytest
from test_data.test_data import tested_buns, tested_ingredients
from praktikum.burger import Burger


class TestBurger:

    @pytest.mark.parametrize("tested_bun", tested_buns)
    def test_set_buns(self, tested_bun):
        burger = Burger()
        burger.set_buns(tested_bun)
        assert burger.bun == tested_bun, "Булочка в бургере должна соответствовать добавленной"

    @pytest.mark.parametrize("tested_ingredient", tested_ingredients)
    def test_add_ingredient_added_single_ingredient(self, tested_ingredient):
        burger = Burger()
        burger.add_ingredient(tested_ingredient)
        print(str(tested_ingredient))
        print(str(burger.ingredients))
        assert burger.ingredients == [tested_ingredient], "Ингредиент в бургере должен соответствовать добавленному"

    def test_add_ingredient_multiply_ingredients(self, ingredients=tested_ingredients):
        burger = Burger()
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
            assert ingredient in burger.ingredients, "Добавленный ингредиент должен присутствовать в бургере"