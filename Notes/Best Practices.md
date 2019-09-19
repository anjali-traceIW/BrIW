# Programming ++ (Best Practices)

> Wednesday 18th September 2019 (Week 3)

[TOC]

## Modules

What is a module?

A self-contained collection of classes, functions and variables which are available under a namespace.

Provide an easy way to organise components in an application

### Namespaces

an area within which a particular name has a particular meaning

allow you to reuse names

A programmer creating a namespace can use any name in that namespace. The same name can have different meanings in different contexts (namespaces)

A fully qualified name of a resource is preficed by the namespace in which the name exists.

### Creating a module

Simply save your code in a different file. 

Make sure the filename followes the same naming rules as variables i.e. no illegal chars etc.

e.g. in a file called `state.py`:

```python
def load_drinks():
	# do some loading
def load_people():
  # do some more loading
def load_preferences():
  # do even more loading
```

### Using a module

Once you've created a module, you can import it into any file where you would like to use it.

In order to use a module, we need to bring it into scope in our current file. Do this with the import statement.

e.g. using our `state` module in a file called `app.py` 

```python
# Assuming state.py is in the same directory
import state
drinks = state.load_drinks()
```

**Q:** What if we have a file called `os.py`? `import os` also imports a useful library. What happens? 

**A:** In general, try not to do this. Python will look in the directories specified by the system.path for anything to import. It will look locally first, then expand to the location where python libraries are stored. So, first come first serve. Else could give it the absolute file path to your local module.

You can limit the amount of things you import if you're not going to use everything from a library. Helps with clarity and readability - others will know you're only using certain bits of a given library.

```python
from state import load_drinks, load_people
```

Can import everything without need to refer to the module name later on.

```python
from state import *
# This uses the load_drinks() from state.py
drinks = load_drinks()	
```

<u>Note</u>: Python will run any modules you import from top to bottom unless you tell it otherwise.

Helpful: can also alias a module and treat it as you would otherwise.

```python
import state as magic
drinks = magic.load_people()
```

### Referencing Modules

The loaction of module files in our filesystem is important as it dictates how we reference them. 

Types of import:

- **Global**: use for files in the same directory, standard python libraries, or 3rd party libraries. No path specification required
- **Absolute**: always start from the project top-level directory (the project root directory)
- **Relative**: path relative to the file doing the importing. Not fun in Python3, so avoid them!

## Packages

A package is a collection of modules uinder one directory that are made available under a parent namespace.

Create a file called `__init__.py` in the directory (say called `package`) you want to include in the package. It is usually empty. This will make everything in and under the directory with the init file in part of the package called `package`

```python
# global
import sys
import state

# absolute
import core.rounds

# relative
import .core.rounds
```

## Libraries

A collection of useful code you reuse in different parts of your application or in different project.

### Standalone applications vs libraries.

The main difference between the two is that apps habe an entry point whereas libraries don't.

When you execute a Python source file directly, puthon gens a entrypoint for it which will be the first line it finds on its global scope.

Some source files can be used as <u>both</u> a library and as a standalone application.

Can address this, that is set the entry point, with 

```python
if __name__ == "__main__":
  # Run this code only if the file is run as a standalone application.
```

Then, if the file is imported into another

Some useful libraries:

#### Pytest

`pip install pytest`

Runs your test nicely from the command line.

#### Coverage

A test coverage application, which gives you a nice report with a percentage of how much of your code is being ckhecked by tests.

```bash
$ coverage report -m
```

Test coverage percentages can be useful, but are not more important than good testing.

## VirtualEnvs (venv)

An isolated location/context in your computer where you can install python libraries without interfering with the python sys libs already installed in your computer.

Helpful for managing versions of libraries or avoiding a mess of system libraries.

### Creating a venv

```bash
# Create a venv in the location of your choosing
$ python3 -m venv /path/to/app/virtualenv/briw

# Source the 'activate' script to activate the briw venv
$ source /path/to/app/virtualenv/briw/bin/activate

# Will install pytest in the virtualenv dir instead of your system.
(briw) $ pip install pytest
```

Handy thing: `virtualenvwrapper` 

### Installing App Dependencies Quickly

`requirements.txt` contains a simple list of all pip packages your app needs to run at top level

```bash
$ pip install -r path/to/requirements.txt
```

--python=python/path

```bash
$ pytest -m src --cov=src test
```



## Programming Best Practices

Some mantras:

> Programs must be written for people to read, and only incidentally for machines to execute.
>
> -Harold Abelson

> You know you are working on clean code when each routine you read turns out to be prettyt much what you expected
>
> -Ward Cunningham

Follow the principle of least surprise.

### Key Ideas

- Functionality: does it work?
- Testability: are you sure it works?
- Readability: 

> Bad code tries to do too much, has muddled intent and ambiguity of purpose.
>
> Clean code is focussed. Each function, each class, each module exposes a single-minded attitude that remains entirely undistracted, and unpolluted, by the surrounding details.

### The Acronyms of Clean Code

- **KISS**  Keep It Simple Stupid
- **DRY** Dont Repeat Yorslef
- **YAGNI** You Ain't Going to Need It
- **DTSTTCPW** Do The Simplest Thing That Could Possibly Work
- **IIABDFI** If It Aint Broke Don't Fix It
- **RTFM** Read The Manual

### Coding Best Practices

Code smells when it is not clean 

#### Code Layout

What can we do to make code more readable?

- Indentation is essential, even if not syntacitally required!
- Whitespace is free - use it to make your code easier to read
- Keep your lines short (80-120)
- Keep related things together
- Remove dead code aggressively - idenitfy it with good testing - it rots

#### Variables

Careful not to get analysis paralysis

- Avoid global variables
- Use intention-revealing names
- Longer names are not bad if theyre meaningful (but don't overdo it)
- Immutable variables make for applications which are easier to follow and test.

#### Functions 

- Small
- Do one thing
- No side effects

#### Classes

- Single purpose: only one reason to change
- Encapsulation
- Keep inheritance to a minimum

#### Components

- Be honest about your dependencies (Inversion of Control, Dependency Injection; Martin Fowler)
- Clear communication boundaries
- Avoid tight coupling

### Documentation

- Only provide what's valuable
- Comments: less is more. Prefer self-documenting code
- README.md: bare minimum. Tell people how to installm set up, use, and contribute code to your application.
- High-level Design Specifications (HLD)
- UML (Universal Modelling Language)

### Refactoring

Improving the way our code is written without affecting the end result. A gradual process.