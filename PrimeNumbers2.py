class PrimeNumberGenerator:
    def generate_prime_numbers(self, x, y):
        prime_numbers = []
        for num in range(x, y+1):
            if num <= 1:
                continue
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
        return prime_numbers


prime = PrimeNumberGenerator()
prime_numbers = prime.generate_prime_numbers(1, 1000)
print(prime_numbers)
print(f"there are {len(prime_numbers)} numbers in your list")
