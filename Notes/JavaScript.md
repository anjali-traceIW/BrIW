# JavaScript

> Monday 30th Septmeber 2019 (Week 5)

Prototype-based: does not support OOP. 

Dynamically typed (non-typed). Variables ar edeclared differently depending upon if we want them to be accessed globally or locally.

```javascript
// Always global, no matter where it is declared 	:(
myvar = 1234;

// Not global if declared inside a function				:(
var yourvar = 12345;

// Takes the same scope it was declared in 				:)
let foo = 543521;

// Same as 'let' but immutable - a constant 			:)
const bar 9001;
```

### Difference between `var` and `let`: 

- Var will expand to the biggest functional scope 
- Let will expand to less than a functional scope, e.g. an if statementd

```javascript
function helloworld() {
  let h = "hello world";
  if (true) {
    let k = 1234
  }
  console.log(k)
}
helloworld();
```

Will throw an error `k is not defined`, where as if this line was instead `var k = 1234`,  would print 1234 as expected.

### Formatted strings

Python: 

```python
text = f"{name}'s favourite drink is {drink}'"
```

JavaScript:

```javascript
const drinks = ['coffe', 'tea', 'water'];
for (let i = 0; i < drinks.length; i++) {
  console.log(i)
    console.log(`Would you like some ${drinks[i]}?`);
}
```

### Switch Statements

```javascript
const userOption = 2;
switch (userOption) {
    case 1:
        console.log('You selected option 1');
        break;
    case 2:
        console.log('You selected option 2');
        break;
    default:
        console.log('You did not enter a valid option');
        break;
}
```

Don't forget the `break`!!

### Arrays

```javascript
const drinks = ['coffee', 'beer', 'water'];
drinks.push('tea');
// Prints: ['coffee', 'beer', 'water', 'tea']
console.log(drinks) 
const selectedDrink = drinks[1];
// Prints: 'beer'
console.log(selectedDrink) 
```

### Object

Most like a Python dictionary

```javascript
const person = {
    "name": 'Kyle',
    "age": 25
};
console.log(person.name) 			// Prints: 'Kyle'
console.log(person["name"]) 	// Prints: 'Kyle'
```

| Client side                                                  | Server side                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Runs in-browser                                              | Runs directly on top of OS via Node runtime                  |
| DOM-aware. Can do DOM manipulation                           | Supports newest language features                            |
| Conservative and outdated                                    | Has additional libraries to access OS features e.g. filesystem, env, vars ... |
| Vendor-dependent, i.e. when a new JS feature is released, must wait for individual browser vendors to implement it. |                                                              |
| Input validation                                             |                                                              |
| Animations                                                   |                                                              |
| Updating your website dynamically                            |                                                              |

Useful website: caniuse.com

### JavaScript in HTML

In HTML, can introduce JavaScript using the `<script>` tag in one of two ways:

```html
<script>
	alert("Hello World")
</script>
<script src="./main.js"></script>
```

Access the DOM by the `window.document` object

```html
<p>Hello <span id="user-name">User</span>!</p>
<script>
  const greeting = document.getElementById('user-name')
  greeting.textContent = 'Brendan';
  // Can change CSS things
  greeting.style.color = "red"
</script>
```

Can attach code to events - what is raised whenever the user does something with a page.

```html
<p>Hello <span id="user-name">User</span>!</p>
<button onClick="handleGreetingButtonClick()">Customise Greeting</button>
```

```javascript
function handleGreetingButtonClick() {
  const greeting = document.getElementById('user-name');
  greeting.style.color = 'green';
  greeting.textContent = 'Brendan';
}
```

### High-order functions

You can pass functions into functions.

The `forEach` array function runs a supplied function against all elements in the array. Expects the argument function to accept one argumentL teh element in the current iteration.

```javascript
function printDrinkMessage(drink) {
    console.log(`Would you like to drink some ${drink}?`);
}

const drinks = ['tea', 'coffee', 'water'];
drinks.forEach(printDrinkMessage);
```

### Events

```html
<button onClick="handleClick()">Click Me</button>
<br>
<button id="button">Reveal the Truth</button>
<p id="hidden-text" style="display: none;">JavaScript is actually an okay language</p>
```

```javascript
function handleClick() {
  alert("Hello world!");
}

function handleSecondButtonClick() {
  const hiddenText = document.getElementById('hidden-text');
  hiddenText.style.display = 'block';
}

const button = document.getElementById('button');
button.addEventListener('click', handleSecondButtonClick);
```

To make a button:

```html
<input type="submit" value="Go">
```

```javascript
function handleSubmit(ev) {	// ev is the event captured
  ev.preventDefault();	// Don't submit straight away!
  const person = document.getElementById('person')
  const drink = document.getElementById('drink')
  
  if (/* is invalid person or drink */) {
    const inputErrorMessage = document.getElementById('input')
    inputErrorMessage.style.display = 'block';
  } else {
    ev.currentTarget.submit()
  }
}
```



### Anonymous Functions

Functions without a name. Non-reusable, one-off functions. Can be inlined as arguments to other functions.

```javascript
const drinks = ['coffee', 'tea', 'water'];
drinks.forEach(function (drink) {
  console.log('Would you like to drinks some ${drink}?');
});
```

```javascript
function runAnyFunction(fn) {
  console.log("Hey, I'm running a function.");
  fn();
}

runAnyFunction(function () {
  console.log("Hello, I'm an anonymous function!")
})
```

> Tuesday 1st October 2019 (Week 5)

### Query Selectors

A more powerful way of selecting elements in the DOM.

`document.querySelector` gets the first element in the DOM that matches criteria.

`document.querySelectorAll` gets all the elements in the DOM that match criteria.

```html
<p class="hightlight-blue">Paragraph 1</p>
<p class="hightlight-blue">Paragraph 2</p>

<p class="hightlight-red">Paragraph 3</p>
<p class="hightlight-red" id="par4">Paragraph 4</p>
<p class="hightlight-red">Paragraph 5</p>

<button onClick="handleBlueButtonClick()">Make Blue</button>
<button onClick="handleRedButtonClick()">Make Red</button>
```

```javascript
function handleBlueButtonClick() {
  const bluePara = document.querySleector('.highlight-blue');	// To select by class, use #
  bluePara.style.background = 'blue';
  
  const par4 document.querySelector('#par4');	// To select by id, use #
  par4.style.color = 'green';
}

function handleRedButtonClick() {
  const paragraphs = document.querySelectorAll('.highlight-red');
  paragrpahs.forEach(function (para) {
    para.style.background = 'red';
    para.style.color = 'white';
  });
}
```

## Working Asynchronously

Synchronis, is the conincidence in time of multple events. Computers are pretty good at doing things in parallel.

Synchronous events happen in strict succession.

Asynchronous events execute simultaneously, which means they may not complete in succession.

### AJAX

Asynchronous JavaScript and XML

Lets you website communicate with other servers in the background. Allows for automatic updates in parts of your site, making it feel more responsive and native.

#### AJAX GET

```html
<button id="load-button">Load Content</button>
<br><br>
<textarea id="textarea" rows="30" cols="50"></textarea>
```

```javascript
function handleClick() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://api.github/users/dvejmz', true);
  
  xhr.onload = function (response) {	// argument not necessary; can be empty.
    console.log(response)	// Some useful stuff in here?
    docmuent.querySelector('#textarea').textContent = xhr.responseText;
  };
  
  xhr.send(null);
}
document.querySelector('#load-button').addEventListener('click', handleClick);
```

#### AJAX POST

```javascript
const xhr = new XMLHttpRequest();
const json = JSON.stringify({
  name:"Jojo",
  surname:"Smith"
});
xhr.open("POST", "/path")
xhr.onload = function () {
  document.querySelector("#successMessage").style.display = "block"
}
```

