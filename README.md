# Prancer
Ever heard of [Black](https://github.com/psf/black)? This is the opposite.
A tool to turn your clean python code into a hideous (working) mess.

## Features
1. Turn all comments into lines from My Little Pony.
2. Turn all your variable names into a mixture of pony names and horribly similar looking characters like "Twilight_Dash_0OO0O".
3. Add irritating white spaces.
4. Code still runs after all these _improvements_! 👷


## Example
Before:
```python


# function that adds two numbers
def addition(a: int, b: int) -> int:

    # find sum
    result = a + b

    # return the sum
    return result


if __name__ == '__main__':
    print("Sum of 1 and 3 is %s" % addition(1, 3))

```

After:
```python

# TODO Add this example

```

## Installation and Usage
Simply run `pip install git+https://github.com/L33Tech/prancer.git` and then use the `prance` command line tool.

```
usage: prance [-h] [--version] -f ./FILE_PATH.py [-y]

Ever heard of Black? This is the opposite.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -f ./FILE_PATH.py, --file ./FILE_PATH.py
                        Python file to be prance'd.
  -y, --yolo            Overwrite original file, lol.
```

So if you have a python file at `./test.py`, you simply run `prance -f ./test.py`

## How does it work
The key tool we use it the `tokenizer` standard module in python. It allows us to tokenize any python script which then in turn makes substituting comments and variable names fairly simple.
Check out the source code for more details. 

## Contribute
Bug reports, fixes and additional features are always welcome! Make sure to run the tests with `python setup.py test` and write your own for new features. Thanks.
