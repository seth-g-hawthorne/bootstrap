# Launchpad: languages/python/libraries

**Contents**
<!-- vscode-markdown-toc -->
* [Command-Line Interfaces](#Command-LineInterfaces)
* [General Purpose](#GeneralPurpose)
* [Automation](#Automation)
* [Astronomy](#Astronomy)
* [System](#System)
* [Testing](#Testing)
* [UI](#UI)
* [Visualiation](#Visualiation)
* [Web Frameworks](#WebFrameworks)
* [Web Scrapting](#WebScrapting)
* [Related Information](#RelatedInformation)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->
</br> 

## <a name='Command-LineInterfaces'></a>Command-Line Interfaces
|   | **Library** | **Description** |
| - | ----------- | --------------- |
| * | [argparse](https://docs.python.org/3/library/argparse.html) | The argparse module makes it easy to write user-friendly command-line interfaces. |
|   | [begins](https://begins.readthedocs.io/en/latest/guide.html) | Command line programs for lazy humans. Decorate a function to be your programs starting point. Generate command line parser based on function signature. Search system environment for option default values. |
|   | [click](https://click.palletsprojects.com/en/8.1.x/) | Friendly argument parsing library [example](./examples/click/demo.py)|
|   | [colorama](https://pypi.org/project/colorama/) | Add color to command-line applications |


## <a name='GeneralPurpose'></a>General Purpose

|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [arrow](https://arrow.readthedocs.io/en/latest/) | Better dates & times for Python |
| | [black](https://black.readthedocs.io/en/stable/) | Code formatting library. [playground](https://black.vercel.app/?version=stable&state=_Td6WFoAAATm1rRGAgAhARYAAAB0L-Wj4ARsAnNdAD2IimZxl1N_WlkPinBFoXIfdFTaTVkGVeHShArYj9yPlDvwBA7LhGo8BvRQqDilPtgsfdKl-ha7EFp0Ma6lY_06IceKiVsJ3BpoICJM9wU1VJLD7l3qd5xTmo78LqThf9uibGWcWCD16LBOn0JK8rhhx_Gf2ClySDJtvm7zQJ1Z-Ipmv9D7I_zhjztfi2UTVsJp7917XToHBm2EoNZqyE8homtGskFIiif5EZthHQvvOj8S2gJx8_t_UpWp1ScpIsD_Xq83LX-B956I_EBIeNoGwZZPFC5zAIoMeiaC1jU-sdOHVucLJM_x-jkzMvK8Utdfvp9MMvKyTfb_BZoe0-FAc2ZVlXEpwYgJVAGdCXv3lQT4bpTXyBwDrDVrUeJDivSSwOvT8tlnuMrXoD1Sk2NZB5SHyNmZsfyAEqLALbUnhkX8hbt5U2yNQRDf1LQhuUIOii6k6H9wnDNRnBiQHUfzKfW1CLiThnuVFjlCxQhJ60u67n3EK38XxHkQdOocJXpBNO51E4-f9z2hj0EDTu_ScuqOiC9cI8qJ4grSZIOnnQLv9WPvmCzx5zib3JacesIxMVvZNQiljq_gL7udm1yeXQjENOrBWbfBEkv1P4izWeAysoJgZUhtZFwKFdoCGt2TXe3xQ-wVZFS5KoMPhGFDZGPKzpK15caQOnWobOHLKaL8eFA-qI44qZrMQ7sSLn04bYeenNR2Vxz7hvK0lJhkgKrpVfUnZrtF-e-ubeeUCThWus4jZbKlFBe2Kroz90Elij_UZBMFCcFo0CfIx5mGlrINrTJLhERszRMMDd39XsBDzpZIYV4TcG7HoMS_IF8aMAAAxI-5uTWXbUQAAY8F7QgAAP01Vc6xxGf7AgAAAAAEWVo=)|
| | [boltons](https://boltons.readthedocs.io/en/latest/) | a general-purpose collection of Python modules that covers a wide range of situations you may encounter. |
| | [celery](https://github.com/celery/celery) | | distributed system to process vast amounts of messages while providing operations with the tools required to maintain such a system. | 
| | [organize](https://organize.readthedocs.io/en/latest/) | Allows you to automate repetitive tasks by writing a simple YAML config file. |
| * | [parsedatetime](https://pypi.org/project/parsedatetime/) | Parse strings to date time| 
| | [pendulum](https://pendulum.eustace.io/) | a library for handling dates and times in Python. It provides a simple and easy-to-use API for working with dates and times, and it is compatible with the datetime module in the Python standard library. | 
| | [poetry](https://python-poetry.org/) | Python dependency management tool that makes it easy to install and manage your Python dependencies. It allows you to declare your dependencies in a single file, and it will handle installing them and creating a virtual environment for your project. |
| | [pulumi](https://www.pulumi.com/) | Create, update, and manage cloud infrastructure using code; AWS, Google Cloud, Azure |
| | [pydantic](https://github.com/pydantic/pydantic) | data validation and settings management using Python-type annotations. |
| | [pygame](https://www.makeuseof.com/pygame-drawing-objects-shapes/) | PyGame is a powerful and popular game development library for Python. It provides a set of tools and functions that make it easier to create games and other interactive applications.|

</br> 

## <a name='Automation'></a>Automation
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [sched](https://docs.python.org/3/library/sched.html) | Standard library to schedule events at time or intervals. | 
|   | [watchdog](https://pypi.org/project/watchdog/) | Receive notifications of changes in the file system. |

## <a name='Astronomy'></a>Astronomy
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [PyEphem](https://github.com/brandon-rhodes/pyephem) | provides highly precise data on the planets and our solar system. |
|   | [geemap](https://github.com/giswqs/geemap) | create detailed maps of the globe and plot points on them | 
|   | [pysat](https://github.com/pysat/pysat) | provides a clean interface to track and plot orbiting satellites. You can load different instruments and track various data provided by each one. | 
|   | [solarsystem](https://github.com/IoannisNasios/solarsystem) | provides the same ability to discover planetary positions and calculate celestial arrangements. This module is a bit simpler than PyEphem and doesn’t  contain as much information, but it is extremely easy to get started with. |
|    | [turboSETI](https://github.com/UCBerkeleySETI/turbo_seti) | provides an efficient way to analyze raw SETI data and sift through it for anomalies that could be markers for extraterrestrial life.  | 
</br> 


</br> 

## <a name='System'></a>System
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [psutil](https://pypi.org/project/psutil/)  | Access system process information |

</br> 

## <a name='Testing'></a>Testing
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [locust](https://github.com/locustio/locust)  | Locust is an easy to use, scriptable and scalable performance testing tool.  |



## <a name='UI'></a>UI 
|   | **Library** | **Description** |
| - | ----------- | --------------- |
| [gradio](https://gradio.app/) | the fastest way to demo your machine learning model with a friendly web interface so that anyone can use it, anywhere! |
|   | [pywebview](https://pywebview.flowrl.com/) | Build GUI for your Python program with JavaScript, HTML, and CSS | 


## <a name='Visualiation'></a>Visualiation 
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [altair](https://github.com/altair-viz/altair) | A declarative statistical visualization library. 
|   | [bokesh](https://github.com/bokeh/bokeh) | An interactive visualization library for modern web browsers. |
|   | [bqplot](https://github.com/bqplot/bqplot) | This is a plotting library for IPython/Jupyter notebooks. It provides a 2-D visualization system for Jupyter, based on the constructs of the Grammar of Graphics. In this library, every component of a plot is an interactive widget. |
|   | [cartopy](https://github.com/SciTools/cartopy) | A library is designed to make drawing maps for data analysis and visualization easy |
| * | [diagrams](https://github.com/mingrammer/diagrams) | Draw the cloud system architecture in Python code. Without any design tools. |
|   | [plotnine](https://github.com/has2k1/plotnine) | An implementation of a grammar of graphics in Python, it is based on ggplot2. |
|   | [Pyqtgraph](https://www.pyqtgraph.org/) |  Scientific Graphics and GUI Library for Python | 
|   | [seaborn](https://github.com/mwaskom/seaborn) | matplotlib based library that provides a high-level interface for drawing attractive and 

## <a name='WebFrameworks'></a>Web Frameworks
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [bottle](https://github.com/bottlepy/bottle) | This is a lightweight and simple Python web framework for building web applications. |

## <a name='WebScrapting'></a>Web Scrapting
|   | **Library** | **Description** |
| - | ----------- | --------------- |
|   | [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) | a library for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping | 
| * | | [pyPDF2](https://pypdf2.readthedocs.io/) | Read, write, and manipulate PDF files.| 
| * | [metadata_parser](https://pypi.org/project/metadata-parser/0.9.15/) | MetadataParser is a python module for pulling metadata out of web documents. |
|   | [mechanicalsoup](https://github.com/MechanicalSoup/MechanicalSoup | Automate interaction with websites. It automatically stores and sends cookies, follows redirects, and can follow links and submit forms. | 

## <a name='RelatedInformation'></a>Related Information
  * [awesome-python](https://github.com/vinta/awesome-python) A curated list of awesome Python frameworks, libraries, software and resources