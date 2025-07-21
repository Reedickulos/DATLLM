import json
import requests
import os
from rich import print
from tools.web_search import search_web  # We'll build this next

# Load config
with open("config.json") as f:
    config = json.load(f)

MODEL = config.get("model", "llama3")
USE_LOCAL = config.get("use_local_model", True)
PROMPT_FILE = config["prompt_file"]
MEMORY_FILE = config["memory_file"]

# Load system prompt
with open(PROMPT_FILE, encoding='utf-8') as f:
    system_prompt = f.read()

def call_llm(prompt):
    """Call Ollama locally"""
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": MODEL,
        "prompt": f"{system_prompt}\n\nUser: {prompt}\nAI:",
        "stream": False
    })
    return response.json()["response"]

# Optional: Save convo history later
def log_conversation(user_input, agent_reply):
    os.makedirs("logs", exist_ok=True)
    with open("logs/conversation.log", "a", encoding="utf-8") as f:
        f.write(f"USER: {user_input}\nAI: {agent_reply}\n\n")

print("[bold cyan]DAT LLM Ready.[/bold cyan] Type your message or 'exit' to quit.\n")

while True:
    user_input = input("[bold yellow]You > [/bold yellow]")

    if user_input.strip().lower() in ["exit", "quit"]:
        print("[bold red]Session Ended.[/bold red]")
        break

    if user_input.lower().startswith("search:") and config["tools"]["web_search"]:
        query = user_input.replace("search:", "").strip()
        reply = search_web(query)
    else:
        reply = call_llm(user_input)

    print(f"\n[bold green]DAT LLM:[/bold green] {reply}\n")
    log_conversation(user_input, reply)
