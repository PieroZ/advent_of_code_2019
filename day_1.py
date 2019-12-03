
def calculate_required_fuel(mass):
    """
    >>> calculate_required_fuel(12)
    2
    >>> calculate_required_fuel(14)
    2
    >>> calculate_required_fuel(1969)
    654
    >>> calculate_required_fuel(100756)
    33583
    """
    return int(mass / 3) - 2


with open("input.txt") as input_file:
    data = map(int, input_file.read().split())
    fuel_required_per_module = [calculate_required_fuel(i) for i in data]
    fuel_required = sum(fuel_required_per_module)
    print(fuel_required)
