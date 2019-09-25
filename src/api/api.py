from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.Round import *

class RoundssHandler(BaseHTTPRequestHandler):
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

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, RoundssHandler)
    print("Starting server")
    httpd.serve_forever()