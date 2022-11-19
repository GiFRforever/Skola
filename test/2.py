def group_by_owners(files) -> dict[str, list[str]]:
    result = {}
    for key, value in files.items():
        if value not in result:
            result[value] = [key]
        elif value in result:
            result[value].append(key)
    return result


if __name__ == "__main__":
    files: dict[str, str] = {
        "Input.txt": "Randy",
        "Code.py": "Stan",
        "Output.txt": "Randy",
        "Test.py": "Stan",
        "Koala.txt": "Randy",
    }
    print(group_by_owners(files))
