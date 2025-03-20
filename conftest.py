from praktikum.burger import Burger
from praktikum.database import Database
import pytest



@pytest.fixture()
def burger() -> Burger:
    db = Database()
    brgr = Burger()
    brgr.set_buns(db.available_buns()[1])
    brgr.add_ingredient(db.available_ingredients()[1])
    return brgr