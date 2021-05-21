def print_banner():
    """
    Print the program banner. You may change the banner message.
    """
    # START OF YOUR CODE
    print("""
Welcome to our Python-powered Unit Converter v1.0 by Zhanning Zhang!
You can convert Distances, Weights, Volumes to one another, but only
within units of the same category, which are shown below. E.g.: 1 mi in ft

   Distances: ft cm mm mi m yd km in
   Weights: lb mg kg oz g
   Volumes: floz qt cup mL L gal pint
""")
    # END OF YOUR CODE


def convert(command):
    """
    Handle a SINGLE user input, which given the command, either print
    the conversion result, or print an error, or exit the program.
    Please follow the requirements listed on project website.
    :param command: User input

    >>> convert("1 m in km")
    1 m = 0.001000 km
    """
    # START OF YOUR CODE
    # if command is 'q', then directly quit after a simple ending prompt.
    if command.lower() == 'q':
        print('To say bye is kinda sad, see u next time!')
        exit()

    conversion_table = generateConversionTable()
    base_unit = {'distance': 'm', 'volume': 'm^3', 'weight': 'kg'}
    try:
        structured_input = getStructuredInput(command)  # may raise SyntaxError!
        original_value, original_unit, targe_unit = float(structured_input[0]), structured_input[1], structured_input[3]
        category = getUnitsCategory(structured_input)   # may raise TypeError!
        # The how process of converting can be concluded as
        # Firstly convert original_unit to base unit, then convert base_unit to targe_unit.
        base_value = original_value / conversion_table[category][(base_unit[category], original_unit)]
        target_value = base_value * conversion_table[category][(base_unit[category], targe_unit)]
        # use the initial form of original_value, structured_input[0]
        result = '{} {} = {:.6f} {}'.format(structured_input[0], original_unit, target_value, targe_unit)
        print(result)
    except SyntaxError:
        pass
    except TypeError:
        pass
    # END OF YOUR CODE


# TODO: Add Other Functions Here
import re
def generateConversionTable():
    '''
    description: To create a dictionary that store the conversion table.

    :return conversion_table: like its literal meaning.
                              And You can know 1 m equals to how many km by enter
                                    conversion_table['distance'][('m', 'km')]
                              The direction is m->km.
    '''
    # build converter separately
    def buildConverter(public_unit, units, data):
        '''
        description: Build a converter of a particular category. The converter is in dictionary type
                     The structure of element in converter, take category distance for example, is like somehow below
                            converter['m', 'ft'] = [3.2808399, 0.304799999536704]
                     Given that a conversion is directed, the value [3.2808399, 0.304799999536704] means that
                            1 m = 3.2808399 ft and 1 ft = 0.304799999536704 m
        
        :param public_unit: a common, base unit that other units use this base unit to convert from each other
        :param units: all units that from a particular category
        :param data: stores conversion data
        
        :return converter: a converter of particular category
        '''
        converter = {}
        i = 0
        for ele in zip([public_unit for i in range(len(units))], units):
            converter[tuple(ele)] = data[i]
            i += 1
        return converter
    
    distance_units = ('m', 'cm', 'mm', 'km', 'in', 'ft', 'yd', 'mi')
    distance_conversion_data = [1, 100, 1000, 0.001, 39.3700787, 3.280839895, 1.0936133, 0.000621371192]
    distance_converter = buildConverter('m', distance_units, distance_conversion_data)

    volume_units = ('L', 'mL', 'floz', 'cup', 'pint', 'qt', 'gal')
    volume_conversion_data = [1000, 1000000, 33814.0227, 4226.75284, 2113.37642, 1056.68821, 264.172052]
    volume_converter = buildConverter('m^3', volume_units, volume_conversion_data)

    weight_units = ('g', 'kg', 'mg', 'oz', 'lb')
    weight_conversion_data = [1000, 1, 1000000, 35.2739619, 2.20462262]
    weight_converter = buildConverter('kg', weight_units, weight_conversion_data)
    
    convertion_table = {'distance': distance_converter, 'volume': volume_converter, 'weight': weight_converter}
    return convertion_table


def getStructuredInput(cmd):
    '''
    description: First provide a reasonable way to check whether user input is fit in expected form of input.
                 If user input is valid, then the function transform it into a tuple which separately stores key data.
    
    :param cmd: The user input (string)
    
    :return structured_cmd/None: a tuple that contains key information. (tuple)/Or none.
    
    >>> getStructuredInput('123.456789 kg in mg')
    ('123.456789', 'kg', 'in', 'mg')
    '''
    regex = re.compile('([0-9]+.?[0-9]*) ([a-zA-Z]+) (in) ([a-zA-Z]+)')
    if regex.fullmatch(cmd):
        return regex.search(cmd).groups()
    else:
        print('Error: Invalid input, the proper input should looks like below'
              '\n', 
              '       "10 mi in m"', 
              sep='')
        raise SyntaxError


def getUnitsCategory(structured_input):
    '''
    description: To gain units for converting from structured input.
                 If two units can be converted from one to another, return their category.
                 If not, report(print) an error message.

    :param structured_input: a tuple containing key information. (tuple)
    
    :return common_category/None: the particular category that two units belong to. (string)/Or none.
    '''
    units_table = [{'distance': ('m', 'cm', 'mm', 'km', 'in', 'ft', 'yd', 'mi')}, 
                   {'volume': ('L', 'mL', 'floz', 'cup', 'pint', 'qt', 'gal')}, 
                   {'weight': ('g', 'kg', 'mg', 'oz', 'lb')}]
    unit_1 = structured_input[1]
    unit_2 = structured_input[3]
    unit1_searched = False
    for units in units_table:
        if unit_1 in list(units.values())[0]:
            unit1_searched = True
            if unit_2 in list(units.values())[0]:
                return list(units.keys())[0]
            else:
                print('Error: Units dismatch, please confirm the unit that the unit you want to convert is the same type with original unit!')
                raise TypeError
    # consider that unit1 is invalid
    if not unit1_searched:
        print('Error: Invalid units, please check the unit you entered is legal!')
        raise TypeError


###########################################
# DO NOT MODIFY ANYTHING BELOW
###########################################

def get_user_input():
    """
    Print the prompt and wait for user input
    :return: User input
    """
    return input("Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]: ")


if __name__ == '__main__':
    print_banner()
    while True:
        command = get_user_input()
        convert(command)
