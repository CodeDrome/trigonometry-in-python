import math


def main():

    print("--------------------------")
    print("| codedrome.com          |")
    print("| Trigonometry in Python |")
    print("--------------------------\n")

    hypotenuse = 0
    adjacent = 0
    opposite = 0
    anglerad = 0

    anglerad = 0.523598775
    opposite = 5
    print(f"angle = {math.degrees(anglerad)}°")
    print(f"opposite = {opposite}")
    hypotenuse = opposite / math.sin(anglerad)
    adjacent = opposite / math.tan(anglerad)
    print(f"hypotenuse = {opposite}/math.sin({math.degrees(anglerad)}) = {hypotenuse}");
    print(f"adjacent = {opposite}/math.tan({math.degrees(anglerad)}) = {adjacent}");

    print()

    anglerad = 0.523598775
    adjacent = 8.66
    print(f"angle = {math.degrees(anglerad)}°")
    print(f"adjacent = {adjacent}")
    hypotenuse = adjacent / math.cos(anglerad)
    opposite = adjacent * math.tan(anglerad)
    print(f"hypotenuse = {adjacent}/cos({math.degrees(anglerad)}) = {hypotenuse}")
    print(f"opposite = {adjacent}*tan({math.degrees(anglerad)}) = {opposite}")

    print()

    anglerad = 0.523598775
    hypotenuse = 10
    print(f"angle = {math.degrees(anglerad)}°")
    print(f"hypotenuse = {hypotenuse}")
    opposite = hypotenuse * math.sin(anglerad)
    adjacent = hypotenuse * math.cos(anglerad)
    print(f"opposite = {hypotenuse}*sin({math.degrees(anglerad)}) = {opposite}")
    print(f"adjacent = {hypotenuse}*cos({math.degrees(anglerad)}) = {adjacent}")

    print()

    opposite = 5
    hypotenuse = 10
    print(f"opposite = {opposite}")
    print(f"hypotenuse = {hypotenuse}")
    anglerad = math.asin(opposite/hypotenuse)
    print(f"angle = asin({opposite}/{hypotenuse}) = {math.degrees(anglerad)}°")

    print()

    adjacent = 8.66
    hypotenuse = 10
    print(f"adjacent = {adjacent}")
    print(f"hypotenuse = {hypotenuse}")
    anglerad = math.acos(adjacent/hypotenuse)
    print(f"angle = acos({adjacent}/{hypotenuse}) = {math.degrees(anglerad)}°")

    print()

    opposite = 5
    adjacent = 8.66
    print(f"opposite = {opposite}")
    print(f"adjacent = {adjacent}")
    anglerad = math.atan(opposite/adjacent)
    print(f"angle = atan({opposite}/{adjacent}) = {math.degrees(anglerad)}°")


main()
