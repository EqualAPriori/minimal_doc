# Docstrings
At the minimum, use docstrings to document your code!

It is good to follow standard conventions for docstrings.

## numpy style
One common standard are numpy style docstrings, e.g. used by `numpy` and `scipy`. For full documentation see: [https://numpydoc.readthedocs.io/en/latest/format.html](https://numpydoc.readthedocs.io/en/latest/format.html)

An example:
```python
def f(x,y):
    """Summary of doing something to `x` and `y`

    Parameters
    ----------
    w : int
    x : type
        Description of parameter `x`.
    y 
        Description of parameter `y` (with type not specified).
    z : iterable object


    Returns
    -------
    err_code : int
        Non-zero value indicates error code, or zero on success.
    err_msg : str or None
        Human readable error message, or None on success.

    Notes
    -----
    additional helpful information
    """
    return x + y
```

## google style
For details, see [https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).

Another good guide: [https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

```python
def f(x,y):
    """Summary of doing something to `x` and `y`

    Args:
        w (int)
        x (type):
            Description of parameter `x`.
        y :
            Description of parameter `y` (with type not specified).
        z (iterable object)


    Returns:
        (int): Non-zero value indicates error code, or zero on success.
        (str or None): Human readable error message, or None on success.

    Note:
        additional helpful information
    """
    return x + y
```

Classes can also have an ``Attributes:`` section in their docstring. Attributes can be documented *inline* or *before* variables. But you should stick to one convention or the other.

```python
class A:
    """Summary of class

    Attributes:
        x (int): a number to store in the class.

    Note:
        additional helpful information
    """
    def __init__(self,x:int):
        #: list of int: documentation of attribute
        self.x = [x]
```