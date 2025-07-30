# Pokémon Weakness Calculator

A Python-based terminal utility that calculates **weaknesses, resistances, and immunities** for a particular Pokémon, including support for alternate forms like Mega Evolutions, Alolan forms, etc. This tool is designed to help users understand the defensive matchups of any Pokémon based on its typing.

## 🔍 Features

- Calculates type effectiveness for a specific Pokémon
- Supports dual-type combinations
- Accepts alternate forms (optional or required for some Pokémon)
- Displays weaknesses, resistances, quad-weaknesses, immunities, and a defensive score
- Clean and simple command-line interface (CLI)
- Uses `pandas` for formatted table output

## 📁 File Structure

```
pkmnWeaknessCalc.py     # Main script for calculating type weaknesses  
Pokemon.csv         # CSV dataset containing Pokémon names, types, and form data  
README.md           # Project documentation
LICENSE.txt           # Project license 
```

## 🧠 How It Works

The script loads type data from a dictionary matrix and looks up Pokémon type combinations from the `Pokemon.csv` file. It then calculates how that Pokémon fares defensively against each of the 18 attack types.

Type effectiveness follows official Pokémon game logic:

- 2x = Weakness  
- 0.5x = Resistance  
- 0.25x = Quad-resistance  
- 4x = Quad-weakness  
- 0x = Immunity  

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/goatnaidu06/pokemon-weakness-calculator.git  
cd pokemon-weakness-calculator  
```

### 2. Install Dependencies

```bash
pip install pandas  
```

### 3. Run the Program

```bash
python3 pkmnWeaknessCalc.py  
```

Follow the prompts to enter:
- **Pokémon name**
- **Form** (optional — e.g., Mega Blastoise, Galarian Meowth, Hisuian Arcanine, etc.)

## 📝 Example Usage

```
Enter Pokémon name: Charizard  
Enter form (leave blank if none): Mega Charizard X  

Charizard (Mega Charizard X), which is a dual-type Fire/Dragon Pokémon from the Kalos region (Generation 6), has:
- 0 quad-weaknesses (4x damage from): None  
- 3 weaknesses (2x damage from): Dragon, Ground, Rock  
- 3 resistances (0.5x damage from): Bug, Electric, Steel  
- 2 quad-resistances (0.25x damage from): Fire, Grass  
- 0 immunities (zero effect from): None  
Defensive Score: 62.5%
```

## 🎯 Future Improvements

- Expand support for all regional forms
- Add offensive calculator mode
- Pokédex-style formatting with generation and region filters
- GUI or web interface using Streamlit or Flask

## 📜 License

MIT License. See [LICENSE](LICENSE.txt) for details.

## 👨‍💻 Author

**Neil Naidu**  
[GitHub Profile](https://github.com/goatnaidu06)
