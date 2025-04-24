import json

sample_data_filepath = "./data/sample_data.json"


def load_data()->list:

    with open(sample_data_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    #on affecte la liste des tickets en provenance du fichier
    tickets:list = data['tickets']
    return tickets