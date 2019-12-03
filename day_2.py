def analyze_intcode(intcode):
    """
    >>> intcode = [1,1,1,4,99,5,6,0,99]
    >>> analyze_intcode(intcode)
    '30,1,1,4,2,5,6,0,99'
    >>> intcode = [1,0,0,0,99]
    >>> analyze_intcode(intcode)
    '2,0,0,0,99'
    >>> intcode = [2,4,4,5,99,0]
    >>> analyze_intcode(intcode)
    '2,4,4,5,99,9801'
    >>> intcode = [1,1,1,4,99,5,6,0,99]
    >>> analyze_intcode(intcode)
    '30,1,1,4,2,5,6,0,99'
    """

    pos = 0
    while pos < len(intcode):
        if intcode[pos] == 1:
            first_summand, second_summand, result_position = intcode[pos + 1: pos + 4]
            intcode[result_position] = intcode[first_summand] + intcode[second_summand]
        elif intcode[pos] == 2:
            first_multiplier, second_multiplier, result_position = intcode[pos + 1: pos + 4]
            intcode[result_position] = intcode[first_multiplier] * intcode[second_multiplier]
        elif intcode[pos] == 99:
            break

        pos = pos + 4
    result = ','.join([str(elem) for elem in intcode])
    return result


with open("input_2.txt") as input_file:
    data = input_file.read()
    parsed_ints = [int(x) for x in data.split(',')]
    parsed_ints[1] = 12
    parsed_ints[2] = 2
    print(parsed_ints)
    result = analyze_intcode(parsed_ints)
    print(result)

