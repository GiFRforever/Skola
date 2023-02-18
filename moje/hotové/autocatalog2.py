import os, sys, shutil, re


def decide_where_to_move(path_org: str, výstupní_místa: list[str]) -> int:
    # check how big is the folder
    size: float = 0
    for root, _, files in os.walk(path_org):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    index_of_size: int = 0
    bsize: int = size
    while size > 1023:
        size /= 1024
        index_of_size += 1
    print("Size of the folder is", round(size, 2), "BKMGTPEZY"[index_of_size])
    # decide where to move
    # check if there is enough space on the drive
    max_freespace: tuple[int, int] = (-1, 0)
    for i, drive in enumerate(výstupní_místa):
        *_, freespace = shutil.disk_usage(drive)
        if freespace > bsize and freespace > max_freespace[1]:
            max_freespace = (i, freespace)
        else:
            print("Not enough space on", drive, end=" ")
            index_of_size = 0
            while freespace > 1023:
                freespace /= 1024
                index_of_size += 1
            print(f"({freespace} {'BKMGTPEZY'[index_of_size]} free)")
    # return the drive with the most free space
    if max_freespace[0] != -1:
        return max_freespace[0]
    else:
        raise Exception("Not enough space on any drive")


def new_name(file: str) -> str:
    filename_parts: list[str] = re.split("[. _-]", file)
    new_filename: list[str] = []
    for i, part in enumerate(filename_parts[:-1]):
        part: str
        try:
            if int(part[:-1]) < 100 and i != 0:  # if it is a resolution or a year
                raise Exception
            break
        except:
            # Tekes care of capitalization
            if part.lower() in ["of", "and", "a", "an"]:
                if i == 0:
                    part = part.capitalize()
                else:
                    part = part.lower()
            elif len(part) > 1:
                if part[0].lower() == "s" and part[1].isdigit():
                    part = part.upper()
                else:
                    part = part.capitalize()
            new_filename.append(part)
    if filename_parts[-1] == "dir":
        return " ".join(new_filename)
    else:
        return " ".join(new_filename) + "." + filename_parts[-1]


složky: list[str] = []
if len(sys.argv) == 2:
    složky: list[str] = [sys.argv[1]]
elif __name__ == "__main__" and len(sys.argv) == 1:
    presets: list[str] = ["U:\\Filmy\\", "U:\\Seriály\\"]
    print(
        "Presets:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(presets, start=1)],
    )
    preset = input("Enter preset: ")
    try:
        preset = presets[int(preset) - 1]
    except:
        preset: str = input("Enter path to original folder: ")

    for _, dirs, _ in os.walk(preset):
        odstavení: int = len(str(len(dirs)))
        print(
            "\nAvailable dirs:\n",
            *[f"{i:>{odstavení}}: {n}\n" for i, n in enumerate(dirs, start=1)],
        )
        dir: str = input("Enter dir: ")
        try:
            složky: list[str] = [
                os.path.join(preset, dirs[int(s) - 1]) for s in dir.split()
            ]
        except:
            složky: list[str] = [
                input("Wrong input. Please enter path to original folder: ")
            ]
        break
else:
    exit("Unsupported inicialization. Only one optional argument (the path)")

for path_org in složky:
    # check if path exists
    if not os.path.exists(path_org):
        raise Exception("Path does not exist")

    # check if path ends with backslash
    if path_org[-1] != "\\":
        path_org += "\\"

    výstupní_místa_seriály: list[str] = ["T:\\Seriály\\"]
    výstupní_místa_filmy: list[str] = ["I:\\Filmy\\", "J:\\"]

    if path_org.split("\\")[1] == "Seriály":
        if len(path_org.split("\\")[2].split(".")) == 1:
            type_of_media: str = "ss"
        else:
            type_of_media: str = "s"
    elif path_org.split("\\")[1] == "Filmy":
        type_of_media: str = "m"
    else:
        type_of_media: str = input("Enter type of media (serial or movie): ")

    if type_of_media[0] == "s":
        path_new: str = výstupní_místa_seriály[
            decide_where_to_move(path_org, výstupní_místa_seriály)
        ]
        # if len(path_org.split("\\")[2].split(".")) == 1:
        #     type_of_media = "ss"
        # else:
        #     type_of_media = "s"
    elif type_of_media[0] == "m":
        path_new = výstupní_místa_filmy[
            decide_where_to_move(path_org, výstupní_místa_filmy)
        ]
        # type_of_media = "m"
    else:
        raise Exception("Wrong type of media")

    print("Moving from", path_org, "to", path_new)

    # decide
    if type_of_media == "s":
        new_dir_parts: str = new_name(path_org.split("\\")[-2] + ".dir").split()  # type: ignore
        new_dir: str = os.path.join(
            path_new, " ".join(new_dir_parts[:-1]), new_dir_parts[-1]
        )
        os.makedirs(new_dir, exist_ok=True)
        for root, _, files in os.walk(path_org):
            for file in files:
                if not file.endswith(("mkv", "mp4", "avi", "srt", "idx", "sub")):
                    continue
                new_filename: str = new_name(file)
                os.system(
                    f'start /wait cmd /c robocopy "{root[:-1]}" "{new_dir}" "{file}"'
                )
                try:
                    os.rename(
                        os.path.join(new_dir, file), os.path.join(new_dir, new_filename)
                    )
                except:
                    os.rename(
                        os.path.join(new_dir, file),
                        os.path.join(new_dir, new_filename + " (1)"),
                    )
    elif type_of_media == "ss":
        hloubka: int = len(path_org.split("\\"))
        for root, _, files in os.walk(path_org):
            if len(root.split("\\")) > hloubka:
                continue
            for file in files:
                if not file.endswith(("mkv", "mp4", "avi", "srt", "idx", "sub")):
                    continue
                new_dir_parts: str = new_name(root.split("\\")[-2] + ".dir").split()  # type: ignore
                new_dir: str = os.path.join(
                    path_new, " ".join(new_dir_parts[:-1]), new_dir_parts[-1][:3]
                )
                os.makedirs(new_dir, exist_ok=True)
                new_filename: str = new_name(file)
                os.system(
                    f'start /wait cmd /c robocopy "{root[:-1]}" "{new_dir}" "{file}"'
                )
                try:
                    os.rename(
                        os.path.join(new_dir, file), os.path.join(new_dir, new_filename)
                    )
                except:
                    os.rename(
                        os.path.join(new_dir, file),
                        os.path.join(new_dir, new_filename + " (1)"),
                    )

    elif type_of_media == "m":
        for *_, files in os.walk(path_org):
            for file in files:
                if not file.endswith(("mkv", "mp4", "avi", "srt", "idx", "sub")):
                    continue
                new_filename: str = new_name(file)
                os.system(
                    f'start /wait cmd /c robocopy "{path_org[:-1]}" "{path_new[:-1]}" "{file}"'
                )
                try:
                    os.rename(
                        os.path.join(path_new, file),
                        os.path.join(path_new, new_filename),
                    )
                except:
                    os.rename(
                        os.path.join(path_new, file),
                        os.path.join(path_new, new_filename + " (1)"),
                    )
