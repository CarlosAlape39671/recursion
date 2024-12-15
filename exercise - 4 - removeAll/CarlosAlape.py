def removeAll(lst: list, value: int) -> list:
    if value not in lst:
        return lst
    lst.remove(value)
    return removeAll(lst, value)

def main() -> None:
    print(removeAll([1,2,3,1,6,7,1,9,1], 1)) # [2,3,6,7,9]

if __name__ == "__main__":
    main()