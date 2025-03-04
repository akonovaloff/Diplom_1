import pytest
from praktikum.bun import Bun
from test_data.test_data import tested_buns


class TestBun:

    @pytest.mark.parametrize("test_bun", tested_buns)
    def test_get_name(self, test_bun):
        tested_name = test_bun["name"]
        bun = Bun(tested_name,
                  test_bun["price"])

        assert bun.get_name() == tested_name, "Булочка должна иметь заданное имя"

    @pytest.mark.parametrize("test_bun", tested_buns)
    def test_get_price(self, test_bun):
        tested_price = test_bun["price"]
        bun = Bun(test_bun["name"],
                  test_bun["price"])

        assert bun.get_price() == tested_price, "Булочка должна иметь заданную цену"
