# It's a bird; It's a plane; It's a battle... between musicians? 

import random

class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength

    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength * 100:.1f} / 100 strength)"
    
    def does_break(self):
        # There's a 50% chance the musician's instrument break.
        return random.random() < 0.5 * self.strength


class Musician:
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(instruments)

    def __str__(self):
        instrument_info = ", ".join(str(instrument) for instrument in self.instruments)
        return f"Musician object '{self.stage_name}', owning {instrument_info}"

    def pick_instrument(self, instrument_index=None):
        if not self.instruments:
            return None

        if instrument_index is None:
            return random.choice(self.instruments)
        elif instrument_index >= self.number_of_instruments:
            return self.instruments[-1]
        else:
            return self.instruments[instrument_index]


def get_name_of_battle_winner(musician_a, musician_b):
    if not musician_a.instruments and not musician_b.instruments:
        return "NO CONTEST"
    elif not musician_a.instruments:
        return musician_b.stage_name
    elif not musician_b.instruments:
        return musician_a.stage_name

    instrument_a = musician_a.pick_instrument()
    instrument_b = musician_b.pick_instrument()

    print(f"{musician_a.stage_name} picked {instrument_a}!")
    print(f"{musician_b.stage_name} picked {instrument_b}!")

    if instrument_a.strength > instrument_b.strength:
        if instrument_b.does_break():
            return musician_a.stage_name
        else:
            return musician_b.stage_name
    elif instrument_b.strength > instrument_a.strength:
        if instrument_a.does_break():
            return musician_b.stage_name
        else:
            return musician_a.stage_name
    else:
        print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
        return random.choice([musician_a.stage_name, musician_b.stage_name])

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]

    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)

    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")

if __name__ == "__main__":
    main()
