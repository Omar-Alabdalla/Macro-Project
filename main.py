age = 0
gender = 0
height = 0
weight = 0

print("Welcome to the Macro Calculator!")
print("Please enter the following information:")
age = int(input("Age (in years): "))
gender  = int(input("Gender (0 for male, 1 for female): "))
height = float(input("Height (in cm): "))
weight = float(input("Weight (in kg): "))

def MacroCalculation(age, gender, height, weight):
    if gender == 0:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    protein = weight * 2.2
    fats = (bmr * 0.25) / 9
    carbs = (bmr - (protein * 4) - (fats * 9)) / 4
    return bmr, protein, fats, carbs

print("\nCalculating your daily macronutrient needs...\n")
bmr, protein, fats, carbs = MacroCalculation(age, gender, height, weight)
print(f"Basal Metabolic Rate (BMR): {bmr:.2f} calories/day")
print(f"Protein: {protein:.2f} grams/day") 
print(f"Fats: {fats:.2f} grams/day")
print(f"Carbohydrates: {carbs:.2f} grams/day")