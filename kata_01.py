import math  # First, I imported the math module to access
# the `.floor` method, which rounds down the number of litres.

def litres(time):  # Next, I created a function to calculate the total
    # litres of water Nathan will drink. The parameter `time` is used
    # as an input variable for the number of hours Nathan cycles.
    return math.floor(time * 0.5)  # Here, I created a basic formula
    # to calculate the total litres of water. I used the `.floor` method
    # to round down the result. Finally, I used `return` to output the value.

# Test cases to verify the solution
print(litres(3))     # Output: 1
print(litres(6.7))   # Output: 3
print(litres(11.8))  # Output: 5