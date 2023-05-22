from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient(capsys):
    bacon = Ingredient("bacon")
    farinha = Ingredient("farinha")

    assert bacon.name == "bacon"
    assert bacon.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert bacon.__hash__() == hash("bacon")
    assert bacon.__eq__(farinha) is False
    assert bacon.__eq__(bacon) is True

    print(bacon)
    out, _ = capsys.readouterr()

    assert out == "Ingredient('bacon')\n"
