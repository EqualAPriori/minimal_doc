# WELCOME
Here we provide short tutorials on generating documentation, with the templates and coded provided in this tutorial repository.

1. using [markdown](markdown.md)
    e.g. in `README.md` in a github repository
2. using [docstrings](docstrings.md)
3. using [pdoc3](pdoc3.md)
4. using [mkdocs](mkdocs.md)
5. [hosting](hosting.md)


Some examples of documented code:

- [mdtraj](https://www.mdtraj.org/1.9.8.dev0/index.html):
    - Uses `sphinx` with `ReadTheDocs` theme. Note the "view page source" link on the top right of the page, which shows the reStructuredText used to write the page.
- [scikitlearn](https://scikit-learn.org/stable/modules/classes.html)
    - the "view page source" is on the bottom left of the page
- [mkdocstrings](https://mkdocstrings.github.io/reference/extension/)
    - using a newer standard called `mkdocs` that is markdown-native, and the `material` theme.
- [pdoc3](https://pdoc3.github.io/pdoc/doc/pdoc/#gsc.tab=0) 
    - a lightweight document generation, with no set up files! 
    - can be more heavily themed, e.g. see the [hikari](https://www.hikari-py.dev/hikari/) project.
