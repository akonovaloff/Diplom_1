import pytest
from praktikum.ingredient import Ingredient
from helpers.generators import random_ingredient_type, random_ingredient_name, random_price


class TestIngredient:
    def test_get_name(self):
        """Тест проверяет имя созданного ингредиента"""
        ingr_type = random_ingredient_type()
        name = random_ingredient_name()
        price = random_price()
        ingredient = Ingredient(ingr_type, name, price)
        assert ingredient.get_name() == name, "Ингредиент должен иметь заданное имя"

    def test_get_type(self):
        """Тест проверяет тип созданного ингредиента"""
        ingr_type = random_ingredient_type()
        name = random_ingredient_name()
        price = random_price()
        ingredient = Ingredient(ingr_type, name, price)
        assert ingredient.get_type() == ingr_type, "Ингредиент должен иметь заданный тип"

    def test_get_price(self):
        """Тест проверяет цену созданного ингредиента"""
        ingr_type = random_ingredient_type()
        name = random_ingredient_name()
        price = random_price()
        ingredient = Ingredient(ingr_type, name, price)
        assert ingredient.get_price() == price, "Ингредиент должен иметь заданную цену"
