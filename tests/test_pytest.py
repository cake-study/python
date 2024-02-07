import pytest
from qaseio.pytest import qase

from cake import Cake


@qase.id(1)
@qase.title("Make a cake")
def test_make_a_cake():
    # step 1: Get new ingredients
    with qase.step("Get new ingredients"):
        cake = Cake()
        assert cake.state() == "uncooked"

    # step 2: Shake ingredients
    with qase.step("Shake ingredients"):
        cake.shake()
        assert cake.state() == "raw"

    # step 3: Bake the cake
    with qase.step("Bake the cake"):
        cake.bake()
        assert cake.state() == "baked"

    # step 4: Take the cake home
    with qase.step("Take the cake home"):
        cake.take()
        assert cake.state() == "taken"


@qase.id(2)
@qase.title("Burn a cake")
def test_burn_a_cake():
    # step 1: Take ingredients, shake and bake them
    with qase.step("Take ingredients, shake and bake them"):
        cake = Cake()
        cake.shake()
        cake.bake()
        assert cake.state() == "baked"

    # step 2: Bake the cake more
    with qase.step("Bake the cake more"):
        cake.bake()
        assert cake.state() == "burned"


@qase.id(7)
@qase.title("Shake a cake repeatedly")
def test_shake_a_cake():
    # step 1: Take ingredients and shake them a lot
    with qase.step("Take ingredients and shake them a lot"):
        cake = Cake()
        cake.shake()
        cake.shake()
        cake.shake()
        assert cake.state() == "raw"

    # step 2: Bake the cake and take it home
    with qase.step("Bake the cake and take it home"):
        cake.bake()
        cake.take()
        assert cake.state() == "taken"


@qase.id(15)
@qase.title("Make parametrized cakes")
@pytest.mark.parametrize("flavor, expected_str", [
    ("cherry", "cherry cake, baked"),
    ("chocolate", "chocolate cake, baked"),
    ("strawberry", "strawberry cake, baked"),
])
def test_cake_str(flavor, expected_str):
    cake = Cake(flavor=flavor)
    cake.shake()
    cake.bake()
    assert str(cake) == expected_str


# When we want to make a "parameterized" test, but match each variant
# to a separate test case at Qase:
def make_test_function(flavor, expected_str, qase_id):
    # should have named it test_func,
    # but then pytest would recognize it as a separate test
    @qase.id(qase_id)
    @qase.title(f"Make {flavor} cakes")
    def func_test():
        cake = Cake(flavor=flavor)
        cake.shake()
        cake.bake()
        assert str(cake) == expected_str

    func_test.__name__ = f"test_{flavor}_cake"
    return func_test


test_cases = [
    ("cherry", "cherry cake, baked", 17),
    ("chocolate", "chocolate cake, baked", 18),
    ("strawberry", "strawberry cake, baked", 19)
]

# Dynamically create and add test functions to the global namespace
for flavor, expected_str, qase_id in test_cases:
    func_test = make_test_function(flavor, expected_str, qase_id)
    globals()[func_test.__name__] = func_test
