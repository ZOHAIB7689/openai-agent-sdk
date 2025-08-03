from agents import Agent, Runner , WebSearchTool
from dotenv import load_dotenv


load_dotenv()


my_agent = Agent(
    name= "Currency Converter",
    instructions= "Converts currencies using real-time exchange rates.",
    tools=[WebSearchTool()],
    model="gpt-4.1",
)

user_input = input("Enter two currency values to get exchange rates: ")

result = Runner.run_sync(my_agent,user_input)

print(result.final_output)