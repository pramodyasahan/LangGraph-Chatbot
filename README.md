Here is a well-structured `README.md` file for your project:  

---

# **LangGraph AI Chatbot**

This is a FastAPI-based chatbot API integrated with LangGraph and Streamlit for an interactive UI. The chatbot allows users to select different AI models, define system prompts, and interact with the LangGraph-based agent.

## **Features**
- 🚀 **FastAPI Backend**: Handles chatbot requests efficiently.
- 🤖 **LangGraph AI Agent**: Uses `LangChain` and `Groq` models.
- 🔍 **Tavily Search Tool**: Enhances chatbot responses with web search.
- 🖥️ **Streamlit UI**: Provides a user-friendly interface for interactions.

---

## **Tech Stack**
- **Backend**: FastAPI, LangChain, Groq, Tavily Search
- **Frontend**: Streamlit
- **Environment Management**: `dotenv`
- **Package Manager**: `pip`

---

## **Installation and Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/pramodyasahan/LangGraph-Chatbot.git
cd LangGraph-Chatbot
```

### **2. Create a Virtual Environment (Optional)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add your API keys:
```
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## **Running the Application**
### **1. Start the FastAPI Backend**
```bash
uvicorn app:app --reload
```
- The backend will be available at: `http://127.0.0.1:8000`

### **2. Start the Streamlit UI**
```bash
streamlit run ui.py
```
- The UI will open in your default browser.

---

## **API Endpoints**
### **1. Chat Endpoint**
- **URL**: `POST /chat`
- **Description**: Processes chatbot messages.
- **Request Body**:
  ```json
  {
    "model_name": "llama3-70b-8192",
    "system_prompt": "Your system instructions",
    "messages": ["Hello, how are you?"]
  }
  ```
- **Response Example**:
  ```json
  {
    "messages": [
      {
        "type": "ai",
        "content": "I'm doing great! How can I assist you today?"
      }
    ]
  }
  ```

---

## **Project Structure**
```
langgraph-chatbot/
│── app.py           # FastAPI backend
│── ui.py            # Streamlit frontend
│── requirements.txt # Required dependencies
│── .env             # Environment variables (not included in repo)
│── README.md        # Documentation
```

---

## **Contributing**
1. **Fork** the repository.
2. **Clone** the forked repository:
   ```bash
   git clone https://github.com/pramodyasahan/LangGraph-Chatbot.git
   ```
3. **Create a new branch**:
   ```bash
   git checkout -b feature-name
   ```
4. **Commit your changes**:
   ```bash
   git commit -m "feat: Added new feature"
   ```
5. **Push to GitHub**:
   ```bash
   git push origin feature-name
   ```
6. **Create a Pull Request** on GitHub.

---

## **License**
This project is licensed under the **MIT License**.

---

## **Author**
👨‍💻 Developed by **Pramodya Sahan**  
🔗 GitHub: [pramodyasahan](https://github.com/pramodyasahan)

---
