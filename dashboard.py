import streamlit as st
import subprocess
import yaml

st.set_page_config(page_title="DeepSight Dashboard", layout="wide")
st.title("🚀 DeepSight AI Command Center")

try:
    with open("agents_config.yaml", "r") as file:
        config = yaml.safe_load(file)
except Exception as e:
    st.error(f"Failed to load agent config: {e}")
    config = {"agents": []}

for agent in config.get("agents", []):
    with st.expander(agent['name']):
        st.write(f"**Role:** {agent['role']}")
        st.write(f"**Tools:** {', '.join(agent['tools'])}")
        if st.button(f"▶️ Run {agent['name']}"):
            st.success(f"{agent['name']} triggered (simulated).")

st.divider()
st.subheader("🧪 Session State")
st.json(st.session_state)
