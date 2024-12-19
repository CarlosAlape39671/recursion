def isEven(n) -> bool:
    if n == 0:
        return True
    return isEven(n - 1) == False

def main() -> None:
    print(isEven(4)) # True
    print(isEven(5)) # False

if __name__ == "__main__":
    main()