from time import sleep


def vstup_float(txt: str) -> float:
    bu: str = " "
    while True:
        try:
            bu = input(txt)
            da: float = float(bu.replace(",", ".").strip())
            # print(da)
            if da == int(da):
                print("\033[91mZadejte desetinné číslo!\033[0m", end="\r")
                sleep(1)
                print("                            ", end="\r")
                continue
            else:
                return da
        except:
            if bu != "":
                if bu[0] == "q":
                    exit()
                print("Zadejte číslo nebo q pro ukončení.")
                continue
            print("\033[91mZadejte číslo!\033[0m", end="\r")
            sleep(0.5)


def main() -> None:
    while True:
        flt: float = vstup_float("Zadejte číslo: ")

        flt_split: list[str] = str(flt).split(".")
        num: int = int("".join(flt_split))
        den: int = 10 ** len(flt_split[1])

        while True:
            if num % 2 == 0:
                if den % 2 == 0:
                    num //= 2
                    den //= 2
            else:
                break
        while True:
            if num % 5 == 0:
                if den % 5 == 0:
                    num //= 5
                    den //= 5
            else:
                break

        print(f"{num/den} = {num}/{den}")


if __name__ == "__main__":
    main()
