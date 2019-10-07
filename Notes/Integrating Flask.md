# Integrating Flask

> Monday 30th September 2019 (Week 5)

## POST with Flask

```python
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST': 
        person_name = request.form.get('person')
        drink_name = request.form['drink']

        return render_template("return_person_drink.html", title="Posted", person=person_name, drink=drink_name)

    return render_template('add_form.html', title="Create Form")
```

add_form.html:

```html
<form method="POST">
  Person: <input type="text" name="person"><br>
  Drink: <input type="text" name="drink"><br>
  <input type="submit" value="Submit"><br>
</form>
```

return_person_drink.html:

```html
<h1>For: {{person}}</h1>
<h1>Drink: {{drink}}</h1>
```

Can use jinja with our html templates to introduce some logic:

```html
<h1>
    Successfully placed an order 
    {% if drink %}
    of {{drink}} 
    {% endif %}
    {% if person %}
    for {{person}}
    {% endif %}
</h1>
```

