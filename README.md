# Targaryen

A distributed computing framework, written in python. This is in no way
"perfect" and is a work in progress. The name draws inspiration from the
Targaryen Sigil, a three headed dragon. This is the result of watching too much
Game of Thrones. Inspiration for the actual project was taken from
[bashmu](https://github.com/renmusxd/bashmu)

## Installation

```shell
virtualenv -p python3 <virtualenv_name>
cd <virtualenv_name>
. bin/activate
git clone https://github.com/MattLombana/Targaryen
cd Targaryen
pip3 install -Ur requirements.txt
```

Make sure to replace `<virtualenv_name>` with a name for your virtual
environment. I like to use Targaryen-virt

## Configuration

There are several files to configure before Targaryen can be run. They are:

* machines.local.yml

```shell
cp conf/machines.yml conf/machines.local.yml
vim conf/machines.local.yml
```

### [machines.local.yml](./targaryen/conf/machines.yml)

Machine specifications should be placed in here. machines.yml is a template,
and configurations will be loaded from machines.local.yml before being loaded
from machines.yml
Any files with *.local.* in the filename will be ignored.

## Running Targaryen

Coming Soon!

## Contributing to Targaryen

Right now, there's not much to do, as I haven't really done anything.
Under the projects tab, the various projects and the TODO's associated
with them can be found. If you want something to be done, create an issue.

If you find a bug, please create an issue and apply one or more appropriate labels.
