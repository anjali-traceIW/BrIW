# Dynamic Websites

> Friday 27th September 2019

Manually writing out HTML is a pain and error-prone. We can dynamically generate and populate HTML for a page instead.

```python
def render_page():
  self.send_response(200)
  # We're about to send some HTML content, client should get ready
  self.send_header("content-type", "text/html")
  self.end_headers()
  
  # Produce the HTML
  html_document = """
<!DOCTYPE html>
<html>
  <body>
    <p>Drinks</p>
    <ul>
    	<li>Coffee</li>
    	<li>Tea</li>
    </ul>
  </body>
</html>
"""
  self.wfile.write(html_document.encode('utf-8'))
```

One way of being dynamic is to use formatted strings, e.g.

```python
drinks = ['Coffee', 'Tea']
# Produce the HTML
html_document = f"""
<!DOCTYPE html>
<html>
  <body>
    <p>Drinks</p>
    <ul>
    	<li>{drinks[0]}</li>
    	<li>{drinks[1]}</li>
    </ul>
  </body>
</html>
"""
```

We can respond to user input using HTML forms.

## MVC Model View Controller

Standard way to structure applications that expose a frontend to users.

**Model** (The flesh)

Holds the data.

POPOs Plain Old Python Objects. Dumb containers which hold your application data and nothing else. e.g. a drink object

**View** (The looks)

Presents the data aand takes new data from users.

The UI. Displays the information and allows user to provide input. Each view corresponds to an indicidial screen in our app.

**Controller** (The brains)

Saves and loads the data as well as orchestrating business logic.

Application logic and data management. Orchestrates or directly implements the rules and domain logic of our applications. Thin vs fat controllers; organiser vs doer. Retrieves and saves data via differentr data sources e.g. the view, APIs, databases, etc. Usually one controller per view.

```python
import database

# Controller that handles the Drinks screen in our app
# Define controller action to perform when IRL is /drinks
@app.rounte('/drinks')
def drinks_action():	# Controller functions typically ends wit _action
  drinks = database.get_drinks()
  # Pass in all the cariables you need in your view
  return render_template("drinks.html", drinks=drinks)
```

### MVC Implementation

Segragates responsibilities, this increasing the modularity and testability of apps.

## Using Flask

```python
ipmort service # ours
from flask umport Flask, jsonify

app = Flask(__name__) 	#

@app.route("/helloworld")
def hello_world():
  return "Hello World"

@app.route("/people")
def get_person():
  people = service.get_all_people()
  return jsonify([person.to_json() for person in people])

if __name__ == "__main__":
  app.run(host="localhost", port=8000)
```

