from praktikum.bun import Bun

test_bun = {"name": "Super bun", "price": 15}


class TestBun:

    def test_get_name(self):
        tested_name = test_bun["name"]
        bun = Bun(tested_name,
                  test_bun["price"])

        assert bun.get_name() == tested_name, "Булочка должна иметь заданное имя"

    def test_get_price(self):
        tested_price = test_bun["price"]
        bun = Bun(test_bun["name"],
                  test_bun["price"])

        assert bun.get_price() == tested_price, "Булочка должна иметь заданную цену"
