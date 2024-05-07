import requests

#_API_URL = "http://localhost:7200/rest/"
_SERVER= "http://34.163.171.165:8080/"
_GRAPHDBSERVER= "http://34.163.171.165:7200/"
#_SERVER= "http://localhost:8080/"
#_GRAPHDBSERVER= "http://localhost:7200/"

_API_URL = _SERVER+"APIContextInteraction/api/headers/"
_DEFAULT_REPOSITORY = ""
#_HEADERS_TEMPLATE = {"X-GraphDB-Repository": _DEFAULT_REPOSITORY, "Accept": "application/json",
#                     "Content-Type": "application/json"}
_HEADERS_TEMPLATE = { "Accept": "application/json",
                      "Content-Type": "application/json",
                      "GRAPHDB_SERVER":_GRAPHDBSERVER}


#def set_default_repository(name):
#    _HEADERS_TEMPLATE["X-GraphDB-Repository"] = name


def request_template(template_id, json):
    url = "sparql-template/execute"
    template = {"templateId": template_id}
    template.update(json)
    response = requests.post(_API_URL + url, headers=_HEADERS_TEMPLATE, json=template)
    return response.json()

def query_to_API(query, params):
    print(_API_URL + query)
    response = requests.get(_API_URL + query, params=params, headers={"GRAPHDB_SERVER":_GRAPHDBSERVER})
    if response.status_code==404:
        print(response, response.status_code)

    return response.json()


def insert_individuals(json,entityName):
    print(_API_URL+"insert{}".format(entityName))
    try:
        response = requests.post(_API_URL+"insert{}".format(entityName), headers=_HEADERS_TEMPLATE, json=json)
        if response.status_code != 200:
            raise ValueError(response.status_code)
    except ValueError as err:
        print(f"Unexpected {err=}, {type(err)=}")
    return response.json()

def insert_batch_individuals(json,entityName):
    print(_API_URL+"insertBatch{}".format(entityName))
    try:
        response = requests.post(_API_URL+"insertBatch{}".format(entityName), headers=_HEADERS_TEMPLATE, json=json)
        if response.status_code != 200:
            raise ValueError(response.status_code)
    except ValueError as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print(json)
    return response.json()