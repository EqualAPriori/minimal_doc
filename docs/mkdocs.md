#MkDocs
Quick start guide for using MkDocs.

##Installing
Several packages are used in this package. They can be installed via

    `pip install -r requirements.txt`

Or you can manually install the following packages:

1. mkdocs
2. mkdocs-material
3. mkdocs-jupyter
4. mkdocstrings
5. mkdocs-literate-nav
6. mkdocs-gen-files
7. pymdown-extensions

The template for this repository can [downloaded](https://github.com/EqualAPriori/minimal_doc/).

If you don't want to use the template in this repository, the first time you get started do:

    `mkdocs new .`

This gives you the ABSOLUTE minimum mkdocs setup, with an empty mkdocs.yml file.

## Documentation organization and writing
The `mkdocs.yml` contains all the settings, such as the github repository, the site name, themes, extensions, plugins, and included pages.

Most important are the following two sections:

```yaml
site_name: Documentation tutorials
site_description: "Example documented repo"
site_url: "https://equalapriori.github.io/minimal_doc"
repo_url: "https://github.com/EqualAPriori/minimal_doc"
repo_name: "minimal_doc"
site_dir: "site"
```

and

```yaml
nav:
    - "Home": index.md
    - "markdown": markdown.md
    - "docstrings": docstrings.md
    - "pdoc3": pdoc3.md
    - "mkdocs": mkdocs.md
    - "Reference": 
        - "At a glance": reference/ToC.md
        - "Src": reference/
```

which outlines the top-level sections and pages of the site. The template starts out with no pages, but in the example branch of the repository you'll see that there already exist some pages that you can browse.

The auto-documentation API generator assumes that modules are in the `src` directory. Either 1) use a `setup.py -e` install so that your python package can find the code and modules, or 2) manually add the `src` directory to your Python PATH so that the modules within are discoverable.

The API documentation is always the most finicky to setup -- hopefully the template in this repository gets you going automatically.

One weird quirk of the `material` theme for mkdocs is that the sidebar navigation is only properly generated for only one top-level heading `#`. This is part of the html standard that they follow.

## Running
After adding your own pages and files, you can now see your site! Run the following commands in the root of the repository, where the `mkdocs.yml` file is.

1. To serve locally:

    `mkdocs serve`

2. To make the html pages locally:
 
    `mkdocs build`

3. To push to github (see next page for details on setting this up):

    `mkdocs gh-deploy`