# Introduction to Property Based Testing
## (Using Hypothesis)

We've covered Test Driven Development at this event many times before, and the many benefits it provides. Among other types of tests, we can create Regression Tests when we fix a bug, to ensure it doesn't happen again. But could we be more proactive than that?

What if we could generate Tests from our code, and find bugs before our end users do? What if we wrote "specifications" or "strategies" instead of individual tests?

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) is a modern, Python implementation of property based testing. To quote wikipedia:

> Property testing is a testing technique where, instead of asserting that specific inputs produce specific expected outputs, the practitioner randomly generates many inputs, runs the program on all of them, and asserts the truth of some "property" that should be true for every pair of input and output. For example, every input to a sort function should have the same length as its output. Every output from a sort function should be a monotonically increasing list.

> Property testing libraries allow the user to control the strategy by which random inputs are constructed, to ensure coverage of degenerate cases, or inputs featuring specific patterns that are needed to fully exercise aspects of the implementation under test.

> Property testing is also sometimes known as "generative testing" or "QuickCheck testing" since it was introduced and popularized by the Haskell library [QuickCheck](https://hackage.haskell.org/package/QuickCheck).

## Setup

At minimum, we need to install the `PyTest` library (a framework for creating, discovering, and running Tests), and `Hypothesis`, which will help us do property-based testing specifically. We've also included some other handy Python development tools like `black` (for automatic code formatting), `isort` (for automatic import sorting) and `rope` (to help VSCode perform refactoring in Python).

_(This setup should happen automatically in GitPod, but if not, use the "Manual Setup via Pip" instructions below.)_

### Automated Setup via Poetry

The dependencies and virtual environment of this project can be managed automatically using `poetry`:
```
poetry install
```

### Manual Setup via Pip
Alternately, create or select an environment through some other means, then install the required packages directly using `pip`:
```
pip install -r requirements.txt
```

## Using Hypothesis



## Updating Dependencies

If you use `Poetry` to install or upgrade any package dependencies, make sure that you "export" the new package selection to the requirements.txt file before committing. _(This is important for environments like GitPod that will use requirements.txt directly!)_
```
poetry export --with=dev > requirements.txt
```
