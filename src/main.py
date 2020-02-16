import os
from pprint import pprint

import firefly_iii_client.models.transaction_split
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from firefly_iii_client.rest import ApiException

soup = ""
with open("../history_1.xml") as fh:
    soup = BeautifulSoup(fh, "xml")

listw = soup.operations.find_all("operation")
# for i in listw:
#     print(i.type)
trans = firefly_iii_client.Transaction()

load_dotenv()

config = firefly_iii_client.configuration.Configuration()

config.host = os.getenv("HOST")
config.access_token = os.getenv("TOKEN")

api_instance = firefly_iii_client.AboutApi(firefly_iii_client.ApiClient(config))
try:
    # System information end point.
    api_response = api_instance.get_about()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about: %s\n" % e)
