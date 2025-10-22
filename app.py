"""
Simple chat example using MCPAgent with built-in conversation memory.

this example demonstrates how to use the MCPAgent with its built-in
conversation memory to maintain context across multiple messages.
    we will also use the OpenAI model to generate responses.
    we will also use the tool to search the web for information.
    we will also use the tool to search the web for information."""

import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    load_dotenv()
    #set the Groq API key
    os.environ["GRPQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    #load the MCP config file
    config_file = "browser_mcp.json"

    print(f"Initializing The chat ....")

    #create MCP Client
    client = MCPClient.from_config_file(config_file)
    # Update to use a supported model
    #llm = ChatGroq(model="llama-3.3-70b-versatile")  
    llm = ChatGroq(model="llama-3.1-8b-instant")

    #create MCPAgent with memory enabled
    agent = MCPAgent(
        llm,
        client=client,
        max_steps=15,
        memory_enabled=True
    )
    
    #start the chat
    print("Welcome to the chat! Type 'exit' to end the conversation.")
    print("--------------------------------")

    try:
        #Main chat loop
        while True:
            #get user input
            user_input = input("\nYou: ")

            #check if user wants to exit
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Goodbye!")
                break

            #check for clear history command 
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            #generate response
            print("Thinking...")
            print("\n Assistant:", end="", flush=True)

            try:
                #Run the agent with user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"Error: {e}")

    finally:
                #clean up 
                if client and client.sessions:
                    await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())



  