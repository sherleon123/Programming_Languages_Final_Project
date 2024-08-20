from functools import reduce


# 1. Fibonacci Sequence Generator
def fibonacci_sequence(n):
    fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])[:n]
    print(f"First {n} Fibonacci numbers: {fibonacci(n)}")


# 2. Concatenate Strings with a Space (Without 'join')
def concatenate_strings():
    lst = input("Enter a list of strings separated by commas: ").split(',')
    concat_strings = lambda lst: reduce(lambda x, y: x + ' ' + y, lst)
    print(f"Concatenated string: {concat_strings(lst)}")


# 3. Cumulative Sum of Squares of Even Numbers in Sublists
def cumulative_sum_squares():
    lst = [
        list(map(int, input("Enter numbers for sublist separated by spaces: ").split()))
        for _ in range(int(input("Enter the number of sublists: ")))
    ]
    cum_sum_squares = lambda lst: list(
        map(lambda sub: reduce(lambda acc, x: acc + (lambda y: y ** 2)(x), filter(lambda x: x % 2 == 0, sub), 0), lst))
    print(f"Cumulative sum of squares of even numbers: {cum_sum_squares(lst)}")


# 4. Higher-Order Function for Cumulative Operation (Factorial and Exponentiation)
def higher_order_function():
    def cumulative(op):
        return lambda seq: reduce(op, seq)

    factorial = cumulative(lambda x, y: x * y)
    exponentiation = lambda base, exp: cumulative(lambda x, _: x * base)([base] * (exp - 1))

    choice = input("Choose 'factorial' or 'exponentiation': ").strip().lower()

    if choice == 'factorial':
        n = int(input("Enter the number to calculate factorial: "))
        print(f"Factorial of {n}: {factorial(range(1, n + 1))}")
    elif choice == 'exponentiation':
        base = int(input("Enter the base: "))
        exp = int(input("Enter the exponent: "))
        print(f"{base} raised to the power of {exp}: {exponentiation(base, exp)}")
    else:
        print("Invalid choice!")


# 5. Filter, Map, Reduce for Sum of Squares of Even Numbers
def sum_of_squares_of_evens():
    nums = [1, 2, 3, 4, 5, 6]
    result = reduce(lambda acc, x: acc + x ** 2, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)), 0)
    print(f"Sum of squares of even numbers: {result}")


# 6. Count Palindromes in Sublists
def count_palindromes():
    lst = [
        input("Enter strings for sublist separated by commas: ").split(',')
        for _ in range(int(input("Enter the number of sublists: ")))
    ]
    count_palindromes = lambda lst: list(map(lambda sub: len(list(filter(lambda s: s == s[::-1], sub))), lst))
    print(f"Number of palindromes in each sublist: {count_palindromes(lst)}")


# 7. Lazy Evaluation Explanation
def lazy_evaluation_explanation():
    def generate_values():
        print('Generating values...')
        yield 1
        yield 2
        yield 3

    def square(x):
        print(f'Squaring {x}')
        return x * x

    print('Eager evaluation:')
    values = list(generate_values())
    squared_values = [square(x) for x in values]
    print(squared_values)

    print('\nLazy evaluation:')
    squared_values = [square(x) for x in generate_values()]
    print(squared_values)


# 8. Filter and Sort Prime Numbers in Descending Order
def primes_descending():
    is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
    lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    primes_desc = lambda lst: sorted(filter(is_prime, lst), reverse=True)
    print(f"Prime numbers in descending order: {primes_desc(lst)}")


def main():
    options = {
        '1': lambda: fibonacci_sequence(int(input("Enter the number of Fibonacci numbers to generate: "))),
        '2': lambda: concatenate_strings([s.strip() for s in input("Enter a list of strings separated by commas: ").split(',')]),
        '3': cumulative_sum_squares,
        '4': higher_order_function,
        '5': sum_of_squares_of_evens,
        '6': count_palindromes,
        '7': lazy_evaluation_explanation,
        '8': primes_descending
    }

    while True:
        print("\nChoose a question to run:")
        print("1. Fibonacci Sequence Generator")
        print("2. Concatenate Strings with a Space")
        print("3. Cumulative Sum of Squares of Even Numbers in Sublists")
        print("4. Higher-Order Function (Factorial and Exponentiation)")
        print("5. Sum of Squares of Even Numbers Using Filter, Map, Reduce")
        print("6. Count Palindromes in Sublists")
        print("7. Lazy Evaluation Explanation")
        print("8. Filter and Sort Prime Numbers in Descending Order")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '9':
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice, please try again.")


main()