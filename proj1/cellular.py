import argparse


def decimal_to_binary(x):
    """
    This function converts a decimal number N into a binary number with 8 bits.
    :param x: The decimal number

    >>> decimal_to_binary(30)
    '00011110'
    >>> decimal_to_binary(139)
    '10001011'
    """
    assert 0 <= x <= 255
    # START OF YOUR CODE

    bin = ""
    while x > 0:
        bin = str(x % 2) + bin
        x //= 2
    bin = '0' * (8 - len(bin)) + bin    #add leading zeros
    return bin

    # END OF YOUR CODE


def generate(rule, steps):
    """
    Generate the image from given rule number and steps
    and print it to the console.
    The output image should have width of 2 * STEPS + 1 and height of STEPS + 1.

    :param rule: The rule number
    :param steps: Number of lines

    >>> generate(30, 5)
    P1 11 6
    0 0 0 0 0 1 0 0 0 0 0
    0 0 0 0 1 1 1 0 0 0 0
    0 0 0 1 1 0 0 1 0 0 0
    0 0 1 1 0 1 1 1 1 0 0
    0 1 1 0 0 1 0 0 0 1 0
    1 1 0 1 1 1 1 0 1 1 1

    >>> generate(30, 3)
    P1 7 4
    0 0 0 1 0 0 0
    0 0 1 1 1 0 0
    0 1 1 0 0 1 0
    1 1 0 1 1 1 1
    """
    # START OF YOUR CODE

    def display(state):
        content = ''
        for i in range(len(state)):
            if i != 0 and i != len(state) - 1:
                content += state[i]
                if i != len(state) - 2:
                    content += " "
        print(content)

    print('P1 %d %d'%(2 * steps + 1, steps + 1))    #process pbm format
    rule = ruleGenerator(decimal_to_binary, rule)   #transform the decimal-format rule into a 8-bits binary series 
    initial_state = ['0' for i in range(steps + 1)] + ['1'] + ['0' for i in range(steps + 1)]   #add two permanently-off sentinels to the header position and trailer position
    current_state = initial_state
    display(current_state)
    for i in range(steps):
        next_state = update(current_state, update_method, rule)
        current_state = next_state
        display(next_state)

    # END OF YOUR CODE


# TODO: You may add any additional functions here
def ruleGenerator(transformation_rule, original_number):
    '''
    Generate the concrete rule of cellular automation
    input: a tranformation rule(function type), a original rule number(int type)
    output: a actual rule number transformed from original rule number
    '''
    rule = transformation_rule(original_number)
    return rule


def update(last_state, update_method, rule):
    '''
    In use of updating the status of cellular automation at once
    input: last state(list-of-strings type), update method for elements(function type), 
    and the rule of cellular automation(a 8-bits binary series)
    output: current state(list-of-strings type)
    '''
    current_state = last_state[ : ]
    length = len(last_state)
    for i in range(length):
        if i == 0 or i == length - 1:   #ignore the situation of two sentinels
            pass
        else:
            three_bits_state_last_time = last_state[i - 1 : i + 2]
            current_state[i] = update_method(three_bits_state_last_time, rule)
    return current_state


def update_method(three_bits_state, rule):
    '''
    Update the state of a particular cell at current time.
    input: a 3-bits binary series(string type), the rule of
           cellular automation(8-bits binary series)
    output: the state(string type, ranged from 0 to 1)
    >>> update_method('100', ruleGenerator(decimal_to_binary, 30))
    '1'
    
    >>> update_method('011, ruleGenerator(decimal_to_binary, 30))
    '1'
    '''
    def toDecimal():
        '''
        Transform a 3-bits binary series into a decimal number
        >>> toDecimal('100')
        4
        '''
        decimal_number = 0
        pow_based_2 = lambda n : 2 ** n
        for i in range(3):
            decimal_number += int(three_bits_state[2 - i]) * pow_based_2(i)
        return decimal_number
    
    corresponding_index = toDecimal()
    return rule[7 - corresponding_index]


if __name__ == '__main__':
    # START OF YOUR CODE
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Project 1: Cellular Automation")
    parser.add_argument('rule', type=int, help='The rule of cellular automation')
    parser.add_argument('steps', type=int, help='The steps of playing')
    args = parser.parse_args()
    rule = args.rule
    steps = args.steps
    # END OF YOUR CODE

    assert 0 <= rule <= 255 and steps >= 0
    generate(rule, steps)