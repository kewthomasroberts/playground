import random

class DiceSimulator:
    def __init__(self, num_dice=1, num_sides=6):
        self.num_dice = num_dice
        self.num_sides = num_sides

    def roll_dice(self):
        rolls = [random.randint(1, self.num_sides) for _ in range(self.num_dice)]
        return rolls

# Пример использования класса
dice_simulator = DiceSimulator(num_dice=3, num_sides=6)
result = dice_simulator.roll_dice()
print(f"Результат броска {dice_simulator.num_dice} кубика(-ов) с {dice_simulator.num_sides} гранями:", result)
