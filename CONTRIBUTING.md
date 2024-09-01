# Contributing to AI Trading Bot - Machine Learning Service

First off, thank you for considering contributing to the AI Trading Bot project! It's people like you that make it such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/aakash-priyadarshi/Trading-bot-model/issues) page to see if someone else has already created a ticket. If not, go ahead and [make one](https://github.com/aakash-priyadarshi/Trading-bot-model/issues/new)!

## Fork & create a branch

If this is something you think you can fix, then [fork the Trading Bot Model repo](https://help.github.com/articles/fork-a-repo) and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```sh
git checkout -b 325-improve-prediction-accuracy
```

## Set up your environment

Make sure you have Python 3.8+ installed. Then set up your environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Get the test suite running

Now you should be able to run the entire test suite using:

```sh
python -m pytest
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## View your changes in action

Start the Flask application:

```sh
python predict.py
```

## Get the style right

Your patch should follow the same coding conventions & pass the same code quality checks as the rest of the project. We use `flake8` for style checking:

```sh
flake8 .
```

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with the latest Trading Bot Model master branch:

```sh
git remote add upstream git@github.com:aakash-priyadarshi/Trading-bot-model.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local master, and push it!

```sh
git checkout 325-improve-prediction-accuracy
git rebase master
git push --set-upstream origin 325-improve-prediction-accuracy
```

Finally, go to GitHub and [make a Pull Request](https://help.github.com/articles/creating-a-pull-request) 😄

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) [resources](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) but here's the suggested workflow:

```sh
git checkout 325-improve-prediction-accuracy
git pull --rebase upstream master
git push --force-with-lease 325-improve-prediction-accuracy
```

## Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

* It is passing CI.
* It has been approved by at least two maintainers. If it was a maintainer who opened the PR, only one extra approval is needed.
* It has no requested changes.
* It is up to date with current master.

Any maintainer is allowed to merge a PR if all of these conditions are met.
