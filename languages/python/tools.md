# Launchpad: languages/python tools

**Contents**
<!-- vscode-markdown-toc -->
* [Summary](#Summary)
* [pip](#pip)
	* [Commands](#Commands)
	* [Related Info](#RelatedInfo)
* [pipx](#pipx)
	* [Install](#Install)
	* [Commands](#Commands-1)
* [virtualenv](#virtualenv)
	* [Commands](#Commands-1)
	* [Related Information](#RelatedInformation)
* [virtualenvwrapper](#virtualenvwrapper)
	* [Commands](#Commands-1)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
</br>

## <a name='Summary'></a>Summary 
|   | **Tool** | **Description** |
| - | ----------- | --------------- |
| * | [black](https://black.readthedocs.io/en/stable/)       | code formatter (does not use tabs)</br> python -m pip install black </br> python -m black .|    
|   | [mypy](https://www.mypy-lang.org/)        | type check code that uses type annotations </br> python -m pip install mypy </br> python -m mypy sample_project </br> [example](https://medium.com/@antongw1p/top-3-tools-you-need-when-working-with-python-c43a0d01a281) | 
|   | [pip-tools](https://github.com/jazzband/pip-tools) | A set of command line tools to help you keep your pip-based packages fresh, even when you've pinned them. | 
|   | [pipx](https://pypa.github.io/pipx/) | Install end-user python applicantions in self-contained environments |
| * | [pylint](https://pypi.org/project/pylint/)      | common code lint tool </br> python -m pip install pylint </br> python -m pylint sample_project |
| * | [virtualenv](https://virtualenv.pypa.io/en/latest/)  | Create and manage self-contained python environments |
|   | [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) | Wrapper for virtual env  |
</br></br>

## <a name='pip'></a>pip
### <a name='Commands'></a>Commands
* `pip freeze --local > requirements.txt` - Export all local packages
* `pip install --upgrade pip` - Upgraded pip
* `pip install -r requirements.txt` - Install dependencies listed in requirements.txt
### <a name='RelatedInfo'></a>Related Info
  * [How to install pip on Ubuntu](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/#:~:text=To%20install%20pip%20for%20Python%203%20on%20%3Cu%3EUbuntu%3C%2Fu%3E,verify%20the%20installation%20by%20checking%20the%20pip%20version%3A)
</br></br>

## <a name='pipx'></a>pipx
### <a name='Install'></a>Install 
     ```
     python -m pip install --user pipx
     ```
     cd to the folder identified in the WARNING message and run
     ```
     pipx ensurepath
     ```
     start a new shell
### <a name='Commands-1'></a>Commands 
  * `pipx install` _package_ - Install a new package
  * `pipx upgrade` _package_ - Upgrade package
  * `pipx upgrade-all` - Upgrade all packages
  * `pipx list` - List all packages
  * `pipx run` _package_ - temporarely downloads _package_ and runs it
</br></br>

## <a name='virtualenv'></a>virtualenv
### <a name='Commands-1'></a>Commands 
  * `python -m virtualenv` _venv_ - Create virtual environent `venv`
  * `.\venv\Scripts\activate` - Activate the virual environment
  * `.\venv\Scripts\deactivate` - Deactivate the virual environment
  * `pip install virtualenv`
  * `virtual env -p usr/bin/python2.6` - Create a virtual environment using a specified python version
  * [How to use virtualenv with Python](https://learnpython.com/blog/how-to-use-virtualenv-python/)
  * [Python tools for managing virtual envs](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
  * [A complete guide to Python virtual envs](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/ )

### <a name='RelatedInformation'></a>Related Information
  * [Python Tools for Managing Virtual Environments](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
</br></br>

## <a name='virtualenvwrapper'></a>virtualenvwrapper
### <a name='Commands-1'></a>Commands 
  * `mkvirtualenv` _env_ - Create virtual environment _env_
  * `lsvirtualenv` - List virtual envs
  * `showvirtualevn` _env_ - Show details of _env_
  * `workon` [ _env_ ] - Work on the specified virutal env
  * `deactivate` - Deactivate current environment (use system python)
  * [virtualenvwrapper commands](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#:~:text=Managing%20Environments%20%C2%B6%201%20mkvirtualenv%20%C2%B6%20Create%20a,existing%20virtualenv%20environment.%20...%207%20allvirtualenv%20%C2%B6%20)
  * [AttributeError: module ‘virtualenv.create.via_global_ref.builtin.cpython.mac_os’ has no attribute](https://techoverflow.net/2022/02/03/how-to-fix-tox-attributeerror-module-virtualenv-create-via_global_ref-builtin-cpython-mac_os-has-no-attribute-cpython2macosarmframework/)
</br></br>


