# Week 3: Testing

Testing increases your confidence in the product. Allows to you to be more confidently able to expand your codebase and add features without fear.

How can you prove your application behaves as intended?

Functional tests: does this do what I expected it to do?

Non-functional tests: non-acctions. e.g. within boundaries for performance, load, and security.

E.g. functional: can I request this and get a sensible response? Non-functional: does the response return within a certain amount of time?

A **regression** is the accidental breakage of some part of your software upon a change somewhere else (perhaps unrelated) in the codebase. Complex codebases with tightly coupled components are super prone to regressions.

## Unit Testing

### What is unit testing?

Define a unit as:

the smallest amount of your code which can be executed independently. 

Something that is executed as a "whole", e.g. a function.

#### Structure

The three A's:

- **Arrange** - What do we need to provide in order to test our unit? e.g. necessary parameters to supply the function we are testing. Also, what do we expect to come out? What kind of object/value is this?
- **Act** - Call and pass args to the this you are testing. Actually run the thing!
- **Assert** - Check that the output was what was expected. 

### Why do we unit test?

- Enables confidence in changes
- Helps understand the design of the code
- Efficient and don't require much effort to rerun
- Eliminate anxiety
- Living documentation - read through tests to understand exected behaviour and how to use

```python
if __name__ == "__main__": 
	unittest.main()
```

Basic round functionality created and working. Need to be able to view rounds but users can now start a round and add orders. People or drinks not already known to the system are rejected. Want to be able to add a new person/drink to all known people/dirnks instead of rejection. Persisting rounds in memory not yet implemented.

### Test Driven Development (TDD)

1. Write tests
2. Run tests (which fail because there is no codebase)
3. Write the code
4. Run tests (they pass)

### Mocking/stubbing/spies

#### Mocking

Creating a fake version of a classs or sersvice in order to test  something else

Don't care about the implementation of the mocked object/other features

A way of using abstraction/encapsulation.

#### Stubbing

In python, stubbing is covered by mocking

Mimicking the specific behaviour or something, not whole instances, e.g. for a function.

#### Spies

- A stub that also holds information about <u>how</u> they were called.
- See how the code behaves as you go through it.
- Tracks local variables/allows inspection at a given point in execution.
- Python library called KGB available ;)

Say we have mocked some things. 

```python
@unittest.mock.patch("builtings.input"), return_value=unittest.mock
def test_input_method(self,input_return):
  combo = {}
  input_return.side_effect = ["Henry", "Americano"]
  
  expected = {"Henry":"Americano"}
  
  actual = input_person_to_add(combo)
  
  self.assertEqual(expected, actual)
```

A side effect is essentially a list of things to return. Will return the next thing in the list each time it is called.

We can check they have indeed been called as expected with things like:

```python
# Has our mocked henry.full_name been called?
henry.full_name.assert_called_with()

#
os_system.assert_called_once_with("clear")
```



### Integration testing

- Testing between multiple layers of code (their *integration*)
- Checking multiple compononts
- Best to be seperate from unit tests
- Consider the pyramid: there should be fewer integration tests than unit tests. Recall it's harder to narrow down specific causes in these.

### Behaviour Driven Development (BDD)

Give joint understanding between techy and business of how the application should behave.

Formed through:

- a narritive

Like user stories in requirements!

> As a brewer -- I want to create a round -- so that i can organise a round of drinks

> Given I select create round -- when I input my name into the application -- then I am assigned to make the round of drinks