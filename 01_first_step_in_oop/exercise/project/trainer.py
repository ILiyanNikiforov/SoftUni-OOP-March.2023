from pokemon import Pokemon

class Trainer:
    def __init__(self, name:str):
        self.name = name
        # List with my pokemons
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        try:
            pokemon = [pokemon for pokemon in self.pokemons if pokemon.name == pokemon_name][0]
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon.name}"
        except IndexError:
            return "Pokemon is not caught"

        # for current_pokemon in self.pokemons:
        #     if pokemon_name == current_pokemon.name:
        #         self.pokemons.remove(current_pokemon)
        #         return f"You have released {current_pokemon.name}"
        # return "Pokemon is not caught"

        # try:
        #     pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        #     self.pokemons.remove(pokemon)
        #     return f"You have released {pokemon.name}"
        # except StopIteration:
        #     return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pokemon in self.pokemons:
            result.append(f"- {pokemon.pokemon_details()}")
        return "\n".join(result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
