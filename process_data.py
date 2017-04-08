import numpy as np
import csv
import requests


def process(data_path, url):
    # TODO: write directly to database, not through HTTP API, as it is too slow for this large data
    # TODO: add precomputed cluster labels to data
    print("Processing..")
    with open(data_path, 'r') as f:
        firstrow = True
        labels = list()
        data = dict()
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if firstrow is True:
                for item in row:
                    labels.append(item.lower())
                firstrow = False
                continue
            d = dict()
            j = None
            for item, label in zip(row, labels):
                if label == "jarnro":
                    j = item
                elif len(item) > 0:
                    d[label] = item
            data[j] = d
            if len(data.items()) == 1000:
                query_db(data, url)
                data = dict()
                break   # use small data for now


def query_db(json_data, url):
    response = requests.post(url, json=json_data)
    print(response.text)


if __name__ == "__main__":
    data_path = "./data/data.csv"
    url_add = "http://127.0.0.1:8000/boats/add"
    url_list = "http://127.0.0.1:8000/boats/list"
    process(data_path, url_add)
    query_db({"kayttokunta_koodi": 47}, url_list)

