import json
import requests

def lambda_handler(event, context):
    api_key = "your_api_key_here"
    city = "New York"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    
    response = requests.get(url)
    data = response.json()
    
    temperature = data["main"]["temp"]
    
    return {
        "statusCode": 200,
        "body": f"Current NYC temperature is {temperature} degrees Fahrenheit"
    }
