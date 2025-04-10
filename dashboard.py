import streamlit as st
import yaml

st.set_page_config(page_title="DeepSight AI Command Center", layout="wide")
st.title("🚀 DeepSight AI Command Center")

# Load agent config
try:
    with open("agents_config.yaml", "r") as file:
        config = yaml.safe_load(file)
except Exception as e:
    st.error(f"⚠️ Failed to load agents_config.yaml: {e}")
    config = {"agents": []}

# UI for each agent
for agent in config.get("agents", []):
    with st.expander(agent["name"]):
        st.write(f"**Role:** {agent.get('role', 'N/A')}")
        st.write(f"**Tools:** {', '.join(agent.get('tools', []))}")

        if st.button(f"▶️ Run {agent['name']}"):
            st.success(f"{agent['name']} is running...")
            st.info(f"✅ Simulated response: {agent['name']} completed its task.")