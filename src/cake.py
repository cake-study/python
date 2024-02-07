
class Cake:
    def __init__(self, flavor: str = "apple"):
        self._state = "uncooked"
        self.flavor = flavor

    def __str__(self):
        return f"{self.flavor} cake, {self.state()}"

    def shake(self):
        if self._state == "uncooked":
            self._state = "raw"
        # elif self._state == "raw":
        #     self._state = "raw"
        elif self._state == "burned":
            raise Exception("You shake the burned cake in despair, but alas, it's burned.")
        elif self._state == "taken":
            raise Exception("Nothing left to shake, make a new cake!")

    def bake(self):
        if self._state == "raw":
            self._state = "baked"
        elif self._state == "baked":
            self._state = "burned"
        elif self._state == "uncooked":
            raise Exception("Don't bake raw ingredients, shake them first!")
        elif self._state == "taken":
            raise Exception("Nothing left to bake, make a new cake!")

    def take(self):
        if self._state == "baked":
            self._state = "taken"
        elif self._state == "taken":
            raise Exception("Nothing left to take, make a new cake!")
        else:
            raise Exception("The cake is not ready yet!")

    def state(self):
        return self._state
