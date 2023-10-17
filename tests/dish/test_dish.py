from src.models.dish import Dish, Ingredient
from src.models.ingredient import Restriction
import pytest

restrictions_macarrao = {
    Restriction.ANIMAL_MEAT,
    Restriction.ANIMAL_DERIVED,
    Restriction.LACTOSE,
}

ingredients_macarrao = {Ingredient("carne"), Ingredient("queijo parmesão")}


# Req 2
def test_dish():
    dish1 = Dish("Macarrão a bolonhesa", 15)
    dish2 = Dish("Brownie de chocolate", 10)
    dish3 = Dish("Brownie de chocolate", 10)
    dish1.add_ingredient_dependency(Ingredient("carne"), 350)
    dish1.add_ingredient_dependency(Ingredient("queijo parmesão"), 20)

    assert dish1.name == "Macarrão a bolonhesa"
    assert dish2.name == "Brownie de chocolate"

    assert dish2 == dish3
    assert dish1 != dish2

    assert dish1.__hash__() != dish2.__hash__()
    assert dish2.__hash__() == dish3.__hash__()

    assert dish1.get_restrictions() == restrictions_macarrao

    assert dish1.get_ingredients() == ingredients_macarrao

    assert len(dish1.recipe) == 2

    assert repr(dish1) == "Dish('Macarrão a bolonhesa', R$15.00)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Macarrão a bolonhesa", "R$15.00")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Macarrão a bolonhesa", -15)
