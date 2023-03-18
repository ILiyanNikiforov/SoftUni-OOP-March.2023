from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    valid_team_names = ["Mercedes", "Red Bull"]

    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None
        self.mercedes_team: MercedesTeam or None = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.valid_team_names:
            raise ValueError("Invalid team name!")

        if team_name == self.valid_team_names[0]:
            self.mercedes_team = MercedesTeam(budget)
        else:
            self.red_bull_team = RedBullTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        return self.get_race_results(race_name, red_bull_pos, mercedes_pos)

    def get_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        ahead_team = "Red Bul" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bul_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bul_revenue}. Mercedes: {mercedes}." \
               f" {ahead_team} is ahead at the {race_name} race."
