def updated_light(current):
    # First, I defined a function to take the current state of the traffic light as input 
    # and return the next state in the sequence.
    # To handle this, I used an if-elif-else structure to check the current state and 
    # determine the next state accordingly.
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        # If the input is not one of the valid states, raise an error to indicate an invalid input.
        raise ValueError("Invalid traffic light state")

# Test cases to verify the function's behavior
# These test cases check whether the light changes correctly from green to yellow, yellow to red, 
# and red back to green.
print(updated_light("green"))   # Output: yellow
print(updated_light("yellow"))  # Output: red
print(updated_light("red"))     # Output: green

# Uncomment the line below to test invalid input handling
# print(updated_light("blue"))  # Should raise ValueError