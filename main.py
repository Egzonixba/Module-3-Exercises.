# Task 1

SIZE_LIMIT = 42

# Input from the fisherman
fish_length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if fish_length >= SIZE_LIMIT:
    print("Congratulations! You've caught a zander that meets the size limit.")
else:
    difference = SIZE_LIMIT - fish_length
    print(f"The caught zander is {difference:.2f} centimeters below the size limit.")
    print("Please release the fish back into the lake.")

# Task 2
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    description = "upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "above the car deck, equipped with a window."
elif cabin_class == "B":
    description = "windowless cabin above the car deck."
elif cabin_class == "C":
    description = "windowless cabin below the car deck."
else:
    description = "Invalid cabin class."

print("Cabin class", cabin_class, "is a", description)

# Task 3

gender = input("Enter your biological gender (male/female): ")
hemoglobin_value = float(input("Enter your hemoglobin value (g/l): "))

FEMALE_LOW = 117
FEMALE_HIGH = 155
MALE_LOW = 134
MALE_HIGH = 167

if gender == "female":
    if hemoglobin_value < FEMALE_LOW:
        feedback = "low"
    elif hemoglobin_value >= FEMALE_LOW and hemoglobin_value <= FEMALE_HIGH:
        feedback = "normal"
    else:
        feedback = "high"
elif gender == "male":
    if hemoglobin_value < MALE_LOW:
        feedback = "low"
    elif hemoglobin_value >= MALE_LOW and hemoglobin_value <= MALE_HIGH:
        feedback = "normal"
    else:
        feedback = "high"
else:
    feedback = "Invalid gender."

#Output
if feedback != "Invalid gender.":
    print("Your hemoglobin value is", feedback + ".")
else:
    print(feedback)

#Task 4
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
