from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.ine.es/jaxiT3/Datos.htm?t=25171#!tabs-tabla"
req = requests.get(url)
html = BeautifulSoup(req.text, "html.parser")
table = html.find("table")
header = []
print(table)
for cols in table.findAll('th', {'class':["r1", "cols"]}):
    # print(cols)
    header.append(cols)
print(header)
