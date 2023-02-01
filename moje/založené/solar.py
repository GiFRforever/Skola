def vstup(txt) -> float:
    a = None
    while a is None:
        try:
            a = float(input(txt))
            return a
        except:
            print("Vložte číslo!!")


T_high_m = vstup("Vložte horní raní teplotu [°C]: ")
T_low_m = vstup("Vložte dolní raní teplotu [°C]: ")
T_high_a = vstup("Vložte horní večerní teplotu [°C]: ")
T_low_a = vstup("Vložte dolní večerní teplotu [°C]: ")
W = vstup("Vložte hodnotu vyrobeného ekvivalentu energie [kWh]: ")
T_avg_m = (T_high_m + T_low_m) / 2
T_avg_a = (T_high_a + T_low_a) / 2
T_delta = T_avg_a - T_avg_m
Q_delta = 1.16222 * 650 * T_delta
print(
    "dT: ",
    round(T_delta, 1),
    " °C ; dQ: ",
    round(Q_delta, 1),
    " Wh ; Spotřeba: ",
    round(W * 1000 - Q_delta, 1),
    " Wh",
)
