
def calculate_required_fuel(mass, accumulated_mass=0):
    """
    >>> calculate_required_fuel(12)
    2
    >>> calculate_required_fuel(14)
    2
    >>> calculate_required_fuel(1969)
    966
    >>> calculate_required_fuel(100756)
    50346
    """
    result = int(mass / 3) - 2
    if result < 0:
        return accumulated_mass
    else:
        accumulated_mass += result
        return calculate_required_fuel(result, accumulated_mass)


with open("input.txt") as input_file:
    data = map(int, input_file.read().split())
    fuel_required_per_module = [calculate_required_fuel(i) for i in data]
    fuel_required = sum(fuel_required_per_module)
    print(fuel_required)
