import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    all = soup.find_all('a',title="Wikipedia:Citation needed")
    return len(all)



def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    par = soup.find_all('p')
    report = []
    for a in par:
        if a.find('a',title="Wikipedia:Citation needed"):
            report.append(a.text.strip())
    return report


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    x = get_citations_needed_report(url)
    for i in x :
        print(i , "\n")

    




