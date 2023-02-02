import os, shutil, re


def decide_where_to_move(path_org: str, výstupní_místa: list[str]) -> int:
    # check how big is the folder
    size: int = 0
    for root, dirs, files in os.walk(path_org):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    print("Size of the folder is", size, "bytes")
    # decide where to move
    # check if there is enough space on the drive
    for i in range(len(výstupní_místa)):
        *_, freespace = shutil.disk_usage(výstupní_místa[i])
        if freespace > size:
            return i
        print("Not enough space on", výstupní_místa[i], "(", freespace, "bytes)")
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

    else:
        return path, ""


path_org: str = input("Enter path to original folder: ")
# check if path exists
if not os.path.exists(path_org):
    raise Exception("Path does not exist")

# check if path ends with backslash
if path_org[-1] != "\\":
    path_org += "\\"

výstupní_místa_seriály: list[str] = ["T:\\Seriály\\"]
výstupní_místa_filmy: list[str] = ["I:\\Filmy\\", "J:\\"]

if path_org.split("\\")[1] == "Seriály":
    type_of_media: str = "s"
elif path_org.split("\\")[1] == "Filmy":
    type_of_media: str = "m"
else:
    type_of_media: str = input("Enter type of media (serial or movie): ")

if type_of_media[0] == "s":
    path_new: str = výstupní_místa_seriály[
        decide_where_to_move(path_org, výstupní_místa_seriály)
    ]
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
elif type_of_media == "m":
    parent_dir, _ = rename_folder(path_org)
    os.system(
        f'start /wait cmd /c robocopy  "{parent_dir[:-1]}" "{path_new[:-1]}" /MOVE'  # type: ignore
    )
