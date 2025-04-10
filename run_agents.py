import yaml

def run():
    with open("agents_config.yaml", "r") as file:
        agents = yaml.safe_load(file)["agents"]
    for agent in agents:
        print(f"Running agent: {agent['name']} with tools {agent['tools']}")

if __name__ == "__main__":
    run()