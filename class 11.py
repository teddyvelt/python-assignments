class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name +" is sitting")

    def roll_over(self):
        print(self.name +" is rolling over")
    def birthday(self):
        self.age += 1
        print("age is", self.age)



my_dog = dog('willie', 6)
print("name: " + my_dog.name)  
print("age: " + str(my_dog.age))
my_dog.sit()
my_dog.roll_over()

your_dog = dog('lucy', 3)
your_dog.sit()



my_dog.birthday()