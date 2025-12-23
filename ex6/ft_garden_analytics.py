class Plant:
    """Blueprint for making plant objects"""
    def __init__(self, name: str, height: int) -> None:
        """Setup plant with name, height"""
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, s_height: int, color: str,
                 is_blooming: bool) -> None:
        super().__init__(name, s_height)
        self.color = color
        self.is_blooming = is_blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, s_height: int, color: str,
                 is_blooming: bool, prize_points: int) -> None:
        super().__init__(name, s_height, color, is_blooming)
        self.prize_points = prize_points
