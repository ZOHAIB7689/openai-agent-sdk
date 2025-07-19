from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def read_task(filepath):
    with open(filepath, "r",  encoding="utf-8") as f:
        return f.read()


def summarize_task(tasks):
    prompt = f"""
    You are a smart task planing agent.
    Given a list of tasks, summarize them into 3 priority
    buckets:
    -High Priority
    -Medium Priority
    -Low Priority

    also translate it into urdu language and give response in urdu
    Tasks:
    {tasks}
    Return the response in this format:
    Hight Priority:
    - task 1
    - task 2

    Medium Priority:
    - task 1
    - task 2

    Low Priority:
    - task 1
    - task 2
    """

    response = client.chat.completions.create(
        model="gpt-4.1-nano",  # Use GPT-4.1-Nano (aka o4-mini)
        messages =[{"role": "user", "content":prompt}]
    )
    

    return response.choices[0].message.content


if __name__== "__main__":
    task_text = read_task("task.txt")
    summary = summarize_task(task_text)
    print("\n Summary \n")
    print("-"* 30)
    print(summary)