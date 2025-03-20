import pytest

from helpers.generators import random_bun, random_ingredient
from praktikum.burger import Burger
from random import randint, choice


class TestBurger:

    def test_set_buns(self):
        """Тест на добавление булочки в бургер"""
        # Создаём булочку
        bun = random_bun()
        # Создаём бургер
        burger = Burger()
        # Добавляем булочку в бургер
        burger.set_buns(bun)
        # Проверяем, что булочка добавлена
        assert burger.bun == bun, "Булочка в бургере должна соответствовать добавленной"

    @pytest.mark.parametrize("ingredients_quantity", ((1), (2), (3), (4), (5), (6)))
    def test_add_ingredient_multiply_ingredients(self, ingredients_quantity):
        """Тест на добавление различного числа ингредиентов в бургер"""
        # Создаем бургер
        burger = Burger()
        # Задаём число ингредиентов
        quantity = ingredients_quantity
        for _ in range(quantity):
            # Создаем ингредиент
            ingredient = random_ingredient()
            # Добавляем ингредиент в бургер
            burger.add_ingredient(ingredient)
            # Проверяем, что ингредиент добавлен в бургер
            assert ingredient in burger.ingredients, "Добавленный ингредиент должен присутствовать в бургере"
        # Проверяем общее число добавленных ингредиентов
        assert len(burger.ingredients) == quantity, "Число ингредиентов в бургере должно соответствовать добавленному"

    @pytest.mark.parametrize("ingredients_quantity", ((1), (2), (3), (4), (5), (6)))
    def test_remove_ingredient(self, ingredients_quantity):
        """Тест на удаление одного ингредиента из бургера"""
        # Создаем бургер
        burger = Burger()
        # Создаем пустой список ингредиентов
        ingredient_list = []
        # Задаем число ингредиентов
        quantity = ingredients_quantity
        for _ in range(quantity):
            # Сохраняем созданный ингредиент
            ingredient_list.append(random_ingredient())
            # Добавляем созданный ингредиент в бургер
            burger.add_ingredient(ingredient_list[-1])
        # Задаём индекс ингредиента для удаления
        remove_index = choice(range(quantity))
        # Удаляем ингредиент из бургера по индексу
        burger.remove_ingredient(remove_index)
        # Проверяем, что выбранный ингредиент удалён
        assert ingredient_list[
                   remove_index] not in burger.ingredients, "Запрошенный ингредиент должен быть удален из бургера"
        # Проверяем число оставшихся ингредиентов
        assert len(burger.ingredients) == quantity - 1, "Из ингредиентов должен быть удален только один элемент"

    @pytest.mark.parametrize("ingredients_quantity", ((1), (2), (3), (4), (5), (6)))
    def test_move_ingredient(self, ingredients_quantity):
        """Тест на перемещение ингредиента в бургере"""
        # Создаём бургер
        burger = Burger()
        # Задаём число ингредиентов
        quantity = ingredients_quantity
        # Создаем пустой список ингредиентов
        ingredient_list = []
        for _ in range(quantity):
            # Сохраняем созданный ингредиент
            ingredient_list.append(random_ingredient())
            # Добавляем созданный ингредиент в бургер
            burger.add_ingredient(ingredient_list[-1])
        # Задаём индекс ингредиента, который будем перемещать
        move_index_1 = choice(range(quantity))
        # Задаём индекс, куда будем перемещать
        move_index_2 = choice(range(quantity))
        # Перемещаем ингредиент по индексам
        burger.move_ingredient(move_index_1, move_index_2)
        # Проверяем, что выбранный ингредиент перемещен на указанную позицию
        assert ingredient_list[move_index_1] == burger.ingredients[
            move_index_2], "Запрошенный ингредиент должен быть перемещен на указанную позицию"

    @pytest.mark.parametrize("ingredients_quantity", ((1), (2), (3), (4), (5), (6)))
    def test_get_price(self, ingredients_quantity):
        """Тест на подсчет цены бургера с разным числом ингредиентов"""
        # Создаем бургер
        burger = Burger()
        # Создаем булочку
        bun = random_bun()
        # Контрольный подсчет цены бургера
        check_price = bun.price * 2
        # Добавляем булочку в бургер
        burger.set_buns(bun)
        # Проверяем, что цена бургера изменилась с учетом добавленной булочки
        assert burger.get_price() == check_price, "Цена бургера без начинок должна равняться цене за две булочки"
        for _ in range(ingredients_quantity):
            # Создаём ингредиент
            ingredient = random_ingredient()
            # Контрольный подсчет цены бургера
            check_price += ingredient.price
            # Добавляем ингредиент в бургер
            burger.add_ingredient(ingredient)
            # Проверяем, что цена бургера изменяется с учетом добавленного ингредиента
            assert burger.get_price() == check_price, "В цене бургера должна учитываться цена каждого ингредиента"

    @pytest.mark.parametrize("ingredients_quantity", ((1), (2), (3), (4), (5), (6)))
    def test_get_receipt(self, ingredients_quantity):
        """Тест на составление рецепта бургера с разным числом ингредиентов"""
        # Создаем бургер
        burger = Burger()
        # Создаем булочку
        bun = random_bun()
        # Добавляем булочку в бургер
        burger.set_buns(bun)
        # Проверяем, что название булочки содержится в рецепте бургера
        assert bun.name in burger.get_receipt(), "Рецепт бургера должен содержать название булочки"
        for _ in range(ingredients_quantity):
            # Создаем ингредиент
            ingredient = random_ingredient()
            # Добавляем ингредиент в бургер
            burger.add_ingredient(ingredient)
            # Проверяем, что название ингредиента содержится в рецепте бургера
            assert ingredient.name in burger.get_receipt(), "Рецепт бургера должен содержать название добавленного ингредиента"
