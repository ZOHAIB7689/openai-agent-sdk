from agents import Agent, Runner 
from dotenv import load_dotenv
import os

load_dotenv()

agent =Agent(
    name = "plant growth tracker",
    instructions = "Track the growth of plants and provide care tips based on their current state.",
    model = "gpt-4o-mini",
)

user_input = input("Please enter your query: ")

result = Runner.run_sync(agent, user_input)

print(result)
