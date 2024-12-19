def withoutDuplicates(list: list) -> list:
    if list[0] in list[1:]:
        list.remove(list[0])
        return withoutDuplicates(list)
    return [list[0]] + withoutDuplicates(list[1:]) if len(list) > 1 else list

def main() -> None:
    print(withoutDuplicates([3, 6, -1, 3, 6, 3])) # [-1, 6, 3]

if __name__ == "__main__":
    main()