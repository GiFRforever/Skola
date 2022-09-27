import math


def vstup(txt):
    bagr = None
    while bagr is None:
        try:
            bagr = float(input(txt))
            return bagr
        except:
            print("Vložte číslo!!")


hrubá_mzda = vstup("Zadejte hrubou mzdu: ")
# print kolik je 13% sociálního pojištění a 6% zdravotního pojištění a 15% daně z příjmu
sociální_pojištění = hrubá_mzda * 0.13
zdravotní_pojištění = hrubá_mzda * 0.06
základ_daně = hrubá_mzda - sociální_pojištění - zdravotní_pojištění - 3170
daně_z_příjmu = základ_daně * 0.15
čistá_mzda = hrubá_mzda - sociální_pojištění - zdravotní_pojištění - daně_z_příjmu
print(
    "Sociální pojištění: {} CZK, Zdravotní pojištění: {} CZK, Daně z příjmu: {} CZK".format(
        math.floor(sociální_pojištění),
        math.floor(zdravotní_pojištění),
        math.floor(daně_z_příjmu),
    )
)
print("Čistá mzda: {} CZK".format(math.floor(čistá_mzda)))