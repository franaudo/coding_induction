# How to build your documentation with Sphinx [WIP]

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
