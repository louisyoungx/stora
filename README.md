
# Stora  [![Visits][visits-badge]](github-page) [![Version][version-badge]][version-link] [![MIT License][license-badge]](LICENSE.md)

**Stora** is a simple, reactive local storage library.

```python
>>> from stora import stora
>>> apple = {"name": "Apple", "price": "10", "size": "small"}
>>> s = stora(apple)
>>> s.state
'{"name": "Apple", "price": "10", "size": "small"}'
>>> s.file
'/home/user/project/state.json'
>>> s.state["size"] = "middle"
>>> s.state
'{"name": "Apple", "price": "10", "size": "middle"}'
```

Stora allows you to save dict to local as json extremely easily. There’s no need to manually open file and read, or save file after change your dict data — but nowadays,  just editor the state, and Stora will automatically save for you!

Stora is a new Python package, welcome issue and pull request.

## Installing Stora and Supported Versions

Stora is available on PyPI:

```shell
$ python3 -m pip install stora
```

Stora only support Python 3.6+.

## Supported Features & Best–Practices

Stora is ready for simple data storage.

> if you need high performance, use a professional database is a better choice.

- Data persistence saving.
- Synchronize data saving to local.
- Customizable file names.
- Customize the save directory.
- Save format is *json* by default.
- Read format is *dict* by default.
- TODO Save files asynchronously
- TODO Debounce function

## Quick Start

Stora will save data as `state.json` in **current working directory**.

```python
from stora import stora
apple = {"name": "Apple", "price": "10", "size": "small"}
s = stora(apple)
print(s.state) # {"name": "Apple", "price": "10", "size": "small"}
```

> **PS:** *You can also decide the filename and filepath.*
> ```python
> s = stora(apple, filename='apple.json', filepath='~/.data/')
> ```

Now open `state.json`, you will see:
```json
{
    "name": "Apple",
    "price": "10",
    "size": "small"
}
```

Next time when you initialize a stora class in the same working directory, Stora will search if there is a file called `state.json`, if it exists it will load it and return a reactive dict.

```python
from stora import stora
s = stora()    # Stora will search state.json and load it
print(s.state) # {"name": "Apple", "price": "10", "size": "small"}
```

> **PS:** If the filename and filepath are specified, use the following code to initialize it.
>
> ```python
> s = stora(filename='apple.json', filepath='~/.data/')
> ```

Fetching and assignment operations are exactly the same as dict.

```python
# Fetching
print(s.state['name']) # Apple
print(s.state['price']) # 10
# Assignment
s.state['name'] = 'Banana'
s.state['price'] = 20
```

Now you will see that the contents of the `state.json` have changed.

```json
{
    "name": "Banana",
    "price": "20",
    "size": "small"
}
```

Here's a feature that may cause confusion. If initialize stora again,

```python
from stora import stora
apple = {"name": "Apple", "price": "10", "size": "small"}
s = stora(apple)
print(s.state) # {"name": "Banana", "price": "20", "size": "small"}
```

run `print(s.state)`, you will find the data is not what you assign to stora, it's data saved in `state.json` .

That's because stora sets the data already read under the current filepath and filename to a higher priority in order to prevent data loss.

You can force an overwrite of the stora state, or define a new stora with different filename or filepath.

```python
s1 = stora(apple, force=True) # force an overwrite
s2 = stora(apple, filename='apple-10.json') # define a new stora with different filename or filepath
```

## API Reference and User Guide available on [Read the Docs](#)

Coming soon.

## Cloning the repository

```shell
git clone https://github.com/louisyoungx/stora.git
```



[github-page]: https://github.com/louisyoungx/stora
[version-badge]:   https://img.shields.io/pypi/v/stora.svg?label=version
[version-link]:    https://pypi.python.org/pypi/stora/
[license-badge]:   https://img.shields.io/badge/license-MIT-007EC7.svg
[visits-badge]: https://badges.pufler.dev/visits/louisyoungx/stora
