def mean(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Returns the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    """Returns the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    for num in frequency:
        if frequency[num] == max_freq:
            return num

def main():
    """Prompt user for numbers and test the statistical functions."""
    input_str = input("Enter numbers separated by spaces: ")
    try:
        data = [float(x) for x in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print("Data:", data)
    print("Mean:", mean(data))
    print("Median:", median(data))
    print("Mode:", mode(data))

if __name__ == "__main__":
    main()
