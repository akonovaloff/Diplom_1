import pytest
from praktikum.bun import Bun


class TestBun:
    test_bun = {"bun_name": "Super bun", "bun_price": 15}

    def test_get_name(self):
        tested_name = self.test_bun["bun_name"]
        bun = Bun(tested_name,
                  self.test_bun["bun_price"])

        assert bun.get_name() == tested_name, "Булочка должна иметь заданное имя"

    def test_get_price(self):
        tested_price = self.test_bun["bun_price"]
        bun = Bun(self.test_bun["bun_name"],
                  self.test_bun["bun_price"])

        assert bun.get_price() == tested_price, "Булочка должна иметь заданную цену"
