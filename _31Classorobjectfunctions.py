
class Student:
    def __init__(self):
        name=(input("Enter your name:"))
        major=(input("Enter your major:"))
        gpa=(input("Enter your G.P.A. in decimals upto 1 place:"))
        kts=(input("Enter the number of KT's if any:"))
        drop=(input("Enter your drop status:Type in True or False "))

        self.name = str(name)
        self.major = str(major)
        self.gpa = float(gpa)
        self.kts = int(kts)
        self.drop = bool(drop)

        def drop_test(self,kts):
            if self.kts > 5:
                drop = True
                self.drop = drop
            else:
                drop = False
                self.drop = drop

    def on_honor_roll(self):
        if self.gpa >=3.5 and self.drop== False:
            print("You are on the honor roll.G.P.A--",self.gpa)
        else:
            print("You are not on the honor role")
