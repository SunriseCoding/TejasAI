import json

prompt = input("Enter a prompt: ")

def generate(prompt):
    with open("data.json", "r") as dataFile:
        loadedData = json.load(dataFile)
        print(loadedData["bye"]["bye"])

print(generate(prompt))
