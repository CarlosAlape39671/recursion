def mix(list: list, other: list) -> list:
    if len(list) == 0:
        return other
    if len(other) == 0:
        return list
    if list[0] < other[0]:
        return [list[0]] + mix(list[1:], other)
    return [other[0]] + mix(list, other[1:])

def main() -> None:
    print(mix([2, 4, 6, 8, 10, 12], [1, 3, 5, 7, 9, 11])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if __name__ == "__main__":
    main()