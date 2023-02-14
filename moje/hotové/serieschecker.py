import os, sys
from imdb import Cinemagoer

# Disable
def blockPrint() -> None:
    sys.stdout = open(os.devnull, "w")


# Restore
def enablePrint() -> None:
    sys.stdout = sys.__stdout__


class log:
    def __init__(self, path: str) -> None:
        self.path: str = path
        with open(self.path, "w") as f:
            pass

    def printl(self, *args, **kwargs) -> None:
        enablePrint()
        print(*args, *kwargs)
        blockPrint()
        with open(self.path, "a") as f:
            f.write(" ".join([str(arg) for arg in args]) + "\n")


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


showspath: str = "T:\\Seriály\\"
ignore: list[str] = ["", "ASDFMOVIE", "The Dark", "The Walking Death", "WTF 101"]
printlogged = log("serieschecker.log").printl
ia = Cinemagoer()
for root, dirs, files in os.walk(showspath):
    if len(root.split("\\")) != 3 or (showr := root.split("\\")[-1]) in ignore:
        continue
    max: int = 0
    for dir in dirs:
        try:
            if int(dir[1:3]) > max:
                max = int(dir[1:3])
        except:
            continue
    if max == 0:
        printlogged("Issue at", root)
    else:
        try:
            # lookup show in imdb
            enablePrint()
            print(f"Looking up {showr}   ", end="\r")
            blockPrint()
            for search in ia.search_movie(showr, "tv series")[:5]:
                ia.update(search)
                if search["kind"] in ["tv series", "tv mini series"]:
                    show = search
                    break
            else:
                raise Exception("No show found")
            # ia.update(show)
            ia.update(show, "episodes")
            num_seasons: int = show["number of seasons"]  # type: ignore
            num_episodes: int = len(show["episodes"][num_seasons])
            last_episode = show["episodes"][num_seasons][num_episodes]
            while last_episode["title"] in [
                f"Episode #{num_seasons}.{num_episodes}",
                "TBA",
                "TBD",
                "",
            ]:
                num_seasons -= 1
                if num_seasons < max:
                    raise Exception("Incomplete db")
                num_episodes: int = len(show["episodes"][num_seasons])
                last_episode = show["episodes"][num_seasons][num_episodes]
            # enablePrint()
            if num_seasons > max:
                printlogged(
                    f"New season at {showr} | {show['title']} : {max} -> {num_seasons}"
                )
            else:
                sys.stdout.write("\033[K")
        except Exception as e:
            # enablePrint()
            printlogged(f"Issue at {root} durring lookup: {e}")
