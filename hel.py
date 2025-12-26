# fibonacci number 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Example usage
if __name__ == "__main__":
    num = 10
    print(f"Fibonacci number at position {num} is {fibonacci(num)}")
# This code defines a function to compute the nth Fibonacci number using recursion. 

