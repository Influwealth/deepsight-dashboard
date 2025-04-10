import yaml

def run():
    try:
        with open("agents_config.yaml", "r") as file:
            agents = yaml.safe_load(file)["agents"]
    except Exception as e:
        print(f"Error loading agents_config.yaml: {e}")
        return

    for agent in agents:
        print(f"🚀 Running {agent['name']} | Tools: {', '.join(agent['tools'])}")

if __name__ == "__main__":
    run()
