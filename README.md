# ThrowColour

ThrowColour is a small Python module to make printing messages with formatting and colours easier! This module is mostly just practice with creating a working pip module for learning purposes.

## Features

  - Supports different types of print messages with colour coding
  - Support basic formatting (bold, italics)
  - Supports timestamp printing

## Usage
###  Getting it

To download throwcolour, either fork this Github repo or simply use Pypi via pip.
```sh
$ pip install ThrowColour
```

### Using it

A few functional examples of how to use ThrowColour.

##### Basic Functionality

A basic example of how to use the ```cthrow``` function.

```Python
from throwcolour import cthrow
cthrow('Test 1,2')
```

This would print the message ```DATETIME - [INFO] Test 1,2``` in a nice looking purple with ```DATETIME``` replaced with the current timestamp.

![eg1](res/eg1.png?raw=true "Nov. 1st")

##### Setting Flags

```Python
cthrow('Test 1,2')
```
When setting flags, ensure the strings match exactly the name of the flag detailed below.
 * INFO - A nice aesthetic purple message
 * OK - A satisfying green message
 * WARN - A cautionary yellow message
 * ERR - A not-so-good red message
