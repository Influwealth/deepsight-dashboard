import streamlit as st
import subprocess
import yaml

st.set_page_config(page_title="DeepSight AI Command Center", layout="wide")
st.title("🚀 DeepSight AI Command Center")

# Load agent configuration
try:
    with open("agents_config.yaml", "r") as file:
        config = yaml.safe_load(file)
except Exception as e:
    st.error(f"Failed to load agent config: {e}")
    config = {"agents": []}

# Display each agent as a collapsible section
for agent in config.get("agents", []):
    with st.expander(agent['name']):
        st.write(f"**Role:** {agent.get('role', 'N/A')}")
        st.write(f"**Tools:** {', '.join(agent.get('tools', []))}")

        if st.button(f"▶️ Run {agent['name']}"):
            with st.spinner(f"Running {agent['name']}..."):
                try:
                    result = subprocess.run(["python", "run_agents.py"], capture_output=True, text=True)
                    if result.returncode == 0:
                        st.code(result.stdout)
                        st.success(f"{agent['name']} completed successfully!")
                    else:
                        st.error(f"❌ Error running {agent['name']}: {result.stderr}")
                except Exception as err:
                    st.error(f"❌ Exception occurred: {err}")

st.divider()
st.subheader("🧠 System Session State")
st.json(st.session_state)

