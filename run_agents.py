import yaml
import time

def run():
    with open("agents_config.yaml", "r") as file:
        agents = yaml.safe_load(file)["agents"]
    for agent in agents:
        print(f"🧠 {agent['name']} starting task...")
        time.sleep(1)
        print(f"🔧 Tools used: {', '.join(agent['tools'])}")
        print(f"✅ {agent['name']} completed successfully!\n")

if __name__ == "__main__":
    run()
