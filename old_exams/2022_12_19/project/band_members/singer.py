from project.band_members.musician import Musician


class Singer(Musician):
    POSSIBLE_SKILLS = ["sing high pitch notes", "sing low pitch notes"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.possible_skills = self.POSSIBLE_SKILLS



# a = Singer("Gosh", 18)
#
# a.learn_new_skill("sing high pitch notes")
# print(a.skills)
# a.learn_new_skill("sing high pitch notes")
# print(a.skills)