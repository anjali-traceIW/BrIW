from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.Round import *

class RoundsHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header("Content-type","application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        people = PeopleFileManager("data/people.csv").get_people_from_file()
        drinks = DrinksFileManager("data/drinks.csv").get_drinks_from_file()

        rounds_data_manager = RoundsFileManager("data/rounds.csv")
        rounds = rounds_data_manager.get_rounds_from_file(people, drinks)

        print(rounds.make_json_str())
        jd = json.dumps(rounds.make_json_str())
        self.wfile.write(jd.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        print(data)
        round = Round(data["owner"], data["time_started"], data["active"])
        round.orders = data["orders"]
        print(round)

        # TODO: Save round
        
        self.send_response(201)
        self.end_headers()

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, RoundsHandler)
    print("Starting server")
    httpd.serve_forever()