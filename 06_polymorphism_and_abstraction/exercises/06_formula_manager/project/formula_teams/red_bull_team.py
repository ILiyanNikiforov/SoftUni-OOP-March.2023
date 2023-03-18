from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250_000

    @property
    def sponsors(self):
        return {
            "Oracle": {1: 1_500_000, 2: 800_000},
            "Honda": {8: 20_000, 9: 10_000}
        }

    @property
    def expenses_for_one_race(self):
        return self.EXPENSES_PER_RACE

