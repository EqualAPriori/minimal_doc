# Hosting

## Easy way
Github pages is the easiest way to host your documentation.

After syncing your local repository with a github.com repository, you can now type:

    `mkdocs gh-deploy --force`

This builds, compiles the page, and pushes to a `gh-pages` repository on your online repository.

Afterwards, on your github repository page, go to:

    `settings > pages`

Using the above standard compilation process, you should see that under "source", github knows to use the `gh-pages` repository. 

Your page will now be hosted at https://YOUR-USERNAME.github.io/REPOSITORY-NAME/

For example, this tutorial is hosted at https://equalapriori.github.io/minimal_doc/.

## Manual way
For other projects, you can also use other arbitrary branches, oftentimes putting the markdown or html pages in a docs folder, which you can also set from the settings > pages admin page. 

Alternatively, you can use 

    `mkdocs build`

To build the html files, and then save them in the appropriate branch/directory you want to host from. However, since `mkdocs` expects markdown files in the `docs` folder, it is probably cleanest to put the html files in a new branch instead of the one you are building from.

Similarly, this repository can also be configured to host html pages generated from `pdoc3`. For an example, for this repository the github page source can be set to the `pdoc3` branch's `docs` directory.
