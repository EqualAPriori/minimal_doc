"""An example module
"""


class A:
    """Simple class containing a variable
    """

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        """For if both objects are of type A
        """
        return self.x * other.x

    def power(self, pow: int = 2):
        """raise to power store, and return.
        Args:
            pow (int)

        Returns:
            (float): self.x ** pow
        """
        self.x *= self.x
        return self.x


class AA(A):
    pass


def mult_A(a1: A, a2: A):
    """Multiplication for A objects.
    computes: 
        $$x_{a1}*x_{a2}$$

    Args:
        a1 (A): instance of `A` class
        a2 (A): instance of `A` class

    Returns:
        float: a1.x * a2.x

    Note:
        programatically this does:
        ```
        a1.x * a2.x
        ```
    """
    return a1.x * a2.x
