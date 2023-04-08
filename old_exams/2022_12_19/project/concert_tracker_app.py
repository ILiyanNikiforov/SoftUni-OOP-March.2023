from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class MusicianFactory:
    @staticmethod
    def produce_musician(m_type, name, age):
        if m_type == "Guitarist":
            return Guitarist(name, age)
        elif m_type == "Drummer":
            return Drummer(name, age)
        elif m_type == "Singer":
            return Singer(name, age)


class ConcertTrackerApp:
    VALID_MUSICIANS = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def is_band_already(self, band_name):
        if [band for band in self.bands if band.name == band_name]:
            return True

    def is_musician_already(self, musician_name):
        if [musician for musician in self.musicians if musician.name == musician_name]:
            return True

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        if self.is_musician_already(name):
            raise ValueError(f"{name} is already a musician!")

        musician = MusicianFactory.produce_musician(musician_type, name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.is_band_already(name):
            raise ValueError(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{band.name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if [conc for conc in self.concerts if conc.place == place]:
            concert = [conc for conc in self.concerts if conc.place == place][0]
            raise ValueError(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician_result = self.__find_musician_by_name(musician_name)
        if not musician_result:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band_result = self.__find_band_by_name(band_name)
        if not band_result:
            raise Exception(f"{band_name} isn't a band!")

        band_result.add_member(musician_result)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician_result = self.__find_musician_by_name(musician_name)
        if not musician_result:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band_result = self.__find_band_by_name(band_name)
        if not band_result:
            raise Exception(f"{band_name} isn't a band!")

        band_result.remove_member(musician_result)
        return f"{musician_name} was added to {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        musicians_set = set(m.__class__.__name__ for m in band.members)
        if len(musicians_set) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        if concert.genre == "Rock":
            skills_set = []
            for m in band.members:
                skills_set.extend(m.skills)
            needed_skills = {"play the drums with drumsticks", "sing high pitch notes", "play rock"}
            if not needed_skills.issubset(set(skills_set)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            skills_set = []
            for m in band.members:
                skills_set.extend(m.skills)
            needed_skills = {"play the drums with drumsticks", "sing low pitch notes", "play metal"}
            if not needed_skills.issubset(set(skills_set)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            skills_set = []
            for m in band.members:
                skills_set.extend(m.skills)
            needed_skills = {"play the drums with drum brushes", "sing low pitch notes", "sing high pitch notes", "play jazz"}
            if not needed_skills.issubset(set(skills_set)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def __find_musician_by_name(self, name):
        for musician in self.musicians:
            if musician.name == name:
                return musician

    def __find_band_by_name(self, name):
        for band in self.bands:
            if band.name == name:
                return band

    def __find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert


