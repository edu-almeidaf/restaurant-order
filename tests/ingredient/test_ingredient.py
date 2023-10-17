from src.models.ingredient import Ingredient, Restriction

restrictions_manteiga = {
    Restriction.LACTOSE,
    Restriction.ANIMAL_DERIVED,
}

restrictions_ravioli = {
    Restriction.LACTOSE,
    Restriction.GLUTEN,
}


def test_ingredient():
    ingredient1 = Ingredient("manteiga")
    ingredient2 = Ingredient("massa de ravioli")

    assert ingredient1.name == "manteiga"
    assert ingredient2.name == "massa de ravioli"

    assert (ingredient1 == ingredient1) is True
    assert (ingredient1 == ingredient2) is False

    assert ingredient1.__hash__() == hash("manteiga")
    assert ingredient1.__hash__() != ingredient2.__hash__()

    assert repr(ingredient1) == "Ingredient('manteiga')"
    assert repr(ingredient2) != "Ingredient('manteiga')"

    assert ingredient1.restrictions == restrictions_manteiga
    assert ingredient2.restrictions == restrictions_ravioli

    assert ingredient1 != ingredient2
