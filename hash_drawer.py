import math


SYMBOL = " # "
SPACE = "   "


def draw(width_fc, start=0, stop=20, filled=True, max_width=50):
    for x in range(start, stop):
        y = min(max_width, max(0, math.floor(width_fc(x))))
        if filled:
            center = SYMBOL * y
        else:
            if y == 0:
                center = ""
            else:
                center = SYMBOL + SPACE * max(0, (y - 2)) + SYMBOL
        msg = SPACE * ((max_width - y) // 2) + center + SPACE * ((max_width - y) // 2 - ((max_width - y) % 2))
        print(msg)


def main():
    radius = 15

    # filled circle
    draw(lambda x: math.sqrt(max(0, radius**2 - x**2))*2, start=-radius, stop=radius, filled=True, max_width=radius*2)
    print(end="\n"*5)

    # empty circle
    draw(lambda x: math.sqrt(max(0, radius**2 - x**2))*2, start=-radius, stop=radius, filled=False, max_width=radius*2)
    print(end="\n"*5)

    # filled square:
    draw(lambda x: radius*2, stop=radius*2, max_width=radius*2)
    print(end="\n"*5)


if __name__ == "__main__":
    main()
