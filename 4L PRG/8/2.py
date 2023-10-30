db = {}
with open("jmena.txt", "r") as f:
    for line in f:
        try:
            jmeno, vek = line.split("-")
            db[jmeno.strip()] = int(vek)
        except:
            pass


oldest = max(db, key=lambda x: db[x])
print(f"Nejstarší je {oldest} ve věku {db[oldest]} let.")
