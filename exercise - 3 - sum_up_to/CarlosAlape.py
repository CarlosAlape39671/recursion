def sum_up_to(n) -> int:
    if n == 0:
        return 0
    return n + sum_up_to(n - 1)

def __main__() -> None:
    print(sum_up_to(10)) # 55

if __name__ == "__main__":
    __main__()