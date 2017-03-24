# Targaryen

A distributed computing framework, written in python. This is in no way
"perfect" and is a work in progress. The name draws inspiration from the
Targaryen Sigil, a three headed dragon. This is the result of watching too much
Game of Thrones. Inspiration for the actual project was taken from
[bashmu](https://github.com/renmusxd/bashmu)

## Installation

```shell
virtualenv <virtualenv_name>
cd Targaryen
git clone https://github.com/MattLombana/Targaryen
cd Targaryen
pip3 install -Ur requirements.txt
```

Make sure to replace `<virtualenv_name>` with your actual name. I like to use Targaryen-virt

## Configuration

There are several files to configure before Targaryen can be run. They are:

* machines.local.yml

```shell
cp machines.yml machines.local.yml
vim machines.local.yml
```

### [machines.local.yml](./conig/machines.yml)

Machine specifications should be placed in here. machines.yml is a template,
and configurations will be loaded from machines.local.yml before being loaded
from machines.yml
Any files with *.local.* in the filename will be ignored.

## Running Targaryen

Coming Soon!
