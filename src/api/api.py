from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.DbManager import *
from src.cls.Round import *
from flask import Flask, jsonify, request, Response, render_template

app = Flask(__name__)

@app.route("/rounds", methods=["GET"])
def get_all_rounds(RoundsDbManager=RoundsDbManager):

    people = PeopleFileManager("data/people.csv").get_people_from_file()
    drinks = DrinksFileManager("data/drinks.csv").get_drinks_from_file()

    rounds_data_manager = RoundsDbManager()
    rounds = rounds_data_manager.get_all_rounds()
    print(rounds)

    return jsonify([round.make_json_obj() for round in rounds])

@app.route("/rounds", methods=["POST"])
def create_a_round(RoundsDbManager=RoundsDbManager):
    data = request.get_json()
    print(data)
    round = Round(data["owner"], data["time_started"], data["active"])
    round.orders = data["orders"]
    print(round)

    try:
        round_id = RoundsDbManager.add_round(round)
    except Exception as e:
        return Response(response=e,status=500)

    return Response(response=f"Successfully added round id {round_id}.",status=200)

@app.route("/people", methods=["GET"])
def get_all_people(PeopleDbManager=PeopleDbManager):
    people = PeopleDbManager.get_all_people()
    return jsonify([person.to_json() for person in people])

@app.route("/pages/drinks", methods=["GET"])
def get_drinks_html(DrinksDbManager=DrinksDbManager):

    drinks_data_manager = DrinksDbManager()
    drinks = drinks_data_manager.get_all_drinks()
    
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
    app.run(host="localhost", port=8081, debug=True)
    