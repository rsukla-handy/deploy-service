import yaml
import requests
from mountebank import *
import json

def load_yaml_file():
    with open("consumer.yaml") as data1:
        consumer_data = json.dumps(yaml.load(data1))
    with open("sales.yaml") as data2:
        sales_data = json.dumps(yaml.load(data2))
    return consumer_data, sales_data


def test_accounting_service():
    consumer_data, sales_data = load_yaml_file()
    consumer_service = Microservice(consumer_data)
    sales_service = Microservice(sales_data)


test_accounting_service()
