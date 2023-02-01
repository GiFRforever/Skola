import sys

input("Press Enter to continue...")
sys.stdout.write("\033[F")  # back to previous line
sys.stdout.write("\033[K")  # clear line
print("SUCCESS!")
input("Press Enter to continue...")
