class Zoo:
    zoon = "Зоопарк"
    animals = 0

    def __init__(self, name, animal, rann=False, hunt=False, c_fly=False, c_jump=False):
        self.name = name
        Zoo.animals += 1
        self.animal = animal
        self.rann = rann
        self.hunt = hunt
        self.c_fly = c_fly
        self.c_jump = c_jump


    def ran(self):
        if self.rann:
            print(f"{self.name} ran!")
        else:
            print(f"{self.name} can't run!")

    def can_hunt(self):
        if self.hunt:
            print(f"{self.name} hunt!")
        else:
            print(f"{self.name} doesn't hunt!")

    def fly(self):
        if self.c_fly:
            print(f"{self.name} fly!")
        else:
            print(f"{self.name} doesn't fly!")

    def jump(self):
        if self.c_jump:
            print(f"{self.name} jump!")
        else:
            print(f"{self.name} doesn't jump!")


monkey = Zoo("Rio", "monkey", rann=True, hunt=True, c_jump=True)
pig = Zoo("Pepa", "pig", rann=True, c_jump=True)
cheetah = Zoo("Kara", "cheetah", rann=True, hunt=True, c_jump=True)
bird = Zoo("Kecha", "bird", hunt=True, c_fly=True, c_jump=True)

print(bird.name, bird.can_hunt(), bird.fly(), bird.jump())
print(monkey.name, monkey.ran(), monkey.jump())
print(pig.name, pig.jump(), pig.ran())
print(cheetah.name, cheetah.ran(), cheetah.can_hunt(), cheetah.jump())

print(f"Zoo: {Zoo.zoon}")
print(f"Animals: {Zoo.animals}")
