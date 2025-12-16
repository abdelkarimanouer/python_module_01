class Plant:
    def __init__(self, name, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.days} days old"


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    old_height = p1.height
    print("=== Day 1 ===")
    print(p1.get_info())
    for i in range(6):
        p1.grow()
        p1.age()
    print("=== Day 7 ===")
    print(p1.get_info())
    growth = p1.height - old_height
    print(f"Growth this week: +{growth}cm")
