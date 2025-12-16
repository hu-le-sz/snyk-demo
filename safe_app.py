# safe_app.py
# A simple, safe program with no external dependencies.

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    :param numbers: list of int or float
    :return: float
    :raises ValueError: if the list is empty
    :raises TypeError: if any item is not a number
    """
    if not numbers:
        raise ValueError("List of numbers cannot be empty.")

    total = 0.0
    count = 0

    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("All items must be int or float, got: "
                            f"{type(n).__name__}")
        total += n
        count += 1

    return total / count

import subprocess


def ping_host_vulnerable():
    """
    ❌ INTENTIONALLY VULNERABLE FUNCTION (for Snyk demo)
    """
    host = input("Enter a host to ping: ")
    command = f"ping -c 1 {host}"
    subprocess.run(command, shell=True, check=False)

def main():
    values = [10, 20, 30, 40]
    avg = calculate_average(values)
    print(f"Input values: {values}")
    print(f"Average: {avg}")

    # ❌ vulnerable call
    ping_host_vulnerable()



if __name__ == "__main__":
    main()
