from datetime import datetime, date, timedelta
from typing import Union
import json
import uuid
import urllib
import uvicorn

from fastapi import FastAPI

sample_data_filepath = "./data/sample_data.json"

app = FastAPI()


@app.get("/")
def read_root(q: Union[str, None] = None):
    # renvoyer Hello World 'Synchrone' [uuid] my_uuid = uuid.uuid4()
    # ajouter un paramètre de type string à cette méthode et le renvoyer dans le json (à côté du Hello)
    my_uuid = uuid.uuid4()
    return {f"Hello {q}": f"World 'Synchrone' { my_uuid.__str__() }"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    date_compare:datetime
    filtered_tickets:list=[]

    #parse q url parameters
    # date_update=2023-10-05T14:00:00Z&user_id=3 >>>>>>>>  {'date_update': ['2023-10-05T14:00:00Z'], 'user_id': ['3']}
    params = urllib.parse.parse_qs(q)
    print(params)
    date_compare_str = params["date_update"][0]
    if date_compare_str:
        date_compare:datetime = datetime.fromisoformat(date_compare_str)

    #recupération des données de tests depuis le fichier json
    tickets:list = load_data()

    for ticket in tickets:
        date_creation:datetime =  datetime.fromisoformat(ticket["creation_date"])
        if date_compare.timestamp() > date_creation.timestamp():
            filtered_tickets.append(ticket)
    
    
    # 1 identifier uniquement les dates inférieur à la date entrée
    # 2 mettre la date comme paramètre à la méthode de service

    # 3 extraire dans une méthode (def) le chargement des tickets
    # 4 retourner la liste filtrée
    # 5 gérer le paramètre q 
    

    return filtered_tickets




def load_data()->list:

    with open(sample_data_filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    #on affecte la liste des tickets en provenance du fichier
    tickets:list = data['tickets']
    return tickets




if __name__ == "__main__":
    # with open("./config/config.json", "r", encoding="utf-8") as f:
    #     config = json.load(f)
    uvicorn.run("main:app")