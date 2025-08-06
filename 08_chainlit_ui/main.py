import chainlit as cl
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


@cl.on_chat_start
async def main():
     await cl.Message(content="Welcome to the Translation Agent! Please enter your text and specify the target language (sindhi, urdu, balochi, pashto).").send()

@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    result = await Runner.run(orchestrator_agent, user_input)
    # await cl.Message(content="Got translation result!").send()  # Debug line

    await cl.Message(content=result.final_output).send()