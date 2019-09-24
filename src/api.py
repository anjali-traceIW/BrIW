from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import *
from src.cls.Drink import *

class DrinksHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header("Content-type","application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        drinks_data_manager = DrinksFileManager("data/drinks.csv")
        drinks = drinks_data_manager.get_drinks_from_file()

        print(drinks.make_json_str())
        jd = json.dumps(drinks.make_json_str())
        self.wfile.write(jd.encode("utf-8"))
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length), object_hook=person_decoder)
        person = Person(data["first_name"], data["surname"], data["age"])
        
        save_person(person)
        
        self.send_response(200)

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, DrinksHandler)
    print("Starting server")
    httpd.serve_forever()