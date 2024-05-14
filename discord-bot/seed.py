import os
import requests
from vectara import Vectara

from datetime import datetime
from dotenv import load_dotenv

links=[
    'https://twitter.com/heyeaslo/status/1581644211769659393',
    'https://twitter.com/iamitsy/status/1574380285906386944',
    'https://twitter.com/ykdojo/status/1572974490262573066',
    'https://twitter.com/EntreEden/status/1780771887624417315'
]

def add_data(link):
    full_link = f"https://r.jina.ai/{link}"

    try:
        response = requests.get(full_link)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return
  
    # save data to vectara with these properties: the chunk is the content. metadata is topic, user_id, and link to post

    # print(f"content: {data}")
    load_dotenv()
    vectara_key = os.getenv("VECTARA_KEY")
    customer_id = os.getenv("CUSTOMER_ID")
    corpus_id = os.getenv("CORPUS_ID")
    vec = Vectara(vectara_key, customer_id, int(corpus_id))
    returns = vec.file_upload(file_text=data, link=link)

    if returns is None:
        print("not added!")
    else:
        print("added!")


for link in links:
    add_data(link)
