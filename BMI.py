class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = weight / (height * height)

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getBMI(self):
        return self.bmi
