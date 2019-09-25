from http.server import HttpServer, BaseHTTPRequestHandler
import json
from src.cls.FileManager import DrinksFileManager
from Person import *

class PersonHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header("Content-type","application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        drinks_data_manager = DrinksFileManager(" ")
        drinks = drinks_data_manager.get_drinks_from_db()

        jd = json.dumps(drinks,)
        self.wfile.write(jd.encode("utf-8"))
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length), object_hook=person_decoder)
        person = Person(data["first_name"], data["surname"], data["age"])
        
        save_person(person)
        
        self.send_response(200)

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, PersonHandler)
    print("Starting server")
    httpd.serve_forever()