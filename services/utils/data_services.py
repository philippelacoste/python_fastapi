import json

from models.exceptions import TicketAppException

sample_data_filepath = "./data/sample_data.json"

class DataFileLoadException(TicketAppException):
    pass

def load_data()->list:

    try:
        with open(sample_data_filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as ex:
        raise DataFileLoadException from ex

    #on affecte la liste des tickets en provenance du fichier
    tickets:list = data['tickets']
    return tickets


def save_data(new_tickets):
        export = {"tickets" : []}
        export["tickets"] = new_tickets
        with open(sample_data_filepath, "w", encoding="utf-8") as f:
            f.write(json.dumps(export))

#unquement qd le fichier est appelé directement en cli
if __name__ == "__main__":
    data = load_data()
    print("Hello", data)