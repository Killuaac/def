def season(year):
    if year == 1 or year == 2 or year == 12:
        return ("Зима")
    elif year >= 3 or year <= 5:
        return ("Осень")
    elif year >= 6 or year <= 8:
        return ("Лето")
    elif year >= 9 or year <= 11:
        return ("Весна")
print(season(int(input())))
