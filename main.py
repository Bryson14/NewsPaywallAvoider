import urllib.request as req
import webbrowser as wb
from bs4 import BeautifulSoup


def innerHTML(element: str) -> str:
    if element is None or not isinstance(element, str):
        return ""
    if not element.startswith("<") or not element.endswith(">"):
        print("Element needs to follow the pattern:\n <tag STUFF> Inner HTML </ tag>")
        return ""
    element = element[element.find(">")+1 :-1]
    return element[:element.find("<")]





nytimes = "https://www.nytimes.com/2018/11/14/climate/california-wildfires-and-reinventing-air-conditioners-climate-newsletter.html"

f = req.urlopen(nytimes)
html = f.read()

soup = BeautifulSoup(html, 'html.parser')
p_elements = soup.find_all("p")

for ele in p_elements:
    print(ele)

# print(html)

# wb.open(nytimes)