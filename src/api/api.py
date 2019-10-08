from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.DbManager import *
from src.cls.Round import *
from flask import Flask, jsonify, request, Response, render_template

app = Flask(__name__)

# ============== ROUNDS ==============

@app.route("/rounds", methods=["GET"])
def get_all_rounds(RoundsDbManager=RoundsDbManager):
    rounds = RoundsDbManager.get_all_rounds()
    print(rounds)

    return jsonify([round.make_json_obj() for round in rounds])

@app.route("/round", methods=["GET"])
def get_round(RoundsDbManager=RoundsDbManager):
    round_id = request.args.get("round_id")

    round = RoundsDbManager.get_round(round_id)

    return jsonify(round)

@app.route("/rounds", methods=["POST"])
def create_a_round(RoundsDbManager=RoundsDbManager):
    data = request.get_json()
    round = Round(data["owner"], data["time_started"], data["active"])
    round.orders = data["orders"]

    try:
        round_id = RoundsDbManager.create_round(round)
    except Exception as e:
        return Response(response=e,status=500)

    return Response(response=f"Successfully added round id {round_id}.",status=200)

# ============== PEOPLE ==============

@app.route("/people", methods=["GET"])
def get_all_people(PeopleDbManager=PeopleDbManager):
    people = PeopleDbManager.get_all_people()
    return jsonify([person.to_json() for person in people])

@app.route("/person", methods=["GET"])
def get_person(PeopleDbManager=PeopleDbManager):
    person_id = request.args.get("person_id")
    person = PeopleDbManager.get_person(person_id)
    return jsonify(person)

@app.route("/person", methods=["POST"])
def add_person(PeopleDbManager=PeopleDbManager):
    data = request.get_json()
    person = Person(data["name"], data["favourite_drink"])
    new_person_id = PeopleDbManager.create_person(person)
    return Response(response=f"Successfully created person id {new_person_id}", status=200)

# ============== DRINKS ==============

@app.route("/drinks", methods=["GET"])
def get_all_drinks(DrinksDbManager=DrinksDbManager):
    drinks = DrinksDbManager.get_all_drinks()
    return jsonify([drink.to_json() for drink in drinks])

@app.route("/drink", methods=["GET"])
def get_drink(DrinksDbManager=DrinksDbManager):
    drink_id = request.args.get("drink_id")
    drink = DrinksDbManager.get_drink(drink_id)
    return jsonify(drink)

@app.route("/drink", methods=["POST"])
def add_drink(DrinksDbManager=DrinksDbManager):
    data = request.get_json()
    drink = Drink(data["name"], data["temperature"])
    new_drink_id = DrinksDbManager.create_drink(drink)
    return Response(response=f"Successfully created drink id {new_drink_id}", status=200)

# ============== PAGES ==============

@app.route("/pages/drinks", methods=["GET"])
def get_drinks_html(DrinksDbManager=DrinksDbManager):
    drinks = DrinksDbManager.get_all_drinks()
    
    # Produce the HTML
    html_document = """
        <!DOCTYPE html>
        <html>
        <body>
            <p>Drinks</p>
            <ul>
        """
    for drink_name in drinks.all_drinks.keys():
        html_document += f"<li>{drink_name}</li>"
    html_document += """
            </ul>
        </body>
        </html>
        """
    return html_document

@app.route("/pages/order-example", methods=["GET", "POST"])
def person_form():
    if request.method == "GET":     # Return the entry form
        return render_template("order_form.html", title="Place an order")
    elif request.method == "POST":  # Take user input, return the submitted form
        person_name = request.form.get("person")
        drink_name = request.form.get("drink")

        # Do something wiht this information

        return render_template("order_submitted.html", title="Submitted", person=person_name, drink=drink_name)

if __name__ == "__main__":
    print("Starting server")
    app.run(host="0.0.0.0", port=8081, debug=True)
    