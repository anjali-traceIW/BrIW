from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.DbManager import *
from src.cls.Round import *
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route("/rounds", methods=["GET"])
def get_all_rounds(RoundsDbManager=RoundsDbManager):
#       people = service.get_all_people()
#   return jsonify([person.to_json() for person in people])

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
        RoundsDbManager.add_round(round)
    except Exception as e:
        return Response(response=e,status=500)

    return Response(response="Successfully added round.",status=200)

@app.route("/pages", methods=["GET"])
def get_drinks_html(self, DrinksDbManager=DrinksDbManager):
    self.send_response(200)

    drinks_data_manager = DrinksDbManager()
    drinks = drinks_data_manager.get_all_drinks()

    self.send_header("content-type", "text/html")
    self.end_headers()
    
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
    self.wfile.write(html_document.encode('utf-8'))

if __name__ == "__main__":
    print("Starting server")
    app.run(host="localhost", port=8081, debug=True)
    