import re
import numpy as np
from tabulate import tabulate
import math as mt

#prime_txt = "H:/mujgit/Skola/moje/p/primes.txt"
#prime_txt = "/storage/sdcard1/Kde/python/moje/primes.txt"
prime_txt: str = "moje\\p\\primes.txt"
while True:
	vstup = None
	cisilka: list = []
	c_0: list = []
	while vstup == None:
		vstup = input("Vložte list: ")
		if vstup == "q":
				exit()
		try:
			vstup = re.findall(r'\b\d+\b', vstup)
			if vstup == []:
				raise Exception
			cisilka = [int(x) for x in vstup]
		except:
			print("Chybný vstup!")
			vstup = None
	#print(cisilka)
	with open(prime_txt, "r") as f:
		primes = []
		#primes = ([int(x) for x in f.readlines() if int(x) <= (min(cisilka)//2) else break])
		for line in f:
			if int(line) <= (min(cisilka)//2):
				primes.append(int(line))
			else:
				break
	#print(primes)
	for i,c in zip(range(len(cisilka)),cisilka):
		temp: list[int] = []
		n: int = 0
		while n == 0:
			m: int = 0
			for x in primes:
				#print(x)
				if c % x ==0:
					c /= x
					temp.append(x)
					m: int = 1
			if m == 0:
				n = 1
		globals()[f"c_{i}"] = temp
			
		#globals()[f"c_{i}"] = [x for x in primes if x <= c and c % x == 0]
		#print(globals()[f"c_{i}"])
	comdevs: list[int] = c_0
	#print(comdevs)
	if len(cisilka) != 1:
		for i in range(1,len(cisilka)):
			comdevs = list(set(comdevs)&set(globals()[f"c_{i}"]))
	#print(comdevs)
	cisilkaout = []
	for c,i in zip(cisilka,range(len(cisilka))):
		globals()[f"c_{i}"].sort()
		globals()[f"ct_{i}"] = " ".join(str(x) for x in globals()[f"c_{i}"])
		cisilkaout.append([c,c/np.prod(comdevs),globals()[f"ct_{i}"]])
	if comdevs != []:
		print(tabulate(cisilkaout, headers=["in","out","devs"]))
		print(f"Společní jmenovatelé: {comdevs} = {np.prod(comdevs)}")
	else:
		print("Žádný společný jmenovatel")
	
	
		
		