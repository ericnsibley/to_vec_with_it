import requests 
from xml.etree import ElementTree as ET


# From https://info.arxiv.org/help/api/user-manual.html#Quickstart
# Because of speed limitations in our implementation of the API, 
# the maximum number of results returned from a single call (max_results) is limited to 30000 in slices of at most 2000 at a time, 
# using the max_results and start query parameters. 
# For example to retrieve matches 6001-8000: http://export.arxiv.org/api/query?search_query=all:electron&start=6000&max_results=8000

# There's also a sortBy query param I can use if needed
def search_arxiv(query: str, max_results: int) -> str: 
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "max_results": max_results
        # "start": Int
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.content.decode("utf-8")
    else:
        print("An error occurred. Status code:", response.status_code)
        return None
    

def parse_arxiv_response(response: str) -> list[dict]: 
    root = ET.fromstring(response)
    results = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        result = {}
        result["title"] = entry.find("{http://www.w3.org/2005/Atom}title").text.strip().replace('\n', ' ')
        result["authors"] = [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")]
        result["date_published"] = entry.find("{http://www.w3.org/2005/Atom}published").text
        result["summary"] = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip().replace('\n', ' ')
        result["pdf_url"] = entry.find("{http://www.w3.org/2005/Atom}link[@title='pdf']").attrib["href"]
        results.append(result)
    
    return results


def download_articles_related_to(query: str, max_results: int = 10) -> list[dict]:
    xml = search_arxiv(query, max_results) 
    parsed_documents = parse_arxiv_response(xml)
    return parsed_documents


if __name__ == "__main__":
    for doc in download_articles_related_to("electrons"):
        print(doc)