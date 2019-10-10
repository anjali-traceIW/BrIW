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

    return jsonify(round.make_json_obj())

@app.route("/rounds", methods=["POST"])
def create_a_round(RoundsDbManager=RoundsDbManager):
    data = request.get_json()
    round = Round(data["owner"], data["time_started"], data["active"])
    round.orders = data["orders"]

    try:
        round_id = RoundsDbManager.create_round(round)
    except Exception as e:
        return Response(response=e,status=500)

    return Response(response=f"Successfully added round {round_id}.", status=201)

@app.route("/round", methods=["PATCH"])
def place_an_order(RoundsDbManager=RoundsDbManager):
    data = request.get_json()
    round_id = data["round_id"]
    order = (data["name"], data["drink"])
    new_order_id = RoundsDbManager.create_order_for_round(round_id, order)

    return Response(response=f"Successfully added order {new_order_id} to round {round_id}", status=200)

# ============== PEOPLE ==============

@app.route("/people", methods=["GET"])
def get_all_people(PeopleDbManager=PeopleDbManager):
    people = PeopleDbManager.get_all_people()
    return jsonify([person.to_json() for person in people])

@app.route("/person", methods=["GET"])
def get_person(PeopleDbManager=PeopleDbManager):
    person_id = request.args.get("person_id")
    person = PeopleDbManager.get_person(person_id)
    return jsonify(person.to_json())

@app.route("/person", methods=["POST"])
def add_person(PeopleDbManager=PeopleDbManager):
    data = request.get_json()
    person = Person(data["name"], data["favourite_drink"])
    new_person_id = PeopleDbManager.create_person(person)
    return Response(response=f"Successfully created person with id {new_person_id}", status=201)

# ============== DRINKS ==============

@app.route("/drinks", methods=["GET"])
def get_all_drinks(DrinksDbManager=DrinksDbManager):
    drinks = DrinksDbManager.get_all_drinks()
    return jsonify([drink.to_json() for drink in drinks])

@app.route("/drink", methods=["GET"])
def get_drink(DrinksDbManager=DrinksDbManager):
    drink_id = request.args.get("drink_id")
    drink = DrinksDbManager.get_drink(drink_id)
    return jsonify(drink.to_json())

@app.route("/drink", methods=["POST"])
def add_drink(DrinksDbManager=DrinksDbManager):
    data = request.get_json()
    drink = Drink(data["name"], data["temperature"])
    new_drink_id = DrinksDbManager.create_drink(drink)
    return Response(response=f"Successfully created drink with id {new_drink_id}", status=201)

# ============== PAGES ==============

@app.route("/pages/drinks-test", methods=["GET"])
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
    for drink in drinks:
        html_document += f"<li>{drink.name}</li>"
    html_document += """
            </ul>
        </body>
        </html>
        """
    return html_document

@app.route("/pages/nineties", methods=["GET"])
def get_nineties():
    return render_template("nineties.html")

@app.route("/pages/people", methods=["GET"])
def show_people():
    people = PeopleDbManager.get_all_people()
    return render_template("view_people.html", title="View all people", people=people)

@app.route("/pages/drinks", methods=["GET", "POST"])
def handle_drinks():
    if request.method == "GET":
        drinks = DrinksDbManager.get_all_drinks()
        return render_template("view_drinks.html", title="View all drinks", drinks=drinks)
    elif request.method == "POST":
        new_drink = Drink(request.form.get("name"), request.form.get("temperature"))
        print(new_drink.make_csv_line())
        new_drink_id = DrinksDbManager.create_drink(new_drink)
        print(new_drink_id)
        
        # Return fresh updated page
        drinks = DrinksDbManager.get_all_drinks()
        return render_template("view_drinks.html", title="View all drinks", drinks=drinks, updated=True)

@app.route("/pages/rounds", methods=["GET"])
def show_rounds():
    rounds = RoundsDbManager.get_all_rounds()
    return render_template("view_rounds.html", title="View all rounds", rounds=rounds)

@app.route("/pages/round", methods=["GET", "POST"])
def make_round():
    if request.method == "GET":
        people = PeopleDbManager.get_all_people()
        return render_template("make_round.html", title="Start a round", people=people)
    elif request.method == "POST":
        new_round = Round(request.form.get("owner"), datetime.now())
        new_round_id = RoundsDbManager.create_round(new_round)
        people = PeopleDbManager.get_all_people()
        return render_template("make_round.html", title="Start a round", people=people, created=True)

@app.route("/pages/order", methods=["GET", "POST"])
def order_form():
    round_id = request.args.get("round_id")
    # print(round_id)
    if request.method == "GET":     # Return the entry form
        round = RoundsDbManager.get_round(round_id)
        round.orders = RoundsDbManager.get_orders_for_round(round_id)

        people = PeopleDbManager.get_all_people()
        drinks = DrinksDbManager.get_all_drinks()

        return render_template("order_form.html", title="Place an order", people=people, drinks=drinks, round=round)
    elif request.method == "POST":  # Take user input, return the submitted form
        person_name = request.form.get("person")
        drink_name = request.form.get("drink")

        # Do something with this information
        RoundsDbManager.create_order_for_round(round_id, (person_name, drink_name))

        # Refresh orders and return updated page
        round = RoundsDbManager.get_round(round_id)
        round.orders = RoundsDbManager.get_orders_for_round(round_id)
        people = PeopleDbManager.get_all_people()
        drinks = DrinksDbManager.get_all_drinks()

        return render_template("order_form.html", title="Place an order", people=people, drinks=drinks, round=round, updated=True)

if __name__ == "__main__":
    print("Starting server")
    app.run(host="0.0.0.0", port=8081, debug=True)
    