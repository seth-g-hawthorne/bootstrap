# Launchpad: languages/python

**Contents**
  * [Windows Installation](#Windows-Installation)
  * [Linux Installation](#Linux-Installation)
  * [Install Python Tools](#Install-Python-Tools)
  * [Command Reference](#Command-Reference])
  * [Resources](#Resources)

___
# Windows Installation

  1. Download Python Windows installer from: https://www.python.org/

  1. If pip is not installed, install it manually
     ```
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     python get-pip.py
     pip --version
     ```

  1. Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
     ```
     python -m pip install --user virtualenv
     ```

  1. Optionally install [virtualenv-wrapper-env](https://pypi.org/project/virtualenvwrapper-win/)

  1. Optionally install [miniconda](https://docs.conda.io/en/latest/miniconda.html) - A minimal installer for the Python conda environment, used for scientific computing

## Resources
  1. https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/ 


# Linux Installation
  1. Check if python is installed
     ```
     python3 --version
     ```

  1. If not
     ```
     sudo apt update
     sudo apt install python3-pip
     pip completion --bash >> ~/.bashrc
     source ~/.bashrc 
     ```

  1. Install virtualenv 
     ```
     sudo apt install virtualenv
     ```

  1. Install [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)
    ```
     sudo apt install virtualenvwrapper
     echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
     export WORKON_HOME=~/.virtualenvs
     mkdir $WORKON_HOME
     echo "export WORKON_HOME=$WORKON_HOME" >> ~/.bashrc
     echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.bashrc 
     source ~/.bashrc 
     ```

  1. Optionally install [miniconda](https://www.jamesbower.com/how-to-install-conda-and-miniconda3-on-ubuntu-22-04-lts/) - A minimal installer for the Python conda environment, used for scientific computing
  ```
  wget https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh
  chmod +x Miniconda3-py310_22.11.1-1-Linux-x86_64.sh
  Miniconda3-py310_22.11.1-1-Linux-x86_64.sh
  export PATH=/home/ubuntu/miniconda3/bin/:$PATH
  ```


## Resources
  * [How to install pip on Ubuntu](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/#:~:text=To%20install%20pip%20for%20Python%203%20on%20%3Cu%3EUbuntu%3C%2Fu%3E,verify%20the%20installation%20by%20checking%20the%20pip%20version%3A)
  * Setting Up Python Projects by Johannes Schmidt, 2022-10 ([gitrepo](github.com/johschmidt42/python-project-johannes))
    * [GitHub and IDE](https://johschmidt42.medium.com/setting-up-python-projects-part-i-408603868c08)
    * [Formatting and linting](https://johschmidt42.medium.com/setting-up-python-projects-part-ii-c4bd84b709d1)
    * [Testing](https://johschmidt42.medium.com/setting-up-python-projects-part-iii-56aafde8ae0b)
    * [Documentation and CI/CD](https://johschmidt42.medium.com/setting-up-python-projects-part-iv-82059eba4ca4)
    * [Versioning and Releasing](https://johschmidt42.medium.com/setting-up-python-projects-part-v-206df3c1e3d3)
  

# Install Python Tools
  * Upgrade pip
    ```
    pip install --upgrade pip
    ```


  * [pipx](https://pypa.github.io/pipx/) - a tool for installing end-user python applications in isolatd environments
     ```
     python -m pip install --user pipx
     ```
     cd to the folder identified in the WARNING message and run
     ```
     pipx ensurepath
     ```
     start a new shell


  * [pip-tools](https://github.com/jazzband/pip-tools)   


# Command Reference

## miniconda commands
  * [miniconda commands](https://gist.github.com/nuhil/8f69478591b3abf29b782b4f315537f0)

## pip commands 
* `pip freeze --local > requirements.txt` - Export all local packages

## pipx commands 
  * `pipx install` _package_ - Install a new package
  * `pipx upgrade` _package_ - Upgrade package
  * `pipx upgrade-all` - Upgrade all packages
  * `pipx list` - List all packages
  * `pipx run` _package_ - temporarely downloads _package_ and runs it

## virtualenv commands 
  * `python -m virtualenv` _venv_ - Create virtual environent `venv`
  * `.\venv\Scripts\activate` - Activate the virual environment
  * `.\venv\Scripts\deactivate` - Deactivate the virual environment
  * `pip install virtualenv`
  * `virtual env -p usr/bin/python2.6` - Create a virtual environment using a specified python version
  * [How to use virtualenv with Python](https://learnpython.com/blog/how-to-use-virtualenv-python/)
  * [Python tools for managing virtual envs](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
  * [A complete guide to Python virtual envs](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/ )

## virtualenvwrapper commands
  * `mkvirtualenv` _env_ - Create virtual environment _env_
  * `lsvirtualenv` - List virtual envs
  * `showvirtualevn` _env_ - Show details of _env_
  * `workon` [ _env_ ] - Work on the specified virutal env
  * `deactivate` - Deactivate current environment (use system python)
  * [virtualenvwrapper commands](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#:~:text=Managing%20Environments%20%C2%B6%201%20mkvirtualenv%20%C2%B6%20Create%20a,existing%20virtualenv%20environment.%20...%207%20allvirtualenv%20%C2%B6%20)
  * [AttributeError: module ‘virtualenv.create.via_global_ref.builtin.cpython.mac_os’ has no attribute](https://techoverflow.net/2022/02/03/how-to-fix-tox-attributeerror-module-virtualenv-create-via_global_ref-builtin-cpython-mac_os-has-no-attribute-cpython2macosarmframework/)


# Resources
  * [Python Tools for Managing Virtual Environments](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)