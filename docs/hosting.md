# Hosting

Easy way
Github pages is the easiest way to host your documentation.

After syncing your local repository with a github.com repository, you can now type:

    `mkdocs gh-deploy --force`

This builds, compiles the page, and pushes to a `gh-pages` repository on your online repository.

Afterwards, on your github repository page, go to:

    `settings > pages`

Using the above standard compilation process, you should see that under "source", github knows to use the `gh-pages` repository. For other projects, you can also use other arbitrary branches, oftentimes putting the markdown or html pages in a docs folder, which you can also set from the settings > pages admin page.

Your page will now be hosted at https://YOUR-USERNAME.github.io/REPOSITORY-NAME/

For example, this tutorial is hosted at https://equalapriori.github.io/minimal_doc/.

