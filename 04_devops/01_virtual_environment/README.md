# Python Virtual Environment TOols
## virtualenv/virtualenvwrapper
* Recommend

## vene
* It is not for Python versions before 3.3
* Recommend 
```
python3 -m venv tutorial-env
```
On Windows, run:
```
tutorial-env\Scripts\activate.bat
```
On Unix or MacOS, run:
```
source tutorial-env/bin/activate
```

## Andconda's conda
* Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more

## pyenv
* Simple Python Version Management
* There is a pyenv plugin named pyenv-virtualenv which comes with various features to help pyenv users to manage virtual environments created by virtualenv or Anaconda

## poetry
* Dependency Management for Python
* poetry will also detect if you are inside a virtualenv and install the packages accordingly. So, poetry can be installed globally and used everywhere.

## pipenv
* Don't recommend. 
* Since pipenv doesn’t seem to be further developed

## pew 
* Don't recommend
* The main problem that I noticed is that its support is very limited now. The last commit on the code is from March 2018, which is almost a year old.