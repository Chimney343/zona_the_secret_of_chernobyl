from random import choice
class ZonaDice:
    faces = ['minus', 'minus', 'plus', 'plus', 'triangle', 'null']
    face_value_lookup = {
        'minus': -1,
        'plus': 1,
        'triangle': 0,
        'null': 0,
    }
    def __init__(self):
        pass

    def roll(self):
        face = choice(self.faces)
        face_value = self.face_value_lookup.get(face)
        return {'face': face, 'face_value': face_value}
