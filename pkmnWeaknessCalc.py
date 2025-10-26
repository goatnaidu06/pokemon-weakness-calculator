#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:24:48 2025

@author: NeilN
"""

import pandas as pd

# Type effectiveness chart (Offense types as rows, Defense types as columns)
pokemon = {
    "Bug":     [1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 2, 1, 1, 0.5, 2, 1, 0.5, 1, 1],
    "Dark":    [1, 0.5, 1, 1, 0.5, 0.5, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    "Dragon":  [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1],
    "Electric":[1, 1, 0.5, 0.5, 1, 1, 1, 2, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 2, 1],
    "Fairy":   [1, 2, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 0.5, 1, 1],
    "Fighting":[0.5, 2, 1, 1, 0.5, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 2, 1, 1],
    "Fire":    [2, 1, 0.5, 1, 1, 1, 0.5, 1, 1, 1, 2, 2, 1, 1, 1, 0.5, 2, 0.5, 1],
    "Flying":  [2, 1, 1, 0.5, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0.5, 0.5, 1, 1],
    "Ghost":   [1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1],
    "Ground":  [0.5, 1, 1, 2, 1, 1, 2, 0, 1, 1, 0.5, 1, 1, 2, 1, 2, 2, 1, 1],
    "Grass":   [0.5, 1, 0.5, 1, 1, 1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 0.5, 1, 2, 0.5, 2, 1],
    "Ice":     [1, 1, 2, 1, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1],
    "Normal":  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 1],
    "Poison":  [1, 1, 1, 1, 2, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 0.5, 1, 0.5, 0, 1, 1],
    "Psychic": [1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 1],
    "Rock":    [2, 1, 1, 1, 1, 0.5, 2, 2, 1, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 1, 1],
    "Steel":   [1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 0.5, 1],
    "Water":   [1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 2, 1, 0.5, 1],
    " ":    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

pokemon_g25 = {
    "Bug":     [1, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 2, 1, 1, 0.5, 2, 1, 0.5, 1, 1],
    "Dark":    [1, 0.5, 1, 1, 0.5, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0.5, 1, 1],
    "Dragon":  [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1],
    "Electric":[1, 1, 0.5, 0.5, 1, 1, 2, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 2, 1],
    "Fighting":[0.5, 2, 1, 1, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 2, 1, 1],
    "Fire":    [2, 1, 0.5, 1, 1, 0.5, 1, 1, 1, 2, 2, 1, 1, 1, 0.5, 2, 0.5, 1],
    "Flying":  [2, 1, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0.5, 0.5, 1, 1],
    "Ghost":   [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0.5, 1, 1],
    "Ground":  [0.5, 1, 1, 2, 1, 2, 0, 1, 1, 0.5, 1, 1, 2, 1, 2, 2, 1, 1],
    "Grass":   [0.5, 1, 0.5, 1, 1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 0.5, 1, 2, 0.5, 2, 1],
    "Ice":     [1, 1, 2, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1],
    "Normal":  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 1],
    "Poison":  [1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 0.5, 1, 0.5, 0, 1, 1],
    "Psychic": [1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 1],
    "Rock":    [2, 1, 1, 1, 0.5, 2, 2, 1, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 1, 1],
    "Steel":   [1, 1, 1, 0.5, 1, 0.5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 0.5, 1],
    "Water":   [1, 1, 0.5, 1, 1, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 2, 1, 0.5, 1],
    " ":    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

pokemon_g1 = {
    "Bug":     [1, 1, 1, 0.5, 0.5, 0.5, 0.5, 1, 2, 1, 1, 0.5, 2, 1, 1, 1],
    "Dragon":  [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Electric":[1, 0.5, 0.5, 1, 1, 2, 1, 0, 0.5, 1, 1, 1, 1, 1, 2, 1],
    "Fighting":[0.5, 1, 1, 1, 1, 0.5, 0, 1, 1, 2, 2, 0.5, 0.5, 2, 1, 1],
    "Fire":    [2, 0.5, 1, 1, 0.5, 1, 1, 1, 2, 2, 1, 1, 1, 0.5, 0.5, 1],
    "Flying":  [2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0.5, 1, 1],
    "Ghost":   [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 1],
    "Ground":  [0.5, 1, 2, 1, 2, 0, 1, 1, 0.5, 1, 1, 2, 1, 2, 1, 1],
    "Grass":   [0.5, 0.5, 1, 1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 0.5, 1, 2, 2, 1],
    "Ice":     [1, 2, 1, 1, 0.5, 2, 1, 2, 2, 0.5, 1, 1, 1, 1, 0.5, 1],
    "Normal":  [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0.5, 1, 1],
    "Poison":  [1, 1, 1, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 0.5, 1, 0.5, 1, 1],
    "Psychic": [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 1, 1],
    "Rock":    [2, 1, 1, 0.5, 2, 2, 1, 0.5, 1, 2, 1, 1, 1, 1, 1, 1],
    "Water":   [1, 0.5, 1, 1, 2, 1, 1, 2, 0.5, 1, 1, 1, 1, 2, 0.5, 1],
    " ":    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}


# Create DataFrame with offense types as rows and defense types as columns
df = pd.DataFrame(pokemon, index=pokemon.keys()).T
df_g1 = pd.DataFrame(pokemon_g1, index=pokemon.keys()).T
df_g25 = pd.DataFrame(pokemon_g25, index=pokemon.keys()).T

data_url = 'https://raw.githubusercontent.com/goatnaidu06/pokemon-weakness-calculator/refs/heads/main/Pokemon.csv'
poke_df = pd.read_csv(data_url)
poke_df.columns = poke_df.columns.str.strip()
poke_df['Form'] = poke_df['Form'].fillna('').str.strip()



# Load the provided Pokémon data

# Ensure column names are correctly formatted
poke_df.columns = poke_df.columns.str.strip()

# Extract relevant columns


# Type effectiveness chart (Offense types as rows, Defense types as columns)

def get_pokemon_weaknesses(pokemon_name, form_name=None):
    pokemon = poke_df[poke_df['Name'].str.lower() == pokemon_name.lower()]
    if form_name:
        pokemon = poke_df[
            (poke_df['Name'].str.lower() == pokemon_name.lower()) & 
            (poke_df['Form'].str.lower() == form_name.lower())
        ]
    else:
        pokemon = poke_df[
            (poke_df['Name'].str.lower() == pokemon_name.lower()) & 
            (poke_df['Form'] == '')
        ]
    
    if pokemon.empty:
        return "Error: Pokémon not found."
    gen = pokemon.iloc[0]['Generation']
    type1 = pokemon.iloc[0]['Type1']
    type2 = pokemon.iloc[0]['Type2'] if pd.notna(pokemon.iloc[0]['Type2']) else None
    form = pokemon.iloc[0]['Form'] if pd.notna(pokemon.iloc[0]['Form']) and pokemon.iloc[0]['Form'] != '' else None

    # Compute combined effectiveness for dual types
    if type2 is None or type2 == " ":
        combined_eff = df[type1]  # If the Pokémon has only one type
    else:
        combined_eff = df[type1] * df[type2]  # If the Pokémon has two types

    # Get unique weaknesses, resistances, and immunities
    weaknessesquad = sorted(set(combined_eff[combined_eff == 4].index.tolist()))  # Weaknesses (4×)
    weaknesses = sorted(set(combined_eff[combined_eff == 2].index.tolist()))  # Weaknesses (2×)
    resistances = sorted(set(combined_eff[combined_eff == 0.5].index.tolist()))  # Resistances (0.5×)
    resistancesquad = sorted(set(combined_eff[combined_eff == 0.25].index.tolist()))  # Resistances (0.25×)
    immunities = sorted(set(combined_eff[combined_eff == 0].index.tolist()))  # Immunities (0×)

    defenses2 = len(resistances) + len(resistancesquad) + len(immunities)
    totalbody2 = defenses2 + len(weaknesses) + len(weaknessesquad)

    defensivescore2 = (defenses2 / totalbody2) * 100 if totalbody2 > 0 else 0

    defenses1 = len(resistances) + len(immunities)
    totalbody1 = defenses1 + len(weaknesses)

    defensivescore1 = (defenses1 / totalbody1) * 100 if totalbody2 > 0 else 0

    region = None

    if gen == 1:
      region = "Kanto"
    elif gen == 2:
      region = "Johto"
    elif gen == 3:
      region = "Hoenn"
    elif gen == 4:
      region = "Sinnoh"
    elif gen == 5:
      region = "Unova"
    elif gen == 6:
      region = "Kalos"
    elif gen == 7:
      region = "Alola"
    elif gen == 8:
      region = "Galar"
    elif gen == 9:
      region = "Paldea"

    display_name = f"{pokemon_name} ({form})" if form else pokemon_name

    if type2 == " ":
      if type1 == "Ice" or type1 == "Electric":
        print(f"{display_name}, which is an {type1}-type Pokémon from the {region} region (Generation {gen}), has:")
        print(f"- {len(weaknesses)} weaknesses (2x damage from): {', '.join(weaknesses) if weaknesses else 'None'}")
        print(f"- {len(resistances)} resistances (0.5x damage from): {', '.join(resistances) if resistances else 'None'}")
        print(f"- {len(immunities)} immunities (zero effect from): {', '.join(immunities) if immunities else 'None'}")
        print(f"Defensive Score: {round(defensivescore1, 2)}%")
      else:
        print(f"{display_name}, which is a {type1}-type Pokémon from the {region} region (Generation {gen}), has:")
        print(f"- {len(weaknesses)} weaknesses (2x damage from): {', '.join(weaknesses) if weaknesses else 'None'}")
        print(f"- {len(resistances)} resistances (0.5x damage from): {', '.join(resistances) if resistances else 'None'}")
        print(f"- {len(immunities)} immunities (zero effect from): {', '.join(immunities) if immunities else 'None'}")
        print(f"Defensive Score: {round(defensivescore1, 2)}%")
    else:
        print(f"{display_name}, which is a dual-type {type1}/{type2} Pokémon from the {region} region (Generation {gen}), has:")
        print(f"- {len(weaknessesquad)} quad-weaknesses (4x damage from): {', '.join(weaknessesquad) if weaknessesquad else 'None'}")
        print(f"- {len(weaknesses)} weaknesses (2x damage from): {', '.join(weaknesses) if weaknesses else 'None'}")
        print(f"- {len(resistances)} resistances (0.5x damage from): {', '.join(resistances) if resistances else 'None'}")
        print(f"- {len(resistancesquad)} quad-resistances (0.25x damage from): {', '.join(resistancesquad) if resistancesquad else 'None'}")
        print(f"- {len(immunities)} immunities (zero effect from): {', '.join(immunities) if immunities else 'None'}")
        print(f"Defensive Score: {round(defensivescore2, 2)}%")


# Example Usage
pokemon_name = input("Enter Pokémon name: ")
form_name = input("Enter form (leave blank if none): ")
result = get_pokemon_weaknesses(pokemon_name, form_name if form_name else None)
print(result)
