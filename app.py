
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/dialogue"

st.set_page_config(page_title="Project Socrates", page_icon="🧠")
st.title("🧠 Project Socrates — Socratic Dialogue Tutor")
st.caption("Learn to think by being asked better questions. The system never hands out direct answers.")

if "history" not in st.session_state:
    st.session_state.history = []

with st.form("query_form"):
    topic = st.text_input("Enter a question or claim you want to explore:")
    complexity = st.selectbox("Depth of questioning", ["low", "medium", "high"], index=1)
    submitted = st.form_submit_button("Ask Socrates")

if submitted and topic.strip():
    st.session_state.history.append(("You", topic))
    payload = {"question": topic, "complexity": complexity}
    try:
        resp = requests.post(API_URL, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        ai_text = data.get("response", "Can you say more about that?")
        trace = data.get("reasoning_trace", {})
        st.session_state.history.append(("Socrates", ai_text))
        st.info(ai_text)
        with st.expander("View reasoning trace and feedback"):
            st.json(trace)
    except Exception as e:
        st.error(f"Server error: {e}")

for who, text in st.session_state.history:
    if who == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Socrates:** {text}")
