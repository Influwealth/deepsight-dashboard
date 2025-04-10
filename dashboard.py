import streamlit as st
import subprocess
import yaml

st.set_page_config(page_title="DeepSight AI Command Center", layout="wide")
st.title("🚀 DeepSight AI Command Center")

try:
    with open("agents_config.yaml", "r") as file:
        config = yaml.safe_load(file)
except Exception as e:
    st.error(f"⚠️ Could not load agents config: {e}")
    config = {"agents": []}

for agent in config.get("agents", []):
    with st.expander(agent["name"]):
        st.write(f"**Role:** {agent.get('role', 'N/A')}")
        st.write(f"**Tools:** {', '.join(agent.get('tools']) or [])}")

        if st.button(f"▶️ Run {agent['name']}"):
            with st.spinner("Running..."):
                try:
                    result = subprocess.run(["python", "run_agents.py"], capture_output=True, text=True)
                    st.code(result.stdout)
                    if result.returncode == 0:
                        st.success(f"{agent['name']} executed successfully!")
                    else:
                        st.error(f"Agent failed:\n{result.stderr}")
                except Exception as e:
                    st.error(f"❌ Error: {e}")


