def toUppercase(string: str) -> str:
    if string == "":
        return ""
    return string[0].upper() + toUppercase(string[1:])

def main() -> None:
    print(toUppercase("this is a test")) # "THIS IS A TEST"

if __name__ == "__main__":
    main()