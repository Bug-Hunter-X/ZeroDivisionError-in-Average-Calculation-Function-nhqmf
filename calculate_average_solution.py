def calculate_average(numbers):
    if not numbers:
        return 0
    if sum(numbers) == 0 and len(numbers) > 0:
        return 0 #Handle only zeros case
    return sum(numbers) / len(numbers)