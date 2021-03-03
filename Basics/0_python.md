# Python

## Install python

It is best to install python using the `Miniconda` distribution from here <https://docs.conda.io/en/latest/miniconda.html>

This will install python and another important software `conda` , which will be discussed later.

Another option is to install python using `Anaconda` : this will install the same packages as `Miniconda` but also many other scientific libraries that can be useful in an engineering environment. However, it is considerably larger and these libraries can be installed anyways later, so I would not reccomend this option.

To check if python is installed correctly, open the command line and type:

``` bash
>>> python
Python 3.8.8 | packaged by conda-forge | (default, Feb 20 2021, 15:50:08) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

With the command above you launched python, which is now running. You can use alredy its basic functionalities. For example, you can type the following:

``` bash
>>> 1+1
2
>>> print('Ciao mamma!')
Ciao mamma!
>>>
```

### learning python

You won't learn python in a day, forget it! :) However, you should start your journey from somewhere. In general, I think you will mostly learning `by doing` , so having a problem and solving it.

The best way of finding information is to just google it! Usually the best answers are provided by the community ( `stackoverflow` ). I also found these tutorials helpful while learning python: <https://realpython.com/tutorials/basics/>

## vscode

However, using the command line is not very convenient, especially when you want to create complex scripts or even applications. A much better alternative is to use an `Integrated Developement Environment` (or IDE) such as `visual studio code` . There are plently of alternatives, but this is free, open source and very lightweight.

You can download it from: <https://code.visualstudio.com/download>

`vscode` can be used with all programming languages (C++, Java, HTML, etc.), but it also offers specific funcionalities for some common ones, like python. In orde to activate its full potential with python, you have to install the `Python extension` . You can find detail instructions here: <https://code.visualstudio.com/docs/python/python-tutorial>

<img src="https://code.visualstudio.com/assets/docs/python/tutorial/python-extension-marketplace.png">

These intro videos are helpful to get started with vscode: <https://code.visualstudio.com/docs/getstarted/introvideos>

## conda

Python itself is very powerfull, but its true power comes from the additional libraries that expand its core functionalities.

There is an infinite number of libraries for python (and you can make your own!) that change and update all the time, therefore people came up with a system to keep track of them. More than a system, a software: `conda`

`conda` is a so called `package manager` or a `virtual environment manager`: think about a `virtual environment` as a new machine where you have only python on it. Everytime you create a virtual environment, you get a free new machine (nice, no?!) and you can create an infinite number of virtual environments using conda!

A virtual environment or better a `conda enviroment` (same thing, but that's the offical name) can be created  using the command line:

```bash
>>> conda create -n <name-of-your-new-environment>
```

A pratical *cheat sheet* with useful conda commands is available here: <https://www.interactivechaos.com/sites/default/files/data/conda_cheatsheet.pdf>
