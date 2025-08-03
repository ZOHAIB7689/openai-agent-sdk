from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
import os


load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    """
    import requests
    print("function called.")

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f"The current temperature in {city} is {data['current']['temp_c']}°C."
    else:
        return "Could not retrieve weather data."

agent = Agent(
    name="WeatherAgent",
    instructions="An agent that provides current weather information.",
    tools=[get_weather],
)

user_input = input("how can i assist you today? =>")
runner = Runner.run_sync(agent, user_input)
print(runner.final_output)