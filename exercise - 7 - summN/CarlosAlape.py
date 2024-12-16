def summN(n, numbers):
    if n == 0:
        return 0
    return numbers[0] + summN(n - 1, numbers[1:])

def main():
    print(summN(3, [2, 4, 6, 8, 10, 12])) # 12
    
if __name__ == "__main__":
    main()