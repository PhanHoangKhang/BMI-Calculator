from BMI import BMI

class CheckResult:
    def __init__(self, gender, bmi, weight, height):
        self.gender = gender
        self.bmi = bmi
        self.weight = weight
        self.height = height

    def getGender(self):
        return self.gender

    def check_result(self):
        if self.gender == "male":
            if self.bmi < 18.2:
                exact = 18.2 * (self.height * self.height)
                needed = exact - self.weight
                print(f"Need to gain {float(needed)} kg to be balanced")
            elif self.bmi > 25.6:
                exact = 25.6 * (self.height * self.height)
                needed = self.weight - exact
                print(f"Need to lose {float(needed)} kg to be balanced")
            else:
                print("Balanced!")
        elif self.gender == "female":
            if self.bmi < 17.5:
                exact = 17.5 * (self.height * self.height)
                needed = exact - self.weight
                print(f"Need to gain {float(needed)} kg to be balanced")
            elif self.bmi > 25.7:
                exact = 25.7 * (self.height * self.height)
                needed = self.weight - exact
                print(f"Need to lose {float(needed)} kg to be balanced")
            else:
                print("Balanced!")
