# Week 3: Testing

Testing increases your confidence in the product. Allows to you to be more confidently able to expand your codebase and add features without fear.

How can you prove your application behaves as intended?

Functional tests: does this do what I expected it to do?

Non-functional tests: non-acctions. e.g. within boundaries for performance, load, and security.

E.g. functional: can I request this and get a sensible response? Non-functional: does the response return within a certain amount of time?

A **regression** is the accidental breakage of some part of your software upon a change somewhere else (perhaps unrelated) in the codebase. Complex codebases with tightly coupled components are super prone to regressions.