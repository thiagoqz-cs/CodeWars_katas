def boolean_to_string(b):
    """
    I chose to use a dictionary to solve this problem because this kind of 
    data structure allows me to map two different data types easily, making 
    the conversion between them straightforward.
    """
    bol_str = {
        True: "True",
        False: "False"
    }
    return bol_str[b]
