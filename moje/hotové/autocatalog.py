import os, sys, shutil, re


def decide_where_to_move(path_org: str, výstupní_místa: list[str]) -> int:
    # check how big is the folder
    size: float = 0
    for root, dirs, files in os.walk(path_org):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    # print("Size of the folder is", size, "bytes")
    isize: int = 0
    while size > 1023:
        size /= 1024
        isize += 1
    print("Size of the folder is", round(size, 2), "BKMGTPEZY"[isize])
    # decide where to move
    # check if there is enough space on the drive
    for i in range(len(výstupní_místa)):
        *_, freespace = shutil.disk_usage(výstupní_místa[i])
        if freespace > size:
            return i
        print("Not enough space on", výstupní_místa[i], end=" ")
        isize = 0
        while freespace > 1023:
            freespace /= 1024
            isize += 1
        print(f"({freespace} {'BKMGTPEZY'[isize]} free)")
    # if there is not enough space on any drive, raise an exception
    raise Exception("Not enough space on any drive")


def rename_folder(path: str) -> tuple[str, str]:
    # rename the folder
    for i, (root, _, files) in enumerate(os.walk(path)):
        for file in files:
            file_parts: list[str] = re.split("[. _-]", file)
            if file_parts[-1] in ["mkv", "mp4", "avi", "srt", "idx", "sub"]:
                file_name: list[str] = []
                for i, part in enumerate(file_parts[:-1]):
                    try:
                        if (
                            int(part[:-1]) < 100 and i != 0
                        ):  # if it is a resolution or a year
                            raise Exception
                        break
                    except:
                        file_name.append(part)
                for i, s in enumerate(file_name):
                    if s in ["of", "and", "a", "an"] and i != 0:
                        continue
                    elif s[0].lower() == "s" and s[1].isnumeric():
                        file_name[i] = s.upper()
                    else:
                        file_name[i] = s.capitalize()
                try:
                    os.rename(
                        os.path.join(root, file),
                        os.path.join(root, " ".join(file_name) + "." + file_parts[-1]),
                    )
                except PermissionError:
                    input(
                        "Stop the torrent (permission error). Press enter to continue."
                    )
                    os.rename(
                        os.path.join(root, file),
                        os.path.join(root, " ".join(file_name) + "." + file_parts[-1]),
                    )
            else:
                os.remove(os.path.join(root, file))

    if type_of_media == "s":
        parentdir: str = "\\".join(path.split("\\")[:-2])
        root_name: list[str] = path.split("\\")[-2].split(".")
        root_name_new: list[str] = []
        season: str = ""
        for part in root_name:
            if part[0] == "S" and part[1:].isnumeric():
                season: str = part
                break
            root_name_new.append(part)
        os.makedirs(
            os.path.join(parentdir, " ".join(root_name_new)),
            exist_ok=True,
        )
        os.rename(path, parentdir + "\\" + season)
        shutil.move(
            parentdir + "\\" + season,
            os.path.join(parentdir, " ".join(root_name_new)),
        )
        return parentdir, " ".join(root_name_new)
    elif type_of_media == "ss":
        parentdir: str = "\\".join(path.split("\\")[:-1])
        root_name: list[str] = path.split("\\")[-1].split(".")
        root_name_new: list[str] = []
        season: str = ""
        for part in root_name:
            if part[0] == "S" and part[1:3].isnumeric():
                season: str = part[:3]
                break
            root_name_new.append(part)
        os.makedirs(
            os.path.join(parentdir, " ".join(root_name_new)),
            exist_ok=True,
        )
        os.rename(path, parentdir + "\\" + season)
        shutil.move(
            parentdir + "\\" + season,
            os.path.join(parentdir, " ".join(root_name_new)),
        )
        return parentdir, " ".join(root_name_new)
    else:
        return path, ""


if len(sys.argv) == 2:
    path_org = sys.argv[1]
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

    dirs: list[str] = []
    for _, d, _ in os.walk(preset):
        dirs = d
        break

    print(
        "\nAvailable dirs:\n",
        *[f"{i}: {n}\n" for i, n in enumerate(dirs, start=1)],
    )
    dir: str = input("Enter dir: ")
    try:
        path_org: str = os.path.join(preset, dirs[int(dir) - 1])
    except:
        path_org: str = input("Wrong input. Please enter path to original folder: ")
else:
    exit("Unsupported inicialization. Only one optional argument (the path)")
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
    if len(path_org.split("\\")[2].split(".")) == 1:
        type_of_media = "ss"
    else:
        type_of_media = "s"
elif type_of_media[0] == "m":
    path_new = výstupní_místa_filmy[
        decide_where_to_move(path_org, výstupní_místa_filmy)
    ]
    type_of_media = "m"
else:
    raise Exception("Wrong type of media")

print("Moving from", path_org, "to", path_new)

# decide
if type_of_media == "s":
    parent_dir, new_name = rename_folder(path_org)
    # windows robocopy
    os.system(
        f'start /wait cmd /c robocopy  "{os.path.join(parent_dir, new_name)}" "{os.path.join(path_new, new_name)}" /S /MOVE'
    )
elif type_of_media == "ss":
    for masterdir, episodes, _ in os.walk(path_org):
        for episode in episodes:
            parent_dir, new_name = rename_folder(os.path.join(masterdir, episode))
            # windows robocopy
            os.system(
                f'start /wait cmd /c robocopy  "{os.path.join(parent_dir, new_name)}" "{os.path.join(path_new, new_name)}" /S /MOVE'
            )
        break
elif type_of_media == "m":
    parent_dir, _ = rename_folder(path_org)
    os.system(
        f'start /wait cmd /c robocopy  "{parent_dir[:-1]}" "{path_new[:-1]}" /MOVE'  # type: ignore
    )
    try:
        shutil.rmtree(path_org[:-1])
    except:
        pass
