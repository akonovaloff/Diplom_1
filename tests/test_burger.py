import pytest
from test_data.test_data import tested_buns, tested_ingredients
from praktikum.burger import Burger


class TestBurger:

    @pytest.mark.parametrize("tested_bun", tested_buns)
    def test_set_buns(self, tested_bun):
        """Тест на добавление булочки в бургер"""
        burger = Burger()
        burger.set_buns(tested_bun)
        assert burger.bun == tested_bun, "Булочка в бургере должна соответствовать добавленной"

    @pytest.mark.parametrize("tested_ingredient", tested_ingredients)
    def test_add_ingredient_added_single_ingredient(self, tested_ingredient):
        """Тест на добавление единственного ингредиента в бургер"""
        burger = Burger()
        burger.add_ingredient(tested_ingredient)
        print(str(tested_ingredient))
        print(str(burger.ingredients))
        assert burger.ingredients == [tested_ingredient], "Ингредиент в бургере должен соответствовать добавленному"

    def test_add_ingredient_multiply_ingredients(self, ingredients=tested_ingredients):
        """Тест на добавление нескольких ингредиентов в бургер"""
        burger = Burger()
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
            assert ingredient in burger.ingredients, "Добавленный ингредиент должен присутствовать в бургере"
        assert len(burger.ingredients) == len(
            ingredients), "Число ингредиентов в бургере должно соответствовать добавленному"

    def test_remove_ingredient(self, ingredients=tested_ingredients):
        """Тест на удаление одного ингредиента из бургера"""
        burger = Burger()
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
            assert ingredient in burger.ingredients, "Добавленный ингредиент должен присутствовать в бургере"
        assert len(burger.ingredients) == len(
            ingredients), "Число ингредиентов в бургере должно соответствовать добавленному"
        burger.remove_ingredient(-1)
        assert ingredients[-1] not in burger.ingredients, "Запрошенный ингредиент должен быть удален из бургера"
        assert ingredients[:-1] == burger.ingredients, "Из бургера должен быть удалён только запрошенный ингредиент"