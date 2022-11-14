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

This project includes two python Modules, with some code that you can implement in a Test Driven Development style - There are function stubs (including documentation and type annotations) that need code, and some suggested Tests that you might want to implement along the way.

### Day Of Week function

In [day_of_week.py](date_utils/day_of_week.py), we have a function `monday_this_week` that, given a datetime, should return a new datetime at midnight on Monday that week (i.e. the same week that the input datetime is from). What test might we start with? How might we implement this function?

Hints:
* You can get the current datetime by calling `datetime.now()`
* You can extract the day of the week from a datetime using `.weekday()`
* _(Remember that weeks start on Monday (weekday 0) in Python datetimes!)_

Once you have a function that "seems" to do what we want, how can we test it more exhaustively in Hypothesis?

Hints:
* Check out the [Hypothesis quick start docs](https://hypothesis.readthedocs.io/en/latest/quickstart.html) for an example
* The `hypothesis.strategies.datetime()` strategy will generate datetimes

This function should be idempotent, in the sense that calling it on a datetime once should produce the same output as calling it two or more times... How can Hypothesis help with that?

Hints:
* Check out the docs on the [Hypothesis Ghostwriter](https://hypothesis.readthedocs.io/en/latest/ghostwriter.html)
* Try `hypothesis write --idempotent date_utils.day_of_week.monday_this_week` on the command line
* Or in a Python REPL:
```
from hypothesis.extra import ghostwriter
print(ghostwriter.idempotent(date_utils.monday_this_week))
```
### Day Of Week function

In [time_since.py](date_utils/time_since.py), we have a stack of function stubs, written in a "functional core, imperative shell" style: To do Test Driven Development, you'll want to start with the lower level functions such as `hours_ago`, and "work your way up" to the higher level functions, though they should be much more straightforward to test at that point...

Once you've finished your typical TDD process, and have your own tests for a function, consider how you might use Hypothesis to test it more thoroughly.

Hints:
* What Strategies should you use for a given function?
* Are there any values you want to filter out of your strategy?
* _(As documented, these functions operate on Datetimes in the past...)_
* You could filter out values you don't want to test for
    * (assuming you will handle that filtering in your code!)
* Or your function(s) could raise specific exceptions for invalid dates
    * (in which case your strategy/test should consider that exception)
    * (see the [assume](https://hypothesis.readthedocs.io/en/latest/details.html#making-assumptions) and/or [filter](https://hypothesis.readthedocs.io/en/latest/data.html#filtering) documentation for more information)

## Updating Dependencies

If you use `Poetry` to install or upgrade any package dependencies, make sure that you "export" the new package selection to the requirements.txt file before committing. _(This is important for environments like GitPod that will use requirements.txt directly!)_
```
poetry export --with=dev > requirements.txt
```
