import yaml

servers = {"flask_server": "0.0.0.0", "mongo_server": "0.0.0.0", "elasticsearch": "0.0.0.0"}
config = 0

# Reading Terraform output file
with open ("../../terraform/servers.txt", "r") as file:
    for line in file:
        if not line.split()[0].find("flask", 0):
            servers["flask_server"] = line.split()[2]
        if not line.split()[0].find("mongo"):
            servers["mongo_server"] = line.split()[2]
        if not line.split()[0].find("elastic"):
            servers["elasticsearch"] = line.split()[2]
        if not line.split()[0].find("kibana"):
            servers["kibana"] = line.split()[2]

# Reading Ansible inventory    
with open ("../../ansible/inventory.yaml", "r") as file:
    config = yaml.safe_load(file)
    config["flask_servers"]["hosts"]["flask_server"]["ansible_host"] = servers["flask_server"]
    config["mongo_servers"]["hosts"]["mongo_server"]["ansible_host"] = servers["mongo_server"]
    config["elastic_servers"]["hosts"]["elasticsearch"]["ansible_host"] = servers["elasticsearch"]
    config["kibana_servers"]["hosts"]["kibana"]["ansible_host"] = servers["kibana"]
    config["flask_servers"]["vars"]["elasticsearch_host"] = servers["elasticsearch"]
    config["kibana_servers"]["vars"]["elasticsearch_host"] = servers["elasticsearch"]

# Writing to Ansible inventory
with open ("../../ansible/inventory.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style = False)
    print("Ansible inventory is updated:")
    print(config)
    print("----")

with open ("../source/dbconfig.yaml", "r+") as file:
    text ="""\
    db:
        host: 0.0.0.0
        port: 27017
        name: "quotes"
        collection: "collection"  
    """
    config = yaml.safe_load(text)
    config["db"]["host"] = servers["mongo_server"]
    yaml.dump(config, file, default_flow_style = False)
    print("Database config is updated:")
    print(config)
    print("----")