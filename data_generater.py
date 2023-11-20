import pandas as pd

# Data from the images provided, structured for CSV format
data = [
    ["Actara", "thiamethoxam", "NYS, LI", "100-938",
        "4A", 3.5, 12, 5, "Excellent", "Excellent"],
    ["Drexel Carbaryl 4L", "carbaryl", "NR", "19713-49",
        "1A", 2, 48, 7, "Excellent", "Excellent"],
    ["Imidan 70WP", "phosmet", "NYS", "10163-169",
        "1B", 1.333, 336, 7, "Excellent", "Poor"],
    ["Dupont Avant", "indoxacarb", "NR", "352-597",
        "22A", 6, 12, 7, "Excellent", "Poor"],
    ["Brigade WSB", "bifenthrin", "F", "279-3108",
        "3A", 8, 12, 30, "Excellent", "Excellent"],
    ["Brigade WSB (researcher 2(ee))", "bifenthrin", "F",
     "279-3108", "3A", 10, 12, 30, "Excellent", "Excellent"],
    ["Brigade 2EC", "bifenthrin", "F", "279-3313",
        "3A", 6.4, 12, 30, "Excellent", "Excellent"],
    ["Hero", "zeta-cypermethrin & bifenthrin", "F",
        "279-3315", "3A", 5, 12, 30, "Excellent", "Excellent"],
    ["Mustang MAXX", "zeta-cypermethrin", "F",
        "279-3426", "3A", 4, 12, 1, "Excellent", "Good"],
    ["Sniper Helios", "bifenthrin", "F", "34704-858",
        "3A", 3.2, 12, 30, "Excellent", "Excellent"],
    ["Danitol 2.4 EC", "fenpropathrin", "F", "59639-35",
        "3A", 16, 24, 21, "Excellent", "Excellent"],
    ["Pryonil Crop Spray", "Pyrethrin+PPO", "NYS",
        "89459-26", "3A", 12, 12, 0, "Good", "Good"],
    ["Swagger", "bifenthrin & imidacloprid", "F", "34704-1045",
        "3A, 4A", 7.6, 12, 30, "Good to Excellent", "Good to Excellent"],
    ["BotaniGard MAXX", "Beauveria bassiana (strain GHA) + pyrethrins", "NR",
     "82074-5-68539", "UN, 3A", 8, 12, "Until spray has dried", "Good", "Good"],
    ["Xpectro OD", "Beauveria bassiana (strain GHA) + pyrethrins", "NR",
     "82074-5", "UN, 3A", 8, 12, "Until spray has dried", "Good", "Good"],
    ["Aza-Direct", "azadirachtin", "NR",
        "71908-1-10163", "UN", 1, 4, 0, "Good", "Good"],
    ["M-Pede", "potassium salts of fatty acids (insecticidal soap)",
     "NR", "10163-324", "UN", 1, 12, 0, "Good", "Good"],
    ["Mycotrol ESO", "Beauveria bassiana", "NR", "82074-1",
        "UN", 0.25, 4, "Up to day of harvest", "Good", "Good"],
    ["BoteGHA ES", "Beauveria bassiana (strain GHA)", "NR", "82074-1",
     "UN", 0.25, 4, "Up to day of harvest", "Good", "Good"],
    ["BotaniGard ES", "Beauveria bassiana (strain GHA)", "NR", "82074-1-68539",
     "UN", 0.25, 4, "Up to day of harvest", "Good", "Good"]
]

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    "Product", "Active Ingredient", "Use Restrictions", "EPA Reg No.", "IRAC Group", "Rate/A", "REI (hours)", "PHI (days)", "Effect on Adults", "Effect on Nymphs"])

# Continuation of the code to write the DataFrame to a CSV file
csv_file_path = 'pesticides.csv'
# Saving the dataframe to a CSV file without the index
df.to_csv(csv_file_path, index=False)
