# Jackson J.
# 11/11/19
# This is a class creation of a car


class Cars:
    def __init__(self, make, model, color, year, engine, mileage, doors, price, distance):
        self.make = make
        self.model = model
        self.color = color
        self.year = int(year)
        self.engine = engine
        self.mileage = int(mileage)
        self.doors = int(doors)
        self.price = int(price)
        self.distance_traveled = int(distance)

    def car_des(self):
        print(f"Wow that's interesting! I've never heard of a car like that.")
        print(f"A {self.make}, model {self.model}, and you've got it in {self.color}?!")
        print(f"You said it was made in {self.year}, right? That explains that {self.engine} engine and the {self.doors} door option.")
        print(f"And with that engine, looks like your gas mileage is sitting at {self.mileage}.")
        print(f"How much did you have to pay for that? Looks like it comes up to about ${self.price}.")

    def change_color(self):
        print("What color would you want to change your car to if you had the opportunity?")
        nc = input(">>>")
        self.color = nc
        print(f"Okay, so you'd have a {self.color} {self.make}. How about you buy me a car like that.")
        buy = input(">>>").title()
        if buy == "Yes" or buy == "Y":
            print("Really??? Wow, that's awesome...")
            print("You may have to program a car for me though. Since...")

        elif buy == "No" or buy == "N":
            print("I figured you say that.")

        else:
            print("I'm going to assume that is a no")

    def meter(self):
        print("What is your odometer at?")
        odometer = input(">>>")
        self.distance = odometer
        print(f"You've traveled far! {self.distance} miles is far")
