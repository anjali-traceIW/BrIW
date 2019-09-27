from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.DbManager import *
from src.cls.Round import *

class RoundsHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header("Content-type","application/json")
        self.end_headers()

    def do_GET(self, RoundsDbManager):
        self._set_headers(200)

        people = PeopleFileManager("data/people.csv").get_people_from_file()
        drinks = DrinksFileManager("data/drinks.csv").get_drinks_from_file()

        rounds_data_manager = RoundsDbManager()
        rounds = rounds_data_manager.get_all_rounds()

        print(rounds.make_json_obj())
        jd = json.dumps(rounds.make_json_obj())
        self.wfile.write(jd.encode("utf-8"))

    def do_POST(self, RoundsDbManager):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        print(data)
        round = Round(data["owner"], data["time_started"], data["active"])
        round.orders = data["orders"]
        print(round)

        RoundsDbManager.add_round(round)
        
        self.send_response(201)
        self.end_headers()

class HtmlHandler(BaseHTTPRequestHandler):

    def do_GET(self, DrinksDbManager=DrinksDbManager):
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
    server_address = ("0.0.0.0", 8081)
    # httpd = HTTPServer(server_address, RoundsHandler)
    httpd = HTTPServer(server_address, HtmlHandler)
    print("Starting server")
    httpd.serve_forever()