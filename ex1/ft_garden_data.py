class ClsPlant:
    def __init__(self, name, height: int, age: int) -> None:
        print(f"{name}: {height}cm, {age} days old")


print("=== Garden Plant Registry ===")
plant1 = ClsPlant("Rose", 25, 30)
plant2 = ClsPlant("Sunflower", 80, 45)
plant3 = ClsPlant("Cactus", 15, 120)
