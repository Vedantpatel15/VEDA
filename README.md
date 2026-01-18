# VEDA
LLM Chat bot using Gemini flash and Streamlit
🤖 VEDA — AI Chatbot using Gemini & Streamlit

VEDA is an intelligent conversational chatbot built using Google Gemini Flash (LLM) and Streamlit, designed to provide fast, interactive, and user-friendly AI conversations through a modern web interface.

🚀 Features

💬 Real-time conversational AI using Google Gemini Flash

🧠 Maintains chat context across messages

⚡ Fast responses with low latency

🖥️ Clean and interactive Streamlit UI

🔐 Secure API key handling using environment variables

📦 Lightweight and easy to deploy

🛠️ Tech Stack
Technology	Purpose
Python 3.11+	Core programming language
Google Gemini Flash	Large Language Model
Streamlit	Web UI framework
python-dotenv	Environment variable management
📂 Project Structure
VEDA/
│
├── main.py          # Streamlit application
├── .env             # API key configuration (not committed)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation

🔑 Prerequisites

Python 3.11 or higher

Google Generative AI API key

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Vedantpatel15/VEDA.git
cd VEDA

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here

▶️ Run the Application
streamlit run main.py


The app will be available at:

http://localhost:8501

🧠 How It Works

Streamlit handles the chat UI

User messages are sent to Gemini Flash

Responses are returned and displayed in a conversational format

Chat history is preserved using Streamlit session state

📸 Preview

A modern AI chat interface powered by Google Gemini and Streamlit.

📌 Future Enhancements

🔄 Multi-model support (OpenAI / Gemini switch)

💾 Chat history export

🎨 Theme customization

🌐 Deployment on Streamlit Cloud

🔊 Voice input support

👨‍💻 Author

Vedant Patel
SAP & Enterprise Technologies | AI & ML Enthusiast

🔗 GitHub: Vedantpatel15

📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.
