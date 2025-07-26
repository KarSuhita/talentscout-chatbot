import streamlit as st
from utils import generate_questions

st.set_page_config(page_title="TalentScout Assistant", page_icon="🤖")

# Page Title
st.title("🤖 TalentScout Hiring Assistant")
st.caption("Helping candidates prepare for interviews and collect their info.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = "greeting"

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

# Core chatbot logic
def get_bot_response(user_input):
    step = st.session_state.step

    # Exit handling
    if user_input.lower() in ["exit", "bye", "thank you"]:
        st.session_state.step = "done"
        return "🎉 Thanks for chatting! All the best for your journey ahead."

    if user_input.lower() == "restart":
        st.session_state.step = "greeting"
        st.session_state.messages.clear()
        return "🔄 Conversation restarted. Let's go again!"

    # Steps
    if step == "greeting":
        st.session_state.step = "collect_name"
        return "👋 Welcome to TalentScout Hiring Assistant!\n\nI'll help you prepare for interviews and collect your details.\n\nWhat's your **full name**?"

    elif step == "collect_name":
        st.session_state.candidate["name"] = user_input
        st.session_state.step = "collect_email"
        return "📧 Great! What's your **email address**?"

    elif step == "collect_email":
        st.session_state.candidate["email"] = user_input
        st.session_state.step = "collect_phone"
        return "📱 Got it. What's your **phone number**?"

    elif step == "collect_phone":
        st.session_state.candidate["phone"] = user_input
        st.session_state.step = "collect_experience"
        return "💼 How many years of **experience** do you have?"

    elif step == "collect_experience":
        st.session_state.candidate["experience"] = user_input
        st.session_state.step = "collect_roles"
        return "🧑‍💼 What **roles** are you applying for?"

    elif step == "collect_roles":
        st.session_state.candidate["roles"] = user_input
        st.session_state.step = "collect_location"
        return "🌍 Which **location** are you applying from?"

    elif step == "collect_location":
        st.session_state.candidate["location"] = user_input
        st.session_state.step = "collect_tech_stack"
        return "💻 Now tell me your **tech stack** one by one (e.g., Python, React, MySQL).\nType `done` when finished."

    elif step == "collect_tech_stack":
        if user_input.lower() == "done":
            st.session_state.step = "done"
            return "✅ Thank you! We've collected your info and generated questions.\nYou can now close the assistant or type `restart` to begin again."
        else:
            questions = generate_questions(user_input)
            return f"🧠 Here are some interview questions for **{user_input}**:\n\n{questions}"

    elif step == "done":
        return "✅ You're all set! Type `restart` if you'd like to start over."

    # Fallback
    return "❓ I didn't quite get that. Please try again or type `restart`."

# Display messages
for user_msg, bot_msg in st.session_state.messages:
    st.chat_message("user").markdown(user_msg)
    st.chat_message("assistant").markdown(bot_msg)

# Chat input
user_input = st.chat_input("Type your response...")

if user_input:
    st.chat_message("user").markdown(user_input)
    bot_response = get_bot_response(user_input)
    st.chat_message("assistant").markdown(bot_response)
    st.session_state.messages.append((user_input, bot_response))
