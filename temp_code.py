import time

# Inefficient function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime (not optimized)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Function to filter prime numbers from a list (inefficient)
def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

# Function to calculate the sum of squares (redundant calculations)
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total

# Main execution
if __name__ == "__main__":
    numbers = list(range(1, 1000))

    # Factorial computation (inefficient for large numbers)
    start = time.time()
    print(f"Factorial of 10: {factorial(10)}")
    print(f"Calculated in {time.time() - start:.5f} seconds")

    # Filter primes
    start = time.time()
    primes = filter_primes(numbers)
    print(f"Found {len(primes)} primes")
    print(f"Calculated in {time.time() - start:.5f} seconds")

    # Sum of squares
    start = time.time()
    print(f"Sum of squares: {sum_of_squares(numbers)}")
    print(f"Calculated in {time.time() - start:.5f} seconds")
