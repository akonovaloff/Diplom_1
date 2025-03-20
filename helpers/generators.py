from faker import Faker
from random import randint, choice
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

fake = Faker("en_US")


def random_bun_name() -> str:
    return fake.color_name().lower() + " bun"


def random_price() -> int:
    return randint(10, 500)


def random_ingredient_type() -> str:
    return choice([INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE])


def random_ingredient_name() -> str:
    second_word = choice(["juicy", "spicy", "smoky", "crispy", "tangy", "savory"])
    third_word = choice(["pepper", "relish", "onion", "bacon", "pickles", "jalapeno"])
    return f"{fake.color_name().lower()} {second_word} {third_word}"


def random_bun() -> Bun:
    return Bun(random_bun_name(), random_price())


def random_ingredient() -> Ingredient:
    return Ingredient(random_ingredient_type(), random_ingredient_name(), random_price())
