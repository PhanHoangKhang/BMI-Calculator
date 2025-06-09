from BMI import BMI
from CheckResult import CheckResult

heights = []
weights = []
BMIs = []
genders = []
num_input = 0

print("\n-------------Welcome to BMI Calculator---------------")
while True:
    print("Choose an option 1, 2, 3 or 4:")
    print("1. Enter new user's height and weight")
    print("2. Show all users' BMI")
    print("3. Exit the calculation")
    print()
    while True:
        try:
            option = int(input("Enter your option: ").strip())
            if option in [1, 2, 3]:
                break   
        except ValueError:
            print("Invalid option. Please enter 1, 2 or 3.")
    match option:
        case 1:
            try:
                height = float(input("Enter height in meters: ").strip())
                weight = float(input("Enter weight in kg: ").strip())
                gender = input("Enter gender male or female: ").strip().lower()
                while gender != "male" and gender !="female":
                    gender = input("The gender must be male or female. Enter gender again: ").strip().lower()
                heights.append(height)
                weights.append(weight)
                genders.append(gender)
                print()
                print(f"User {num_input + 1} recorded: {heights[num_input]} {weights[num_input]} {genders[num_input]}")
                num_input += 1
                print()
            except ValueError:
                print("Height and weight must be numeric values.")
        case 2:
            print("\n--------------BMI CALCULATION RESULT--------------") 
            for i in range(num_input):
                user = BMI(heights[i], weights[i])
                user_gender = CheckResult(genders[i], user.getBMI(), weights[i], heights[i])
                BMIs.append(user.getBMI())
                genders.append(user_gender.getGender())
                print(f"User {i + 1}:")
                print(f"  Height: {heights[i]} m")
                print(f"  weight: {weights[i]} kg")
                print(f"  BMI: {BMIs[i]:.2f} kg/m2")
                print(f"  Gender: {genders[i]}")
                user_gender.check_result()
                print("-------------------------")
        case 3:
            print("**************************************************")
            print("Thank you for using our BMI calculator. Hope to see you again!")
            break


