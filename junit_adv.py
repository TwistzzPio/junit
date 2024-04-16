def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    while True:
        try:
            num = int(input("Nhập một số nguyên dương: "))
            if is_prime(num):
                print(f"{num} là số nguyên tố.")
            else:
                print(f"{num} không phải là số nguyên tố.")
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")

if __name__ == "__main__":
    main()

