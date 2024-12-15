def match(one_list: list, other: list) -> list:
    if one_list == [] or other == []:
        return []
    return [(one_list[0], other[0])] + match(one_list[1:], other[1:])

def main():
    print(match([1,2,3], ['a','b','c'])) # [(1, 'a'), (2, 'b'), (3, 'c')]

if __name__ == "__main__":
    main()