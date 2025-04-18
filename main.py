class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy < 2 or self.hunger > 8:
            print(f"{self.name} is too tired or hungry to play!")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        if self.energy < 2:
            print(f"{self.name} is too tired to learn a new trick!")
            return
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 1)

    def get_status(self):
        mood = self.get_mood()
        return (f"Name: {self.name}\n"
                f"Hunger: {self.hunger}\n"
                f"Energy: {self.energy}\n"
                f"Happiness: {self.happiness}\n"
                f"Mood: {mood}")

    def get_mood(self):
        if self.hunger > 8:
            return "Hungry"
        elif self.energy < 3:
            return "Tired"
        elif self.happiness > 7:
            return "Happy"
        else:
            return "Okay"

    def show_tricks(self):
        return f"{self.name} knows: {', '.join(self.tricks) if self.tricks else 'no tricks yet'}"

# Example usage
pet1 = Pet("Puppy")
print(pet1.get_status())

pet1.eat()
pet1.sleep()
pet1.play()
pet1.train("sit")

print(pet1.get_status())
print(pet1.show_tricks())
