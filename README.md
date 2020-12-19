# teaching_template

## Folder Structure

* `_examples`   --> test and example code
* `database`   --> folder containing the data about the slabs
* `queries`    --> here goes the code to generate plots and query the database
* `temp` --> you can create a temp folder where you can dump any sort of files: these will be ignored by git and never pushed in the main repository on GitHub.

---

## How to work with git

> **NOTE**: you neeed to have `git` on your machine. if you don't have it already, you can install it from: <https://git-scm.com/download/win>

With the following steps you can `clone` the repository:

0. Open the `terminal` and navigate to the folder where you want to `clone` the repo
1. `clone` the repository entering `git clone https://github.com/franaudo/PA.git`
2. type `cd PA` to change directory

Once you have cloned the repo, you can use the following commands to interact with it:

[<img src="https://i.redd.it/8341g68g1v7y.png">](https://i.redd.it/8341g68g1v7y.png)

## How to build your documentation with Sphinx

Here you can find detailed info about `sphinx` and how to get started with `rst`: <https://sphinx-tutorial.readthedocs.io/start/>. You probably won't need to do any modification to the source files for the documentation, but it is always good to learn new stuff! ;)

First, you need to install `sphinx` on your conda environment (it doesn't necessarily need to be the same environment that you are using for the develpment, but it is annoying to switch to a different environment every time you want to build your documentation).

In a terminal type:

```bash
conda activate <name-of-your-environment>
conda install sphinx
```

Now that you have `sphinx`, you can build the html files for the documentation any time you make modification to the `docstrings` in your code (the `rst` text part in your code...)

Navigate to the `docs` folder in the repository:

```bash
cd <path-to-main-repository-on-your-machine>/docs
```

and then build the documentation html pages using

```bash
make html
```
