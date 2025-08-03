from agents import Agent, Runner 
import asyncio
from dotenv import load_dotenv

load_dotenv()
sindhi_agent = Agent(
    name="Sindhi Agent",
    instructions="you are an assistant agent your work is to convert user propmt in roman sindhi language",
    model="gpt-4.1",
)



urdu_agent = Agent(
    name="urdu Agent",
    instructions="you are an assistant agent your work is to convert user propmt in roman urdu language",
    model="gpt-4.1",
)

balochi_agent = Agent(
    name="balochi Agent",
    instructions="you are an assistant agent your work is to convert user propmt in roman balochi language",
    model="gpt-4.1",
)


pashto_agent = Agent(
    name="pashto Agent",
    instructions="you are an assistant agent your work is to convert user propmt in roman  pushto language",
    model="gpt-4.1",
)


orchestrator_agent = Agent(
    name="Orchestrator Agent",
    instructions=
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools. also tell which agent you are using",
    model="gpt-4.1",
    tools=[sindhi_agent.as_tool(
        tool_name="translate_to_sindhi",
        tool_description="Translate user's message to Roman Sindhi language"
    ),
    urdu_agent.as_tool(
        tool_name="translate_to_urdu",
        tool_description="Translate user's message to Roman Urdu language"),
        balochi_agent.as_tool(
            tool_name="translate_to_balochi",
            tool_description="translate user's messgae to roman balochi language"
        ),
        pashto_agent.as_tool(
            tool_name="translate_to_pashto",
            tool_description="translate user's message to roman pashto language"
        )
    ]
)

user_input= input("what do you want to translate and to which language: ")

async def main():
    result = await Runner.run(orchestrator_agent, user_input)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())