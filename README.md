# AI Assistant with LangChain, Groq & MCP

This project is an AI Assistant built using **LangChain**, **LangChain-Groq**, and **FastAPI**, enhanced with **MCP servers** for additional functionality such as web automation, weather data, and academic paper search.  

---

## **Features**

- Conversational AI using **Groq Chat model**  
- Exposed API endpoints via **FastAPI**  
- Asynchronous communication using **aiohttp** and **WebSockets**  
- Environment-based configuration via **python-dotenv**  
- Integration with **MCP servers**: browser automation, weather API, and Semantic Scholar API  

---

## **Tools & Technologies**

### **AI & LLM Frameworks**
- **LangChain** → Orchestrates language models, chains, and memory  
- **LangChain-Groq** → Provides Groq Chat model integration  

### **Web & API Frameworks**
- **FastAPI** → Serves the AI Assistant as HTTP endpoints  
- **Uvicorn** → ASGI server to run FastAPI apps  
- **aiohttp & websockets** → For asynchronous HTTP requests and real-time communication  

### **Environment & Dependency Management**
- **python-dotenv** → Loads API keys and environment variables from `.env`  
- **venv** → Isolated Python virtual environment for dependencies  

### **MCP (Modular Chat Platform) Tools**
- **mcp-use** → Manages and runs multiple MCP agents locally or remotely  
- **MCP Servers in this project:**
  - **Playwright MCP Server** → Browser automation and web scraping  
  - **MCP Weather Server** → Fetches weather information dynamically  
  - **MCP Semantic Scholar Server** → Academic paper metadata and search  

> **Note:** API keys are stored in `.env` and should never be pushed to GitHub. Use `.env.example` with placeholders for sharing.  

---

## **Project Structure**
```bash
AIAssistantWithMCP/
│ app.py # FastAPI entrypoint
│ requirements.txt # Python dependencies
│ .env # Environment variables (API keys)
│ venv/ # Virtual environment
│ README.md
│
├── mcp_servers/ # MCP server configurations
└── modules/ # Custom Python modules (if any)
```



## **Installation**

```bash
# 1. Clone the repo
git clone https://github.com/maryemchk/ai-assistant-mcp.git
cd ai-assistant-mcp

# 2. Create a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# OR
source venv/bin/activate      # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file from template
copy .env.example .env
# Fill in your API keys
```
---

## License

MIT License

---

## Acknowledgements

- [LangChain](https://www.langchain.com/)  
- [Groq](https://www.groq.com/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [MCP](https://github.com/modular-chat-platform/mcp)


