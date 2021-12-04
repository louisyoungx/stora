
# Stora

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

Stora allows you to save dict to local as json extremely easily. There’s no need to manually open file and read, or save file after change your data — but nowadays,  just editor the state, and stora will automatically save for you!

Stora is a new Python package, welcome issue and pull request.

## Installing stora and Supported Versions

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

## API Reference and User Guide available on [Read the Docs](#)

Coming soon.

## Cloning the repository

When cloning the Requests repository, you may need to add the `-c
fetch.fsck.badTimezone=ignore` flag to avoid an error about a bad commit (see
[this issue](https://github.com/psf/requests/issues/2690) for more background):

```shell
git clone https://github.com/louisyoungx/stora.git
```
