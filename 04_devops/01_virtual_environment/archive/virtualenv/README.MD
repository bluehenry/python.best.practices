# Get Start
[Reference](https://segmentfault.com/a/1190000014935970)
## virtualenvwrapper install
```
$ sudo pip3 install virtualenvwrapper
$ mkdir -p ~/Envs
```
## vim ~/.bash_profile
```
export WORKON_HOME=~/Envs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
## create virtual env
```
mkvirtualenv name --python=python3
```
## install all packages
```
pip3 install -r requirements.txt
```
## if install new package not in requirements.txt
```
pip3 freeze > requirements.txt
```
## open virtualenv
```
workon name
```
## close virtualenv
```
deactivate
```
## Run command to use githook
```
git config core.hooksPath .githook
```

## Create requirements.txt
If you use virtual environment
```bash
pip3 freeze > requirements.txt
```