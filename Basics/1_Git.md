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

## Top 5 commands

0. `git fetch` -> get the latest changes without merging
1. `git pull` -> get the latest changes and merge them
2. `git status` -> check if there are changes to the repo
3. `git add .` -> stage all the changes
4. `git commit -am "\<message>"` -> commit all staged changes (save the status of the repo at that time)
5. `git push` -> send the you commits to the origin

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
