from cake import Cake


def test_make_a_cake():
    # step 1: Get new ingredients
    cake = Cake()
    assert cake.state() == "uncooked"

    # step 2: Shake ingredients
    cake.shake()
    assert cake.state() == "raw"

    # step 3: Bake the cake
    cake.bake()
    assert cake.state() == "baked"

    # step 4: Take the cake home
    cake.take()
    assert cake.state() == "taken"


def test_burn_a_cake():
    # step 1: Take ingredients, shake and bake them
    cake = Cake()
    cake.shake()
    cake.bake()
    assert cake.state() == "baked"

    # step 2: Bake the cake more
    cake.bake()
    assert cake.state() == "burned"


def test_shake_a_cake():
    # step 1: Take ingredients and shake them a lot
    cake = Cake()
    cake.shake()
    cake.shake()
    cake.shake()
    assert cake.state() == "raw"

    # step 2: Bake the cake and take it home
    cake.bake()
    cake.take()
    assert cake.state() == "taken"
