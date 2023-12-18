from hashlib import md5

sekret = "69"


def md5c(s):
    return md5(s.encode()).hexdigest()



# target = md5c(sekret)
target = "j9T$3KhZWtld0SwPhAgKkK7Fx0$shk6GUPJAol.l68Zm5gjUDDEuPeJo7iW72pLcZgjer1"

znaky = [chr(i) for i in range(32, 127)]
print(*znaky)

def bruteforce(l: int):
    for i in znaky:
        if l == 1:
            yield i
        else:
            for j in bruteforce(l - 1):
                yield i + j


i = 1
while True:
    print(i)
    for t in bruteforce(i):
        if md5c(t) == target:
            print(t)
    i += 1
