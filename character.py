# Creates character objects
class Character:
    # Defines what a character should look like
    def __init__(self, name: str, sex: str, race: str, level: int, dex: int, strength: int):
        self.name = name
        self.sex = sex
        self.race = race
        self.level = level
        self.dex = dex
        self.strength = strength

    # Level increase method
    def level_up(self, level_increase):
        self.level += level_increase

    # Dex increase method
    def increase_dex(self, dex_increase):
        self.dex += dex_increase

    # Strength increase method
    def increase_strength(self, strength_increase):
        self.strength += strength_increase

    # Return methods
    def return_name(self):
        return self.name

    def return_sex(self):
        return self.sex

    def return_race(self):
        return self.race

    def return_level(self):
        return self.level

    def return_dex(self):
        return self.dex

    def return_strength(self):
        return self.strength
