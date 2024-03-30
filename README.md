![image](https://github.com/Pimed23/list-holiday/assets/42551016/362422c8-45f9-4ea4-a540-0f1968a29155)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)

This program requests information from the legal holidays API in Chile (https://apis.digital.gob.cl/fl/), processes the received response, and extracts only the information regarding holidays occurring from the year 2020 onwards. It was written in Python and supports the following features:
- [Poetry](https://python-poetry.org) for dependency management
- [Pydantic](https://docs.pydantic.dev/latest/) to generate and validate data models
- Testing and coverage using [Pytest](https://docs.pydantic.dev/latest/)
---
# Requirements
- python ^3.10
- pip
- poetry
   
# Quickstart

On your local machine, navigate to the directory in which you want to create a project directory, and clone the project:
```
git clone https://github.com/Pimed23/list-holiday.git
```

After that, we navigate to the directory we just cloned. As mentioned earlier, the project is built using Poetry, so we need to install it (don't forget to set up the environment variables):
```
pip install poetry
```

Poetry is a Python dependency manager. To install the project dependencies, we execute the following command:
```
poetry install
```

Once this is done, a virtual environment will be created where these dependencies will be stored. To start the project, we write:
```
poetry run start
```

In case you want to review the tests, you can use the following command:
```
poetry run pytest
```


