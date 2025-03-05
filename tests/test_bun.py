import pytest
from praktikum.bun import Bun
from helpers.generators import random_bun_name, random_price


class TestBun:

    def test_get_name(self):
        """Тест проверяет имя созданной булочки"""
        bun_name = random_bun_name()
        bun_price = random_price()
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun.name == bun_name, "Булочка должна иметь заданное имя"

    def test_get_price(self):
        """Тест проверяет цену созданной булочки"""
        bun_name = random_bun_name()
        bun_price = random_price()
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun.price, "Булочка должна иметь заданную цену"
