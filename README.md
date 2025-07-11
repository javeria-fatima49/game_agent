"# game_agent" 
# 🧙 Game Master Agent – Fantasy Adventure Game

Welcome to your own **text-based fantasy world** powered by **AI agents and Gemini**. Embark on epic adventures, face terrifying monsters, find magical treasures, and let your story unfold – all from a simple input.

> 🔥 Built using Streamlit + Gemini + Multi-Agent Logic  
> 🎯 Assignment-ready & deployable on GitHub + Streamlit Cloud

---

## 🌟 Features

- 🎮 **Narrative-Driven Game**: Enter caves, fight monsters, open chests, and create your own fantasy journey.
- 🧠 **AI-Powered Agents**:
  - **NarratorAgent** – Builds immersive story from your input
  - **MonsterAgent** – Handles AI-based monster battles (with dice rolls)
  - **ItemAgent** – Generates random magical rewards
- 🎲 **Tools Integration**: 
  - `roll_dice()` – Simulates dice rolls for action outcomes
  - `generate_event()` – Creates random reward encounters
- ✨ **Gemini Model Integration** (Gemini 1.5 Flash)
- 🖥️ **Streamlit UI** – Responsive, clean, and interactive

---

## 🚀 How to Run Locally

### 🔧 Prerequisites

- Python 3.10+
- [Gemini API Key](https://aistudio.google.com/app/apikey)

---

### 📦 Installation Steps

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/game-master-agent.git
cd game-master-agent

# Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate   # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
🔐 Environment Setup
Create a .env file and add your Gemini API key:

env
Copy
Edit
GEMINI_API_KEY=your_google_gemini_api_key
🧠 Run the App
bash
Copy
Edit
streamlit run main.py
💡 Tip: Make sure your Gemini quota is not exceeded (Daily limit)

🗂️ Project Structure
bash
Copy
Edit
game-master-agent/
│
├── main.py                      # Streamlit UI + Game Flow
├── narrator_agent.py            # Handles narrative logic
├── monster_agent.py             # Handles battle logic
├── item_agent.py                # Handles rewards logic
│
├── tools/
│   ├── roll_dice.py             # Dice roll tool
│   └── generate_event.py        # Random reward generator
│
├── .env                         # Your API key (should be in .gitignore)
├── requirements.txt             # Dependencies
└── README.md                    # You're reading it! ❤️
🧪 Example Prompts to Try
Type	Sample Input
🗺️ Exploration	Enter the dark cave
⚔️ Combat	Fight the skeleton with my sword
💎 Reward	Open the golden chest
🧙 Misc	Drink potion from the fountain
🙏 Polite	Thank you → "You're welcome, brave adventurer!"

📸 UI Preview
(Add screenshot here of your Streamlit app)
Use st.image("screenshot.png") in your app if needed.

📈 Future Plans (Optional)
Save game state across sessions

Add character customization

Integrate voice input using Whisper API

Deploy on mobile with Streamlit Community Cloud

🙌 Credits
Developed by Javeria Fatima 🌸
Mentors: Sir Bilal, Sir Ali Aftab, Sir Zia Khan
Part of the GIAIC Agentic AI Assignment Series