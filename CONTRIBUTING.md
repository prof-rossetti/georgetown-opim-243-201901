# Contributor's Guide

Anyone with a GitHub account can propose changes to files in this repository. This document describes instructions and best practices for contributing to this repository. If you are a student unfamiliar with Git and GitHub, please consult the [official Git guides](https://guides.github.com/) or the [professor's Git notes](/notes/git.md), or ask the professor for a crash course.

## Step 1: Fork the Repository

Fork the course repository via the GitHub.com online interface to create a copy under the ownership of your own GitHub user. After doing so, you should be able to view your fork online at `https://github.com/YOUR_GITHUB_USERNAME/georgetown-opim-243-201901`.

### Refreshing your Fork

If you have previously forked the course repository and now your fork is out of date / behind the "upstream" course repository, then follow these steps to **refresh your fork** from the command-line (Terminal or Git Bash):

```sh
git branch # make sure you are on the "master" branch

git remote -v # make sure you see both "upstream" and "origin" remote addresses

git fetch # detect changes in the "upstream" course repository

git pull upstream master # override your local fork to reflect the contents of the "upstream" repository

git push origin master # override your remote fork to reflect the contents of the "upstream" repository
```

> NOTE: after fetching, if you see conflicts when you pull or push, run: `git reset --hard upstream master` to do a hard reset.

> WARNING: refreshing your fork will delete any previous changes you have committed there that aren't reflected in the "upstream" course repository. So make sure any outstanding Pull Requests have been merged before refreshing your fork!


## Step 2: Revise File Contents

To revise content, navigate to a file in your forked repository via the GitHub.com online interface, then click the "pencil" icon to reveal an online text editor. When done editing a file, "commit" to save the changes. After doing so, you should be able to view your changes reflected online in your own fork.

> NOTE: Most files in this repository are written in a syntax called Markdown. For reference, see this [Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).

## Step 3: Submit a Pull Request

After your fork contains the changes you'd like to be included in the course repository, navigate to the original course repository and create a Pull Request (PR) using the GitHub.com online interface. In the PR message, describe what changes you made and why.

An instructor should review your PR within a timely manner. If the instructor accepts your changes, the instructor will merge them into the course repository's master branch, at which point you should be able to view your changes reflected in the course repository. Else if there are issues with the submission, the instructor should provide further instruction by commenting on the PR, and may close it.

Congratulations! :clap: Thanks! :pray:
