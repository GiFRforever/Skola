from keypuller import KeyPuller

white = {"Novák": "+420 603 763 466", "Bittner": "+420 792 333 630", "Česnek": "+420 776 324 232", "Glac": "+420 735 968 231"}

lines = [f"{(name+':'):10} {white[name]}" for name in white]
print(*lines, sep="\n")


with KeyPuller() as keyPoller:
    while True:
        c = keyPoller.poll()
        if not c is None:
            print("You pressed", c)