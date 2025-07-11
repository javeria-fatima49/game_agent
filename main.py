# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# from narrator_agent import NarratorAgent
# from monster_agent import MonsterAgent
# from item_agent import ItemAgent

# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key=API_KEY)
# model = genai.GenerativeModel("gemini-1.5-flash")

# narrator = NarratorAgent(model)
# monster = MonsterAgent()
# item = ItemAgent()

# st.set_page_config(page_title="🧙 Fantasy Adventure Game", layout="centered")
# st.title("🧝 Game Master Agent")
# st.markdown("""
# Welcome to the fantasy realm! Choose your path and let your adventure unfold.
# """)

# if "history" not in st.session_state:
#     st.session_state.history = []

# user_input = st.text_input("What would you like to do? (e.g. Enter cave, Fight goblin, Drink potion)")

# if st.button("Submit Action") and user_input:
#     st.session_state.history.append(f"🧍 You: {user_input}")

#     story = narrator.narrate(user_input)
#     st.session_state.history.append("📖 Story: " + story)

#     if "fight" in user_input.lower() or "monster" in user_input.lower():
#         outcome = monster.attack()
#         st.session_state.history.append(outcome)
#     else:
#         reward = item.reward()
#         st.session_state.history.append(reward)

# for msg in st.session_state.history[::-1]:
#     st.markdown(msg)


import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

from narrator_agent import NarratorAgent
from monster_agent import MonsterAgent
from item_agent import ItemAgent

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

narrator = NarratorAgent(model)
monster = MonsterAgent(model)   
item = ItemAgent(model)        

st.set_page_config(page_title="🧙 Fantasy Adventure Game", layout="centered")
st.title("🧝‍♂️ Game Master Agent - Fantasy Adventure")
st.markdown("Welcome to the fantasy realm! Choose your path and let your story unfold. 🌟")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input(
    "🗨️ What will you do?",
    placeholder="Enter cave, Fight goblin, Drink potion..."
)

if st.button("Submit Action") and user_input:
    st.session_state.history.append(f"🧍 You: {user_input}")

    if user_input.strip().lower() in ["thanks", "thank you", "shukriya"]:
        st.session_state.history.append("🤗 You're welcome, brave adventurer!")

    else:
        story = narrator.narrate(user_input)
        st.session_state.history.append("📖 Story: " + story)

        if any(word in user_input.lower() for word in ["fight", "monster", "attack", "battle", "kill", "strike", "slay"]):
            outcome = monster.run(user_input)  # ✅ Fixed
            st.session_state.history.append(outcome)

        if any(word in user_input.lower() for word in ["open", "search", "loot", "drink", "explore", "check", "use", "take"]):
            reward = item.reward(user_input)   # ✅ Fixed
            st.session_state.history.append(reward)

for msg in st.session_state.history[::-1]:
    st.markdown(msg)

st.markdown("---")
st.markdown("🛠️ Powered by Streamlit + Gemini + Multi-Agent Logic")
