import time


def vstup_float(txt):
    while True:
        try:
            return float(input(txt))
        except ValueError:
            print("Zadejte prosím číslo!")


# načti strany trojúhelníku a zjisti, zda lze sestrojit a jaký je typ
def main():
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    except:
        print("\033[91m Neplatný vstup\033[0m", end="\r")
        time.sleep(1)
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Trojúhelník nelze sestrojit.")
    else:
        te = "Trojúhelník lze sestrojit"
        if (
            a ** 2 + b ** 2 == c ** 2
            or a ** 2 + c ** 2 == b ** 2
            or b ** 2 + c ** 2 == a ** 2
        ):
            te += " a je pravoúhlý"
        elif a == b == c:
            te += " a je rovnostranný"
        elif a == b or a == c or b == c:
            te += " a je rovnoramenný"
        else:
            te += " a je obecný"
        te += "."
        print(te)


if __name__ == "__main__":
    while True:
        main()
