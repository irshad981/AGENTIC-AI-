# import streamlit as st

# st.title("Hello, Streamlit!")
# st.write("If you can read this in your browser, Streamlit is working.")import streamlit as st

# st.title("Streamlit Widgets Demo")

# name = st.text_input("What is your name?")

# if st.button("Say hello"):
#     if name.strip():
#         st.write(f"Hello, {name}! 👋")
#     else:
#         st.warning("Please type your name first.")

import streamlit as st

st.title("Session State Demo")

# Create the counter once; keep it across reruns
# if "count" not in st.session_state:
#     st.session_state.count = 0

# st.write(f"Button clicked **{st.session_state.count}** time(s).")

# if st.button("Click me"):
#     st.session_state.count += 1
#     st.rerun()

# import streamlit as st

# st.set_page_config(page_title="Streamlit Warmup", layout="wide")
# st.title("Main area — chat goes here")

# with st.sidebar:
#     st.header("Sidebar")
#     st.write("Buttons and dropdowns go here.")
#     if st.button("Example button"):
#         st.sidebar.success("You clicked the sidebar button!")

import streamlit as st

st.set_page_config(page_title="Echo Chat", layout="wide")
st.title("Echo Chat (no AI — just Streamlit UI practice)")

with st.sidebar:
    st.header("Sidebar")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

# Remember messages between reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show all past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Read new input from the user
if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": f"You said: {prompt}"})
    st.rerun()