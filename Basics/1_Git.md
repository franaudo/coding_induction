# Git workflow

## Getting started with git

> **NOTE**: you neeed to have `git` on your machine. if you don't have it already, you can install it from: <https://git-scm.com/download/win>

With the following steps you can `clone` the repository:

0. Open the `terminal` and navigate to the folder where you want to `clone` the repo
1. `clone` the repository entering `git clone https://github.com/franaudo/teaching_template.git`
2. type `cd teaching_template` to change directory

Once you have cloned the repo, you can use the following commands to interact with it:

[<img src="https://i.redd.it/8341g68g1v7y.png">](https://i.redd.it/8341g68g1v7y.png)

However, you will probably not need many of these commands in a day-to-day scenario.

### Top 5 commands

0. `git fetch` -> get the latest changes without merging
1. `git pull` -> get the latest changes and merge them
2. `git status` -> check if there are changes to the repo
3. `git add .` -> stage all the changes
4. `git commit -am "\<message>"` -> commit all staged changes (save the status of the repo at that time)
5. `git push` -> send the you commits to the origin

### Working with branches

0. `git branch` -> show a list of all the branches in the local repository
1. `git branch -a` -> show a list of all the branches (local and remote)
2. `git branch <name-of-the-new-branch>` -> create a new branch
3. `git checkout <name-of-the-new-branch>` -> switch to the given branch
4. `git push origin <name-of-the-new-branch>` -> pushes the new branch on the remote and links it your local branch

### Working with forks

Forks are not really a `git` concept, but they were introduced by `GitHub` and now are basically implemented by every repo hosting provider.
A `fork` is basically a *special* clone of the repository: when you create a `fork`, a new repository is created in your GitHub account, which is linked to the main one. You have now full control of this repository (your are the admin), but you can still see if changes are made in the main repo and in case sync this changes with your version. Most importantly, you can chage the code yourself without interfering with other people work.

These are the most useful commands when dealing with forks:

0. `git remote -v` -> List the current configured remote repository for your fork.
1. `git remote add upstream <https://user@github.com/main-repository-address>` -> adds a pointer to the main repository so you can do all the `reading` operations you would normally do with your own repository (fetch and pull).
2. `git fetch upstream` -> Fetch the branches and their respective commits from the upstream repository
3. `git pull upstream <branch>` -> merge the latest changes from the main repo

However, at some point you might want to merge your code into the main repository. This is done creating a so called `pull request`. I have always found this name confusing and I usually think of it as a `merge request`: you are asking the main developer to review your code and merge it into the main repository.

You can create `pull requests` directly from GitHub: <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork>

## Git tools

Even though learning the basic CLI commands can be extremelly usefull, when things get complicated (merging, resolving conflicts, visualising the log history, etc.) it is a good idea to use external tools designed to work with git.

Here, I suggest two main tools, but many are available and in the end is a metter of preference.

### GitKraken

This software is free to use for public repos for everyone. For students and university members the pro version is available for free, which allows to use its functionalities also for private repos.

You can download the software here: <https://www.gitkraken.com/download>

On the website there are plenty of videos that explain the software and git concepts in general, which I strongly reccomend to watch.

[<img src="https://www.gitkraken.com/img/index/gk-product-2.png">](GitKraken)

### vscode

In vscode git is already integrated, but I suggest to enhance the basic functionalities with the `gitgraph` extension <https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph>

[<img src="https://github.com/mhutchie/vscode-git-graph/raw/master/resources/demo.gif">](git_graph)
