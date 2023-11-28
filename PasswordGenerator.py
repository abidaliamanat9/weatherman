import random as rnd

class PasswordGenerator:
    def __init__(self):
        self.simple = "abcdefghijklmnopqrstuvwxyz123456789"
        self.capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.symbols = "!@#$%^&*(){}[]/\:;.,"
        self.length = rnd.randint(5, 9)

    def set_password_length(self):
        islength = input("Do you want to specify the length of the password? Enter 'y' or 'n': ")
        if islength.lower() == 'y':
            self.length = int(input("Enter your desired password length: "))

    def add_special_symbols(self):
        isspecial = input("Do you want to add special symbols to your password? Enter 'y' or 'n': ")
        if isspecial.lower() == 'y':
            self.simple += self.symbols + self.capitals

    def generate_password(self):
        self.set_password_length()
        self.add_special_symbols()
        password = "".join(rnd.sample(self.simple, self.length))
        print("Generated Password:", password)

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    password_generator.generate_password()

