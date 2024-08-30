# ColabCode (fix-update)

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![PyPI version](https://badge.fury.io/py/colabcode.svg)](https://badge.fury.io/py/colabcode)
![python version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python)

## Installation

```python
$ pip install git+https://github.com/your1name/colabcode-fix-by-me
```

Run code server on [Google Colab](https://colab.research.google.com/) or [Kaggle](https://www.kaggle.com/) Notebooks.

## Getting Started

ColabCode also has a command-line script. So you can just run `colabcode` from command line.

**`colabcode -h`** will give the following:

```console
usage: colabcode [-h] --port PORT [--password PASSWORD] [--mount_drive]

ColabCode: Run VS Code On Colab / Kaggle Notebooks

required arguments:
  --port PORT          the port you want to run code-server on

optional arguments:
  --password PASSWORD  password to protect your code-server from unauthorized access
  --mount_drive        if you use --mount_drive, your google drive will be mounted
  --version            Choose the version of VSCode to install, default is latest version
```

**Else**, you can do the following:

**Step 1: Add Auth token of ngrok**

```python

$ from pyngrok import ngrok
$ ngrok.set_auth_token("YOUR_TOKEN") 
```
You can get token at: ngrok.com

**Step 2: Import and use** 

Default is use vscode latest of [coder](https://github.com/coder/code-server). You can check version at [here](https://github.com/coder/code-server/releases)


```python
# import colabcode
$ from colabcode import ColabCode
```

```python
# run colabcode with by default options.
$ ColabCode()
```

```python
# ColabCode has the following arguments:
# - port: the port you want to run code-server on, default 10000
# - password: password to protect your code server from being accessed by someone else.
#             Note that there is no password by default!
# - mount_drive: True or False to mount your Google Drive
# - version: Choose the version of vscode, default 
$ ColabCode(port=10000, password="yourpass", mount_drive=True, version="4.92.2")
```

## License

[MIT](LICENSE)
