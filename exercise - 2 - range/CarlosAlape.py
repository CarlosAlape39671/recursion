def range(start: int, end: int) -> list:
    if start == end:
        return [end]
    else:
        return range(start, end-1) + [end]

def __main__() -> None:
    print(range(5, 10))

if __name__ == "__main__":
    __main__()