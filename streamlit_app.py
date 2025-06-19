
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import json
from utils.progress_tracker import save_progress, get_user_progress

# Custom Page Config
st.set_page_config(page_title="📘 StudySync AI", page_icon="📘", layout="wide")

# Custom Header with Emoji
st.markdown(
    """
    <h1 style='text-align: center;'>📘 StudySync AI</h1>
    <h4 style='text-align: center; color: gray;'>Your Personalized AI Study Planner</h4>
    """, unsafe_allow_html=True
)

# OpenAI Setup
llm = ChatOpenAI(openai_api_key=st.secrets["openai"]["openai_api_key"], temperature=0.5, model_name="gpt-3.5-turbo")

# User Inputs
st.sidebar.header("🛠️ Customize Your Plan")
goal = st.sidebar.text_input("🎯 What do you want to learn?")
days = st.sidebar.slider("📆 Duration (days)", 7, 90, 30)
hours_per_day = st.sidebar.selectbox("⏰ Daily Study Time (hours)", [1, 2, 3, 4])
email = st.sidebar.text_input("👤 Enter your name or email (for saving progress):")

if st.sidebar.button("📅 Generate Study Plan"):
    with st.spinner("🧠 Thinking..."):
        prompt = PromptTemplate.from_template(
            "Create a {days}-day study plan to learn {goal}. Each day should have a topic, estimated time ({hours}h/day), and 2–3 free online resources like videos or GitHub links."
        )
        query = prompt.format(goal=goal, days=days, hours=hours_per_day)
        response = llm.predict(query)
        st.session_state["plan"] = response
        st.session_state["user_email"] = email
        st.success("✅ Study plan generated!")
        st.markdown("### 🗂️ Your Study Plan")
        st.markdown(response)

# Progress Tracker
if "plan" in st.session_state:
    st.divider()
    st.markdown("### ✅ Track Your Progress")
    progress = get_user_progress(st.session_state["user_email"])
    cols = st.columns(5)
    for i in range(1, days + 1):
        key = f"Day {i}"
        completed = progress.get(key, False)
        with cols[(i - 1) % 5]:
            if st.checkbox(f"{key}", value=completed, key=key):
                save_progress(st.session_state["user_email"], key, True)

    st.markdown("### 📥 Download Your Plan")
    st.download_button("📄 Download Plan as Text", st.session_state["plan"], file_name="study_plan.txt")

# Footer
st.markdown("""<hr><div style='text-align:center'>💡 Made with LangChain, Streamlit & OpenAI | © 2025 StudySync AI</div>""", unsafe_allow_html=True)
