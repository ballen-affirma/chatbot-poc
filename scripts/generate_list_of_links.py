import xml.etree.ElementTree as ET

def read_to_elementtree():
    tree = ET.parse('alorica-sitemap.xml')
    return tree

def parse_tree_into_list_of_links(tree):
    root = tree.getroot()
    urls = root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
    output_list = []
    for url in urls:
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        output_list.append(loc.text)
    return output_list

def filter_links(links):
    f1 = filter(lambda x: ("/news/" in x) == False, links)
    f2 = filter(lambda x: ("/awards-recognition/" in x) == False, f1)
    f3 = filter(lambda x: ("/insights/" in x) == False, f2)
    return list(f3)

def filter_links_news_only(links):
    f1 = filter(lambda x: ("/news/" in x) == False, links)
    return list(f1)

if __name__ == "__main__":
    tree = read_to_elementtree()
    links = parse_tree_into_list_of_links(tree)
    
    # filter the links for news and awards. Done to shrink the context and fit within a limit
    links = filter_links_news_only(links)
    links = [x.split("https://alorica.com")[1] for x in links]
    print("\n".join(links))