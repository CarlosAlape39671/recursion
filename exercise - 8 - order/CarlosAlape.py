def order(numbers: list) -> list:
    if len(numbers) == 0:
        return []
    min_num = min(numbers)
    numbers.remove(min_num)
    return [min_num] + order(numbers)

def main() -> None:
    print(order([3,6, -1])) # [-1, 3, 6]

if __name__ == "__main__":
    main()