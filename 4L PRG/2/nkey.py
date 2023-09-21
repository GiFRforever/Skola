import sys
import select
import os

try:
    import msvcrt
except ImportError:
    isWindows = False
    import termios
else:
    isWindows = True


class KeyPuller:
    def __enter__(self):
        global isWindows
        if isWindows:
            self.capturedChars = []
        else:
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = self.new_term[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

        return self

    def __exit__(self, type, value, traceback):
        if not isWindows:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def poll(self) -> str | None:
        if isWindows:
            if not len(self.capturedChars) == 0:
                return self.capturedChars.pop(0)

            while msvcrt.kbhit():
                char = msvcrt.getch()
                self.capturedChars.append(char.decode("utf-8"))

            if not len(self.capturedChars) == 0:
                return self.capturedChars.pop(0)
            else:
                return None
        else:
            dr, dw, de = select.select([sys.stdin], [], [], 0)
            if not dr == []:
                return os.read(self.fd, 1).decode("utf-8")
            return None


def main():
    while True:
        with KeyPuller() as keyPuller:
            c = vstup(keyPuller)
            if c is not None:
                print(f"Received: {c}")


def vstup(keyPuller):
    if c := keyPuller.poll():
        return c


if __name__ == "__main__":
    main()
