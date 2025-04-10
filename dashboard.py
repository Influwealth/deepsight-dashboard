import streamlit as st
import yaml
import time

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
        tools_list = agent.get("tools", [])
        st.write(f"**Tools:** {', '.join(tools_list)}")

        if st.button(f"▶️ Run {agent['name']}"):
            st.success(f"{agent['name']} is running...")
            
            # Simulate live logs
            log_placeholder = st.empty()
            log_messages = [
                f"✅ Initializing {agent['name']}...",
                f"⚙️ Loading tools: {', '.join(tools_list)}",
                f"🚀 Executing tasks for {agent['name']}...",
                f"✅ Task completed for {agent['name']}."
            ]
            
            for message in log_messages:
                log_placeholder.text(message)
                time.sleep(1)  # Simulate processing time
            
            st.info(f"✅ Simulated response: {agent['name']} completed its task.")

