"""
#10 Mones, Jacques Vincent Dion C.
9 - Samat
"""

year = int(input("Enter your birth year: "))

print("")

if year >= 1900:
    zodiacs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    def zodiac():
        signs = year - 1900
        sign = zodiacs[signs%12]
        print("Your chinese zodiac sign is:", [sign])
    zodiac()

else:
    print("Invalid, pick a year younger than 1900")
