from project.band_members.musician import Musician


class Guitarist(Musician):
    POSSIBLE_SKILLS = ["play metal", "play rock", "play jazz"]

    def __init__(self, name, age):
        super().__init__(name, age)
        self.possible_skills = self.POSSIBLE_SKILLS



# a = Guitarist("Gosh", 18)
#
# a.learn_new_skill("play metal")
# print(a.skills)
# a.learn_new_skill("play metal")
# print(a.skills)