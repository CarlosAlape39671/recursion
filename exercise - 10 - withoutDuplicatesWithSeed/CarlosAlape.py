def withoutDuplicatesWithSeed(list: list, result: list) -> list:
    if len(list) == 0:
        return result
    if list[0] in result:
        return withoutDuplicatesWithSeed(list[1:], result)
    return withoutDuplicatesWithSeed(list[1:], result + [list[0]]) if len(list) > 1 else result + list
    

def main() -> None:
    print(withoutDuplicatesWithSeed([3, 6, -1, 3, 6, 3], [])) # [3, 6, -1]

if __name__ == "__main__":
    main()