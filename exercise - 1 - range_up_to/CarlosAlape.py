def range_up_to(n: int) -> list:
    if n == 0:
        return [0]
    else:
        return range_up_to(n-1) + [n]

def __main__() -> None:
    print(range_up_to(5))

if __name__ == "__main__":
    __main__()