import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number) + 1)):
        if number % element == 0:
            return False
    return True


def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count


def benchmark(upper_bound: int) -> int:
    start_time = perf_counter()
    value = count_prime_numbers(upper_bound)
    end_time = perf_counter()
    run_time = end_time - start_time
    logging.info(
        f"Execution of count_prime_numbers took {run_time: .2f} seconds." 
    )
    return value

# class LoggingDecorator(AbstractDecorator):
#     def execute(self, upper_bound: int) -> int:
#         logging.info(f"Calling {self._decorated.__class__.__name__}")
#         value = self._decorated.execute(upper_bound)
#         logging.info(f"Finished Calling {self._decorated.__class__.__name__}")
#         return value

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = benchmark(100000)
    logging.info(f"Found {value} prime numbers.")


    
if __name__ == "__main__":
    main()

