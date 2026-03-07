import requests
import os
from datetime import datetime

url = "https://zenquotes.io/api/random"
print("\n--- Welcome to MotivZen 🍃 ---\n")
filePath = input(r"(Optional) Enter the path where you want to save the citation: ")
if filePath == "":
    filePath = "citations"

def get_quote():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{data[0]['q']} \n-{data[0]['a']}"
    else:
        print("\nError: couldn't connect to API")
        return None

def download(content):
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    
    time_str = datetime.now().strftime("%d-%m-%Y_%H%M%S")
    fileName = f"citation_{time_str}.txt"
    fullPath = os.path.join(filePath, fileName)
    
    with open(fullPath, 'w', encoding='utf-8') as file:
        file.write(content)
        print(f"File created: {fullPath}")
try:
    while True:
        option = input("\nGenerate a quote? (Y/N): ").upper()

        if option == "Y":
            quote = get_quote()
            if quote:
                print(f"\n{quote}\n")
                download(quote)
        elif option == "N" or option == "":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option, please type Y or N.")
except KeyboardInterrupt:
    print("\nGoodbye!")
