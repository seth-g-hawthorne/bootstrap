# Launchpad: languages/python installation

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