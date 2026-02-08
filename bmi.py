gender_input = "none"
gender = "none"
string_to_add = "none"
counter = 0
exercise = False
 
while counter <= 3 and counter >= 0:
    gender_input = str(input("input your gender: "))
    weight_kg = int(input("input your current weight in kg: "))
    height_cm = int(input("input your current height in cm: "))
    age_years = int(input("input how old are you: "))
    if (weight_kg >= 30 and weight_kg <= 250) and (height_cm >= 120 and height_cm <= 210) and (age_years >= 14 and age_years <= 100) and (gender_input == "male" or gender_input == "female"):
        counter = 4
        gender = gender_input
    else:
        print("Incorrect, try again. ")
        print("make sure your inputs meet the given criteria: ")
        print("Weight range: 30 to 250 kg.", "Your Input: ", weight_kg)
        print("Height range: 120 to 210 cm", "Your Input: ", height_cm)
        print("Age range: 14 to 100 years of age.", "Your Input: ", age_years)
        print("Genders: male, female", "Your Input: ", gender_input)
    if counter == 4:
        male_bmr = [f"{88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age_years) :.2f}"]
        female_bmr = [f"{447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age_years) :.2f}"]
        bmr_calculation = {
            "male" : male_bmr,
            "female" : female_bmr
        }
        # bmr part
        bmr = bmr_calculation[gender_input][-1]
        # bmi part
        meters = height_cm / 100
        bmi = f"{weight_kg / (meters * meters):.1f}"
        bmi_int = float(bmi)

        if bmi_int < 18.5:
            string_to_add = "Underweight"
        elif bmi_int >= 18.5 and bmi_int <= 24.9:
            string_to_add = "Normal Weight"
        elif bmi_int >= 25 and bmi_int <= 29.9:
            string_to_add = "Overweight"
        elif bmi_int >= 30:
            string_to_add = "Obesity"

        print("Your current BMR: ", bmr)
        print("Your current BMI: ", str(bmi), "" + string_to_add)
        print("Your target BMI: ", "Normal Weight")

        bmr_type = float(bmr)
        calory_calc = {
            1 : bmr_type * 1.2,
            2 : bmr_type * 1.375,
            3 : bmr_type * 1.55,
            4 : bmr_type * 1.725,
            5 : bmr_type * 1.9
        }
        print("\n 1. Little to no exercise \n 2. Light exercise (1–3 days per week) \n 3. Moderate exercise (3–5 days per week) \n 4. Heavy exercise (6–7 days per week) \n 5. Very heavy exercise (twice per day, extra heavy workouts)")
        
        while exercise == False:
            level_of_exercise = int(input("what is your level of exercise (input a number from 1-5): "))
            if level_of_exercise >= 1 and level_of_exercise <= 5:
                exercise = True
            else:
                print("You can only input numbers from 1 to 5, your input: ", level_of_exercise)
            for key, value in calory_calc.items():
                if level_of_exercise == key:
                    print("Your recommended daily kilocalorie intake to maintain weight: ", round(value))