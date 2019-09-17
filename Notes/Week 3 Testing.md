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

Mocking/stubbing/spies

integration testing

BDD