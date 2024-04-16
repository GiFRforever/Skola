import hashlib


def md5(vstup) -> str:
    return hashlib.md5(vstup.encode("utf-8")).hexdigest()


# i = 0
# while True:
#     if md5("admin;;;tajnyobsah;;;" + str(i)) == "f2e6e6ddcf2ef0a2a29471c0cbd79a60":
#         print(i)
#         break
#     i += 1

print(md5("uzivatel;;;tajnyobsah;;;heslo"))
