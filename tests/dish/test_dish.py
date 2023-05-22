from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


def test_dish(capsys):
    lasanha = Dish("lasanha", 30.00)
    ravioli = Dish("ravioli", 40.00)
    massa_lasanha = Ingredient("massa de lasanha")
    presunto = Ingredient("presunto")

    assert lasanha.name == "lasanha"
    assert lasanha.price == 30.00

    assert lasanha.__hash__() == hash(lasanha.__repr__())
    assert lasanha.__eq__(ravioli) is False
    assert lasanha.__eq__(lasanha) is True

    lasanha.add_ingredient_dependency(massa_lasanha, 1)
    lasanha.add_ingredient_dependency(presunto, 2)

    assert lasanha.get_ingredients() == {massa_lasanha, presunto}
    assert lasanha.recipe == {
        massa_lasanha: 1,
        presunto: 2,
    }

    assert lasanha.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    print(lasanha)
    out, _ = capsys.readouterr()
    assert out == "Dish('lasanha', R$30.00)\n"

    with pytest.raises(TypeError, match="Dish price must be float"):
        Dish("Invalid", "10.00")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero"
    ):
        Dish("Invalid", -1)
