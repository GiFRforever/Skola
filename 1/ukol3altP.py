try:
    import pandas as pd
    #print("module ''' is installed")
except ModuleNotFoundError:
    print("module 'pandas' is not installed")
    import pip
    import subprocess
    import sys
    def install(package):
    	subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install("pandas")
    import pandas as pd
    
vstup = input("Vložte řetězec:")
cisla = []
out = []
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
	out.extend([[i, pos, ppos]])
df = pd.DataFrame(out, columns=["Číslo", "Poslední", "Předposlední"])
df.set_index("Číslo", inplace=True)
print(df)