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
git clone https://github.com/YOUR_USERNAME/game-agent.git
cd game-agent

# Install dependencies
pip install -r requirements.txt
🔐 Environment Setup
Create a .env file and add your Gemini API key:

GEMINI_API_KEY=your_google_gemini_api_key
🧠 Run the App
streamlit run main.py
💡 Tip: Make sure your Gemini quota is not exceeded (Daily limit)
```

### 📂 Project Structure
```bash
📁 game-agent-rpg/
├── 🧙 main.py → Streamlit UI & main logic
├── 📜 narrator_agent.py → Narrates fantasy scenes
├── 🧟 monster_agent.py → Handles battles via Gemini
├── 🎁 item_agent.py → Rewards & discoveries logic
├── 🧰 tools/
│ ├── 🎲 roll_dice.py → Simulates dice for combat
│ └── ✨ generate_event.py → Random item/event generator
├── 📄 .env → Gemini API Key (DO NOT COMMIT)
└── 📘 README.md → Project overview & usage
```

## 💡 How It Works

1. The user inputs a fantasy action (e.g., *"Enter the cave"* or *"Fight the goblin"*).
2. `NarratorAgent` uses the Gemini model to narrate what happens next.
3. If the action includes combat (e.g., *fight*, *battle*), `MonsterAgent` rolls a dice and generates an AI-powered battle result.
4. If the action is exploratory (e.g., *open*, *search*, *drink*), `ItemAgent` generates a reward or magical item using Gemini.
5. All messages are displayed chronologically using `Streamlit` with memory of session actions.

---

## 🧪 Sample Player Inputs

You can try these sample actions to test the game:

- `Enter cave`
- `Fight goblin`
- `Search treasure chest`
- `Drink from the fountain`
- `Use magic scroll`
- `Attack the orc`
- `Open mysterious box`

---

## 🙌 Credits

Developed by Javeria Fatima 🌸
Mentors: Sir Bilal, Sir Ali Aftab, Sir Zia Khan
Part of the GIAIC Agentic AI Assignment Series
