def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(n):
    if n % 2 != 0 or n <= 2:
        print("Invalid input. Please enter an even number greater than 2.")
        return
    
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(f"{i} + {n-i}")

# Test the function with an even number
n = int(input('Enter an even number: '))
goldbach_conjecture(n)
