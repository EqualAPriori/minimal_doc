# Using pdoc3
[pdoc3](https://github.com/pdoc3/pdoc) is a really simple documentation generator and viewer with minimal setup. It is great, example for browsing code that you haven't fully set up documentation for yet, although it also can generate functional web pages that you can host if the project is not too extensive. See [here](https://pdoc3.github.io/pdoc/doc/pdoc/) for an example.

## Getting started
Install:

    `pip install pdoc3`

Note that `pdoc3` is only for python 3.6+, so it can only document python code that is useable in python 3.6+.

## Locally browsing code
Simply point your terminal to the directory where your code is. For example, in this repository navigate to `src/module`, where there is a file `module1.py`:

```python
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
```

In the directory, simply do:

    `pdoc -d google --math module1`

This starts a live web server at the localhost:8080 port. You can now open that page in your browser! There's even a search function. 
The flag `-d google` means to use google docstring format (the default is markdown, and pdocs also supports numpy and rst docstrings). 
The `--math` flag turns on latex rendering. In the docstrings `pdoc3` also knows how to read code blocks, etc.


Of course, in the `src` directory you can also directly do:

    `pdoc -d google --math ./*

to document all modules inside `src`.


# Making webpage
The command to use is:

    `pdoc -d google --math -o ../html ./*`

This puts html files in a `../html` folder above the current `src` directory. For further discussion, see [here](https://github.com/pdoc3/pdoc/issues/55).

To host, the cleanest way is to make a new (empty) branch and copy the contents of the `html` directory and put it into the `docs` directory of the new branch. Then, see the [hosting guide](hosting.md) about configuring github to know which branch and directory you want to host as your repository's page.

## More
To see all the command line commands, simply type in

    `pdoc --help`

to see all the options.

If you have nested submodules, make sure that all the modules are ***importable***. One hack is to add

```python
import sys,os
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)))
```
to the `__init__.py` in submodule directories.
