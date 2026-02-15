## problem no: 2 -- Reverse Integer

def reverse_integer(n):
    """Reverse a 32-bit signed integer.

    Parameters
    - n (int): The integer to reverse. Can be positive or negative.

    Returns
    - int: The reversed integer. If the input (as currently implemented)
      falls outside the 32-bit signed integer range, the function
      sets the result to -1.

    Behavior & Notes
    - The function converts the absolute value of `n` to a string,
      reverses that string, converts it back to an integer, and restores
      the sign for negative inputs.
    - The current implementation checks the input `n` against the
      32-bit signed integer bounds and assigns `-1` to the result when
      `n` is out of range. (This means very large inputs are flagged
      before reversing.)
    - Examples:
        - `reverse_integer(123)` -> `321`
        - `reverse_integer(-120)` -> `-21`
        - If `n` is outside [-2**31, 2**31], the function returns `-1`.

    Complexity
    - Time: O(d) where d is the number of digits in `n` (string reversal).
    - Space: O(d) for the string conversion.

    """
    if(n >0):
        result = int(str(n)[::-1])
    else:
        result = int(str(abs(n))[::-1])
    
    if(n < -2**31 or n > 2**31):
        result = -1
    
    return result


print(reverse_integer(143))