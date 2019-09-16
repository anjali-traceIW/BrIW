# Testing

with Katia

## Types of testing

Unit testing: If you took the component into an empty room to test, you're unit testing.

Integration testing: Do you need more than one thing to test it? Are you testing how multiple things interact? You're integration testing.

End-to-end testing: Checking big-picture functionality

UAT: If the user does this, does our application

Smoke testing: broad not deep. If I touch all these things, does anything fall over?

Regression testing: Deep not broad.

## What is testing?

Idiot-proofing: can be achieved with limiting user options, but most effectively achieved with good design. Is it obvious what the user should be doing? If little explanations are required, you're design could use some improving!

Testing is: 

- Information gathering - helps decision making and builds confidence
- Learning - learn about your product, understand behaviour, decrease risk as knowledge increases.

Testing is not:

- Finding defects - this is a <u>consequence</u> of testing
- A tick box exercise - if it doesn't add value, don't do it
- Quality assurance - this is a shared responsibility with development. Testing alone will not spontaneously introduce quality.

## Who does the testing?

Developers:

- Unit tests
- integration tests
- automated regression tests
- End to end tests
- performance (if of interest?)
- system monitoring?

PO/PM/BA (Product)

- Acceptancec testing
- Design review
- User feedback 
- System moitoring

Users

We won't throw untested things at our users in hopes of them discoving problems! We can ask them what they likecan be improved in functionality or design. Are things clear? Alpha/Beta testing. Feedback.

Tester

Thorough considerations of use cases. 

- Test strategy
- Test harness
- Automated regression tests
- Exploratory testing
- End to end testing
- Performance tests - e.g. does this task complete in a reasonable time?
- system monitoring
- acceptance tests
- Design review
- UAT
- user feedback
- Code coverage (a double edged sword - everything may be covered but not sufficient)

These roles can blur together dependent upon team composition/individual interests, e.g. may have a developer invested in automated testing, may have an univolved PO so some back and forth is required?

The clearer a question we can ask, the better an answer testing can provide.

Do as much testung as nbeeded to be confident that our code works as expected.

Go forth and break things!