import plotly.express as px
import csv
import numpy as np

def pf(data_path):
    with open(data_path) as csv_file:
        rag = csv.DictReader(csv_file)
        idk = px.scatter(rag,x="Days Present", y="Marks In Percentage")
        idk.show()

def getDataSource(data_path):
    marks = []
    daysP = []
    with open(data_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            marks.append(float(row["Marks In Percentage"]))
            daysP.append(float(row["Days Present"]))

    return {"x" : marks, "y": daysP}

def find(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    find(datasource)
    pf(data_path)

setup()
