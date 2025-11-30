#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:24:48 2025

@author: NeilN
"""

import pandas as pd
import customtkinter as ctk

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
df_g1 = pd.DataFrame(pokemon_g1, index=pokemon_g1.keys()).T
df_g25 = pd.DataFrame(pokemon_g25, index=pokemon_g25.keys()).T

data_url = 'https://raw.githubusercontent.com/goatnaidu06/pokemon-weakness-calculator/refs/heads/main/Pokemon.csv'
poke_df = pd.read_csv(data_url)
poke_df.columns = poke_df.columns.str.strip()
poke_df['Form'] = poke_df['Form'].fillna('').str.strip()



# Load the provided Pokémon data

# Ensure column names are correctly formatted
poke_df.columns = poke_df.columns.str.strip()

# Extract relevant columns


# Type effectiveness chart (Offense types as rows, Defense types as columns)
def get_pokemon_weaknesses(pokemon_name, form_name=None, gen_filter=None):
    # --- Look up the Pokémon row (with/without form) ---
    base = poke_df[poke_df['Name'].str.lower() == pokemon_name.lower()]

    if form_name:
        pokemon = base[base['Form'].str.lower() == form_name.lower()]
    else:
        # Default to “no form” entry
        pokemon = base[base['Form'] == '']

    if pokemon.empty:
        return {"ok": False, "error":"Error: Pokémon not found."}

    # Basic info from CSV
    gen = int(pokemon.iloc[0]['Generation'])
    type1 = pokemon.iloc[0]['Type1']
    type2 = pokemon.iloc[0]['Type2'] if pd.notna(pokemon.iloc[0]['Type2']) else None
    form = pokemon.iloc[0]['Form'] if pd.notna(pokemon.iloc[0]['Form']) and pokemon.iloc[0]['Form'] != '' else None

    # Normalize blank/space second type
    if isinstance(type2, str) and type2.strip() == '':
        type2 = None

    display_name = f"{pokemon_name} ({form})" if form else pokemon_name

    # --- Generation filter handling ---
    # gen_filter: which game's type chart / era you want to use
    #   - 1       → use Gen 1 chart (df_g1)
    #   - 2–5     → use Gen 2–5 chart (df_g25)
    #   - 6–9     → use modern chart (df)
    #   - If the Pokémon's own generation > gen_filter → invalid input
    if gen_filter is None:
        # default: use the Pokémon's own generation for chart selection
        gen_filter = gen
    else:
        try:
            gen_filter = int(gen_filter)
        except ValueError:
            return {"ok": False, "error": "Error: Generation filter must be an integer between 1 and 9."}

        if gen_filter < 1 or gen_filter > 9:
            return {"ok": False, "error":"Error: Generation filter must be between 1 and 9."}

        # If the Pokémon wasn't introduced yet in that generation → invalid
        if gen > gen_filter:
            return {"ok": False, "error": (f"Error: {display_name} is from Generation {gen}, "
                    f"so it does not exist in Generation {gen_filter}.")}

    # --- Choose which type chart to use ---
    if gen_filter == 1:
        chart = df_g1          # no Dark/Steel; weird Gen 1 Ghost/Psychic
    elif 2 <= gen_filter <= 5:
        chart = df_g25         # Dark/Steel exist, no Fairy, old Steel resists
    else:  # 6–9
        chart = df             # modern chart with Fairy and updated Steel

    # --- Adjust typings for pre-Gen 6 (no Fairy) ---
    # Rule you gave:
    #   - If 1st type is Fairy → change to Normal
    #   - Else if 2nd type is Fairy → remove it
    if gen_filter <= 5:
        if type1 == "Fairy":
            type1 = "Normal"
        if type2 == "Fairy":
            type2 = None

    # --- Safety: make sure resulting types exist in this chart ---
    for t in [type1, type2]:
        if t is not None and t not in chart.columns:
            return {"ok": False, "error": (f"Error: Type '{t}' does not exist in the Generation {gen_filter} "
                    f"type chart (after pre-Gen 6 conversion).")}

    # --- Compute combined effectiveness using the chosen chart ---
    if type2 is None or type2 == " ":
        combined_eff = chart[type1]  # single-type Pokémon
    else:
        combined_eff = chart[type1] * chart[type2]  # dual-type Pokémon

    # Get unique weaknesses, resistances, and immunities
    weaknessesquad = sorted(set(combined_eff[combined_eff == 4].index.tolist()))      # 4×
    weaknesses = sorted(set(combined_eff[combined_eff == 2].index.tolist()))          # 2×
    resistances = sorted(set(combined_eff[combined_eff == 0.5].index.tolist()))       # 0.5×
    resistancesquad = sorted(set(combined_eff[combined_eff == 0.25].index.tolist()))  # 0.25×
    immunities = sorted(set(combined_eff[combined_eff == 0].index.tolist()))          # 0×

    defenses2 = len(resistances) + len(resistancesquad) + len(immunities)
    totalbody2 = defenses2 + len(weaknesses) + len(weaknessesquad)
    defensivescore2 = (defenses2 / totalbody2) * 100 if totalbody2 > 0 else 0

    defenses1 = len(resistances) + len(immunities)
    totalbody1 = defenses1 + len(weaknesses)
    defensivescore1 = (defenses1 / totalbody1) * 100 if totalbody1 > 0 else 0

    # Region text (based on original generation, not filter)
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
    else:
        region = "Unknown"
    
    #return output for our text helper function to format the results for the UI
    return {
        "ok": True,
        "pokemon_name": pokemon_name,
        "form": form,
        "display_name": display_name,
        "region": region,
        "gen": gen,
        "type1": type1,
        "type2": type2,
        "weaknessesquad": weaknessesquad,
        "weaknesses": weaknesses,
        "resistances": resistances,
        "resistancesquad": resistancesquad,
        "immunities": immunities,
        "defensive_score_single": round(defensivescore1, 2),
        "defensive_score_dual": round(defensivescore2, 2),
        "used_chart_gen": gen_filter,
    }

# Text formatter that turns original printed text that can be called by the customtkinter UI
def format_result_text(result: dict) -> str:
    if not result.get("ok", False):
        return result.get("error", "Unknown error")\
    
    # Creating variables for pokemon weakness results
    name = result["display_name"]
    region = result["region"]
    gen = result["gen"]
    type1 = result["type1"]
    type2 = result["type2"]
    weaknessesquad = result["weaknessesquad"]
    weaknesses = result["weaknesses"]
    resistances = result["resistances"]
    resistancesquad = result["resistancesquad"]
    immunities = result["immunities"]
    defensivescore1 = result["defensive_score_single"]
    defensivescore2 = result["defensive_score_dual"]
    
    # How we store our text formatting
    lines = []
    
    # Single types:
    if type2 is None or type2 == " ":
        # Determining whether to use a or an depending on the type
        article = "an" if type1 in ("Ice", "Electric") else "a"
        
        lines.append(f"{name}, which is {article} {type1}-type Pokémon from {region} (Generation {gen}), has:")
        lines.append(f"- Weaknesses: {', '.join(weaknesses) if weaknesses else 'None'}")
        lines.append(f"- Resistances: {', '.join(resistances) if resistances else 'None'}")
        lines.append(f"- Immunities: {', '.join(immunities) if immunities else 'None'}")
        lines.append(f"- Defensive Score: {round(defensivescore1, 2)}%")
    
    # Dual Types:
    
    else:
        lines.append(f"{name}, which is a dual-type {type1}/{type2} Pokémon from {region} (Generation {gen}), has:")
        lines.append(f"- Quad Weaknesses: {', '.join(weaknessesquad) if weaknessesquad else 'None'}")
        lines.append(f"- Weaknesses: {', '.join(weaknesses) if weaknesses else 'None'}")
        lines.append(f"- Resistances: {', '.join(resistances) if resistances else 'None'}")
        lines.append(f"- Quad Resistances: {', '.join(resistancesquad) if resistancesquad else 'None'}")
        lines.append(f"- Immunities: {', '.join(immunities) if immunities else 'None'}")
        lines.append(f"- Defensive Score: {round(defensivescore2, 2)}%")
    
    return "\n".join(lines)

# Appearance settings
ctk.set_appearance_mode("dark")         # "light" or "dark"
ctk.set_default_color_theme("dark-blue")     # "blue", "green", "dark-blue"
class PokemonWeaknessApp(ctk.CTk):

    def __init__(self):
        # Constructor to create UI
        super().__init__()

        # Creating window title and original size
        self.title("Pokémon Weakness Calculator")
        self.geometry("700x500")

        # Makes sure column and output box adjust with manual window adjustments 
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(3, weight = 1)

        # ---- Title (row 0) ----
        title_label = ctk.CTkLabel(
            self,
            text = "Pokémon Weakness Calculator", # Setting text of label
            font = ctk.CTkFont(family = "Segoe UI", size = 22, weight = "bold") # Setting font
        )
        
        # All widgets are customized through .grid:
        #   1. row / column -> where the widget resides
        #   2. padx / pady -> how much empty space around the widget
        #   3. sticky -> which sides the widget attaches to
        
        title_label.grid(row = 0, column = 0, padx = 20, pady = (20, 10), sticky = "w")

        # ---- Input frame (row 1) ----
        frame = ctk.CTkFrame(self)
        frame.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = "ew")
        frame.grid_columnconfigure(1, weight = 1)

        # Pokémon name
        name_label = ctk.CTkLabel(frame, text = "Pokémon name:")
        name_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")

        self.name_entry = ctk.CTkEntry(frame, placeholder_text = "e.g. Pikachu")
        self.name_entry.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "ew")

        # Form (optional)
        form_label = ctk.CTkLabel(frame, text = "Form (optional):")
        form_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")

        self.form_entry = ctk.CTkEntry(frame, placeholder_text = "blank = no form")
        self.form_entry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "ew")

        # Generation filter
        gen_label = ctk.CTkLabel(frame, text = "Generation filter (1–9):")
        gen_label.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "e")

        self.gen_entry = ctk.CTkEntry(frame, placeholder_text = "blank = Pokémon's first introduced gen")
        self.gen_entry.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "ew")

        # ---- Calculate button (row 2) ----
        calc_button = ctk.CTkButton(
            self,
            text = "Calculate",
            command = self.on_calculate
        )
        calc_button.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = "ew")

        # ---- Output box (row 3) ----
        self.output_box = ctk.CTkTextbox(
            self,
            wrap = "word",
            font = ctk.CTkFont(family="Segoe UI", size = 15)
        )
        

        # Insert output box in the third row
        self.output_box.grid(row = 3, column = 0, padx = 20, pady = (5, 20), sticky = "nsew")

        # Prevents typing inside output box
        self.output_box.configure(state = "disabled")

    def on_calculate(self):
        name = self.name_entry.get().strip()
        form_text = self.form_entry.get().strip()
        gen_text = self.gen_entry.get().strip()

        form = form_text if form_text != "" else None

        # Handle generation input
        gen_filter = None
        if gen_text != "":
            try:
                gen_filter = int(gen_text)
            except ValueError:
                error_result = {"ok": False, "error": "Error: Generation filter must be an integer 1–9."}
                text = format_result_text(error_result)
                self.show_text(text)
                return

        # Calls original logic
        result = get_pokemon_weaknesses(name, form, gen_filter)

        text = format_result_text(result)  # Formats logic into text
        self.show_text(text)               # Displays text in output box

    def show_text(self, text: str):
        """Utility to update the read-only output textbox."""
        self.output_box.configure(state = "normal")   # temporarily editable
        self.output_box.delete("1.0", "end")          # clear previous text
        self.output_box.insert("1.0", text)           # insert new text
        self.output_box.configure(state = "disabled") # lock again


# Loop to run code
if __name__ == "__main__":
    app = PokemonWeaknessApp()
    app.mainloop()