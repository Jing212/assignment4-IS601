"""Arithmetic operations module."""

class Operation:

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Adds two floating-point numbers and returns the result.

        **Parameters:**
        - `a (float)`: The first number to add.
        - `b (float)`: The second number to add.
        
        **Returns:**
        - `float`: The sum of `a` and `b`.

        """
        return a + b  # Performs addition of two numbers and returns the result.
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Subtracts the second floating-point number from the first and returns the result.

        **Parameters:**
        - `a (float)`: The number from which to subtract.
        - `b (float)`: The number to subtract.
        
        **Returns:**
        - `float`: The difference between `a` and `b`.

        """
        return a - b  # Subtracts the second number from the first and returns the difference.
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Multiplies two floating-point numbers and returns the product.

        **Parameters:**
        - `a (float)`: The first number to multiply.
        - `b (float)`: The second number to multiply.
        
        **Returns:**
        - `float`: The product of `a` and `b`.
        
        """
        return a * b  # Multiplies the two numbers and returns the product.
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Divides the first floating-point number by the second and returns the quotient.

        **Parameters:**
        - `a (float)`: The dividend.
        - `b (float)`: The divisor.
        
        **Returns:**
        - `float`: The quotient of `a` divided by `b`.

        **Raises:**
        - `ValueError`: If the divisor `b` is zero, as division by zero is undefined.

        **Example:**
        >>> Operation.division(10.0, 2.0)
        5.0
        >>> Operation.division(10.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: Division by zero is not allowed.

        **Error Handling:**
        - Division requires extra error handling to prevent division by zero, which 
          would cause a runtime error. Here, we check if `b` is zero and raise a 
          `ValueError` with a descriptive message if it is.
        
        """
        if b == 0:
            # Checks if the divisor is zero to prevent undefined division.
            raise ValueError("Division by zero is not allowed.")  # Raises an error if division by zero is attempted.
        return a / b  # Divides `a` by `b` and returns the quotient.