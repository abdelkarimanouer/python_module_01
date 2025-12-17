class SecurePlant:
    def __init__(self, name) -> None:
        self.name = name
        self.height: int
        self.age: int
        print(f"Plant created: {self.name}")

    def set_height(self, height) -> None:
        if (height >= 0):
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            self.height = 0
            print(f"Invalid operation attempted: height {self.height}cm "
                  f"[REJECTED]")
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        if (self.height >= 0):
            return (self.height)
        else:
            return 0

    def set_age(self, age) -> None:
        if (age >= 0):
            self.age = age
            print(f"Age updated: {self.age} days [OK]")
        else:
            self.age = 0
            print(f"Invalid operation attempted: age {self.age} days "
                  f"[REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self) -> int:
        if (self.age >= 0):
            return (self.age)
        else:
            return 0


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose")
    p1.set_height(25)
    p1.set_age(30)
    print(f"Current plant: {p1.name} ({p1.get_height()}cm, "
          f"{p1.get_age()} days)")
