import json
from sys import get_coroutine_origin_tracking_depth
from time import sleep
import requests
from bs4 import BeautifulSoup
from generate_list_of_links import *

def get_data_from_link(link):
    print("Fetching " + link)
    res = requests.get(link)
    html_content = res.content
    print("Fetched " + str(len(html_content)) + " bytes")
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.find('title').string.split("\n")[1].strip()
    main_content = soup.find('div', class_ = 'main-content')
    text = main_content.get_text()
    lines = [link] + [x.strip() for x in text.split("\n") if x.strip() != '']
    return (title, "\n".join(lines))

tree = read_to_elementtree()
links = parse_tree_into_list_of_links(tree)
links = filter_links_news_only(links)

data = []

for i in range(len(links)):
    print("\n=====", str(i), "/", len(links), " =====")
    link = links[i]
    title, content = get_data_from_link(link)
    id = "doc" + str(i)
    data.append({"_id": id, "title": title, "text": content})
    if i == 1:
        print(data)
    sleep(2) # be nice

with open("unfiltered_embeddings_dataset_corpus.jsonl", "w") as output:
    for row in data:
        output.write(json.dumps(row))
        output.write("\n")
