db: list[tuple[str, int, float, float]] = []
with open("4L PRG\\8\\listek.txt", "r") as f:
    for line in f:
        try:
            t = line.strip().replace(",", ".").split()
            print(t)
            db.append(
                tuple(
                    str(t[0]),
                    int(t[1]),
                    float(t[2]),
                    float(t[3]),
                )
            )
        except:
            pass

print(db)
