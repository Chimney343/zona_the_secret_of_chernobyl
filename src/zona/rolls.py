from .dices import ZonaDice

class ZonaStandardRollTest:
    def __init__(self):
        pass

    def count_roll_effect(self, rolls):
        assert len(rolls) == 3, "Provide a list with at least 3 rolls."

        roll_face_values = [roll.get('face_value') for roll in rolls]
        roll_faces = [roll.get('face') for roll in rolls]

        roll_effect = sum(roll_face_values)

        n_triangles = roll_faces.count('triangle')
        if n_triangles >= 2:
            damage = True
        else:
            damage = False

        return {'roll_effect': roll_effect, 'damage': damage}

    def roll_test(self):
        dice = ZonaDice()

        rolls = [
            dice.roll(),
            dice.roll(),
            dice.roll(),
        ]

        rolls_effect = self.count_roll_effect(rolls=rolls)

        self.rolls = rolls
        self.rolls_effect = rolls_effect