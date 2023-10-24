""" Client script to test app.py """
import sys
import json
import requests

def menu():
    """ the menu :) """
    print (" Hello and welcome to the JSON request-O-matic:")
    print (" Please use your keyboard to send the payload [1] [2] [3]")
    print()

    choice = input("""
                      1: payload1.json
                      2: payload2.json
                      3: payload3.json
                      Q: Quit

                      Please enter your choice: """)

    if choice == "1":
        load_json(choice)
    elif choice == "2":
        load_json(choice)
    elif choice == "3":
        load_json(choice)
    elif choice in ("Q","q"):
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def load_json(option):
    """ This function selects between the 3 given json files"""
    url = "http://localhost:8888/productionplan"
    if option == "1":
        make_request(url,"example_payloads/payload1.json")
    elif option == "2":
        make_request(url,"example_payloads/payload2.json")
    elif option == "3":
        make_request(url,"example_payloads/payload3.json")
    else:
        print("that option is not an option ...")

def make_request(url,json_file_path):
    """ This functions performs the request"""
    with open(json_file_path, encoding="utf-8") as file:
        res = requests.post(url, json=json.load(file), timeout=100)
        if res.ok:
            print(res.json())
        else:
            print("Error in request")

menu()
