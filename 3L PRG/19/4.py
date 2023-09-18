def vstup_int_list() -> list[int]:
    temp: str = ""
    for znak in input("Zadejte čísla: "):
        if znak in "0123456789":
            temp += znak
        else:
            temp += " "
    return [int(x) for x in temp.split()]


print(sum(vstup_int_list()))
