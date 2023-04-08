from project.band_members.musician import Musician


class Drummer(Musician):
    POSSIBLE_SKILLS = ["play the drums with drumsticks",
                        "play the drums with drum brushes",
                        "read sheet music"]

    def __init__(self, name, age):
        super().__init__(name, age)
        self.possible_skills = self.POSSIBLE_SKILLS
