from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import time
import matplotlib.pyplot as plt
import requests
import pandas as pd
import json

app = FastAPI()
path = "graph.png"
url = "https://random-data-api.com/api/color/random_color"
app.mount("/static", StaticFiles(directory="source/static"), name="static")
templates = Jinja2Templates(directory="source/views")

def request_api(indexFake):
    time.sleep(0.6)        
    try:
        rawReceive = requests.get(url)
        rawDict = rawReceive.json()
        cleanDict = {
            "y": rawDict['id'],
            "color_name": rawDict['color_name'],
            "hex_value": rawDict['hex_value'],
            "x": indexFake
        }
        buff = pd.DataFrame([cleanDict])
        return buff
    except:
        return None

class DataToSend():
    def __init__(self):
        self.last_sent = 0
        self.colorDataframe = request_api(self.last_sent)
        

    def retrieve_data(self):
        return self.colorDataframe.iloc[[self.last_sent]]

    def increaseList(self):
        self.last_sent +=1
        list_to_concat = [self.colorDataframe , request_api(self.last_sent)]
        concatened = pd.concat(list_to_concat)
        self.colorDataframe = concatened.copy()
                
data = DataToSend()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/request_data")
def request_data():
    data.increaseList()
    value_to_send = data.retrieve_data().to_json(orient="index")
    print(value_to_send)
    return JSONResponse(value_to_send)

def saveData(rawData):
    uniques = rawData.drop_duplicates()
    result = uniques.to_json("s2.json")

def plotGraph(someData):
    plt.plot(someData)
    plt.ylabel("some numbers")
    plt.savefig("graph.png")


        
