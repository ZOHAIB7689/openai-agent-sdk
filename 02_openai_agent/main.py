from agents import Agent, Runner 
from dotenv import load_dotenv
import os



agent =Agent(
    name = "plant growth tracker"
    instructions = "Track the growth of plants and provide care tips based on their current state.",
    model = "gpt-4o-mini",
)