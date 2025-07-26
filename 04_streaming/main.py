import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv()

async def main():
    agent =Agent(
        name = "Jarvis",
        instructions = "You are helpful agent like jarvis of tony stark",
        model= "gpt-4.1-nano"
    )
    user_input = input("Enter your query: ")

    result = Runner.run_streamed(agent, user_input )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


if __name__== "__main__":
    asyncio.run(main())