from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Grigor", 27, 2000)

    def test_init(self):
        assert self.player.name == "Grigor"
        assert self.player.age == 27
        assert self.player.points == 2000
        assert self.player.wins == []

    def test_raise_not_correct_len_of_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "aa"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_raise_age_under_18(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_raise_add_already_added_tournament(self):
        self.player.add_new_win("AO")
        self.player.add_new_win("WB")
        result = self.player.add_new_win("AO")
        assert result == 'AO has been already added to the list of wins!'
        assert self.player.wins == ['AO', 'WB']

    def test_add_new_tournament(self):
        self.player.add_new_win("WB")
        assert self.player.wins == ["WB"]

    def test_lt_other_is_larger(self):
        player = TennisPlayer("Grigor", 27, 1000)
        other = TennisPlayer("Novak", 31, 2000)
        result = str(player < other)
        self.assertEqual(result, 'Novak is a top seeded player and he/she is better than Grigor')

    def test_lt_other_is_lower(self):
        player = TennisPlayer("Grigor", 27, 2000)
        other = TennisPlayer("Novak", 31, 1000)
        result = str(player < other)
        self.assertEqual(result, 'Grigor is a better player than Novak')

    def test_string_represent(self):
        self.player.wins = ["WB", "AO"]
        assert f"Tennis Player: Grigor\nAge: 27\nPoints: 2000.0\nTournaments won: WB, AO" == str(self.player)


if __name__ == "__main__":
    main()

