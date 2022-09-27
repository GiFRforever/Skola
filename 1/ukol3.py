import pprint
vstup = input("Vložte řetězec:")

cisla = []
for z in vstup.split():
   if z.isdigit():
      cisla.append(z)

for i in cisla:
	try:
		pos = i[-1]
	except:
		pos = "Není"
	try:
		ppos = i[-2]
	except:
		ppos = "Není"
	print(i,": poslední = ",pos," ; předposlední = ",ppos)