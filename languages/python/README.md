# Launchpad: languages/python

**Contents**
  * [Installation](.\installation.md)
  * [Language](#Language)
  * [Python Tools](#Install-Python-Tools)
    * [pip](#pip)    
    * [pip-tools](#pip-tools)
    * [pipx](#pipx)
    * [virtualenv](#virtualenv)
    * [virtualenvwrapper](#virtualenvwrapper)
  * [Command Reference](#Command-Reference])
  * [Resources](#Resources)


# Language 
## Resources
  * [Python3 Cheatsheet](https://www.pythoncheatsheet.org/)


</br> 

# Tools 
## miniconda
### Commands
  * [miniconda commands](https://gist.github.com/nuhil/8f69478591b3abf29b782b4f315537f0)
</br> 

## pip
### Commands
* `pip freeze --local > requirements.txt` - Export all local packages
* `pip install --upgrade pip` - Upgraded pip
* `pip install -r requirements.txt` - Install dependencies listed in requirements.txt
### Related Info
  * [How to install pip on Ubuntu](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/#:~:text=To%20install%20pip%20for%20Python%203%20on%20%3Cu%3EUbuntu%3C%2Fu%3E,verify%20the%20installation%20by%20checking%20the%20pip%20version%3A)

</br> 

## pip-tools
[pip-tools](https://github.com/jazzband/pip-tools)   
</br> 

## pipx 
[pipx](https://pypa.github.io/pipx/) - a tool for installing end-user python applications in isolatd environments
### Install
     ```
     python -m pip install --user pipx
     ```
     cd to the folder identified in the WARNING message and run
     ```
     pipx ensurepath
     ```
     start a new shell
### Commands
  * `pipx install` _package_ - Install a new package
  * `pipx upgrade` _package_ - Upgrade package
  * `pipx upgrade-all` - Upgrade all packages
  * `pipx list` - List all packages
  * `pipx run` _package_ - temporarely downloads _package_ and runs it

</br> 

## virtualenv 
### Commands commans 
  * `python -m virtualenv` _venv_ - Create virtual environent `venv`
  * `.\venv\Scripts\activate` - Activate the virual environment
  * `.\venv\Scripts\deactivate` - Deactivate the virual environment
  * `pip install virtualenv`
  * `virtual env -p usr/bin/python2.6` - Create a virtual environment using a specified python version
  * [How to use virtualenv with Python](https://learnpython.com/blog/how-to-use-virtualenv-python/)
  * [Python tools for managing virtual envs](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
  * [A complete guide to Python virtual envs](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/ )
### Related Information
  * [Python Tools for Managing Virtual Environments](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
</br>

## virtualenvwrapper 
### Commands
  * `mkvirtualenv` _env_ - Create virtual environment _env_
  * `lsvirtualenv` - List virtual envs
  * `showvirtualevn` _env_ - Show details of _env_
  * `workon` [ _env_ ] - Work on the specified virutal env
  * `deactivate` - Deactivate current environment (use system python)
  * [virtualenvwrapper commands](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#:~:text=Managing%20Environments%20%C2%B6%201%20mkvirtualenv%20%C2%B6%20Create%20a,existing%20virtualenv%20environment.%20...%207%20allvirtualenv%20%C2%B6%20)
  * [AttributeError: module ‘virtualenv.create.via_global_ref.builtin.cpython.mac_os’ has no attribute](https://techoverflow.net/2022/02/03/how-to-fix-tox-attributeerror-module-virtualenv-create-via_global_ref-builtin-cpython-mac_os-has-no-attribute-cpython2macosarmframework/)
</br>

## Related Info
  * Setting Up Python Projects by Johannes Schmidt, 2022-10 ([gitrepo](github.com/johschmidt42/python-project-johannes))
    * [GitHub and IDE](https://johschmidt42.medium.com/setting-up-python-projects-part-i-408603868c08)
    * [Formatting and linting](https://johschmidt42.medium.com/setting-up-python-projects-part-ii-c4bd84b709d1)
    * [Testing](https://johschmidt42.medium.com/setting-up-python-projects-part-iii-56aafde8ae0b)
    * [Documentation and CI/CD](https://johschmidt42.medium.com/setting-up-python-projects-part-iv-82059eba4ca4)
    * [Versioning and Releasing](https://johschmidt42.medium.com/setting-up-python-projects-part-v-206df3c1e3d3)
  


