# Pokémon Type Effectiveness Calculator

A Python-based terminal utility that calculates type effectiveness between Pokémon types, supporting offensive and defensive interactions. This project is designed to help users understand the complex relationships between the 18 Pokémon types, including dual-type calculations and form-specific support.

## 🔍 Features

- Calculates type effectiveness using a standard type chart  
- Supports both attacking and defending scenarios  
- Handles dual-type combinations  
- Simple command-line interface (CLI)  
- Easy-to-read pandas DataFrame output  
- Built-in support for adding forms (e.g., regional forms) [WIP]

## 📁 File Structure

```
pkmnTypeCalc.py     # Main script for calculating type effectiveness  
Pokemon.csv           # (Expected) CSV file to load Pokémon type and form data (optional extension)  
README.md           # Project documentation  
```

## 🧠 How It Works

The program uses a dictionary-based matrix where:  
- Keys = Attacking type names  
- Values = List of effectiveness multipliers against 18 defending types (in order)  

These values follow standard Pokémon game mechanics (e.g., Fire is 2× against Grass, 0.5× against Water, etc.).

Sample output shows effectiveness multipliers like:  
```
Against Flying: 0.5×  
Against Steel: 2.0×  
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/goatnaidu06/pokemon-type-calculator.git  
cd pokemon-type-calculator  
```

### 2. Install Dependencies

This project requires `pandas`:

```bash
pip install pandas  
```

### 3. Run the Program

```bash
python3 pkmnTypeCalc.py  
```

Follow the prompts to enter:  
- Attack type  
- One or two defense types (e.g., Water, Flying)  

## 📝 Example Usage

```
Enter attack type: Electric  
Enter defense type 1: Flying  
Enter defense type 2 (or press enter if none): Water  

Type effectiveness:  
Electric vs Flying: 2.0×  
Electric vs Water: 2.0×  
Total effectiveness: 4.0×  
```

## 🎯 Future Improvements

- Add support for Pokémon forms (e.g., Alolan, Galarian)  
- GUI interface (Tkinter or web)  
- Pokémon name-based type lookup  
- Unit tests and test coverage  

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

## 👨‍💻 Author

**Neil Naidu**  
[GitHub Profile](https://github.com/goatnaidu06)
