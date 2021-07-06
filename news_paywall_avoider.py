import urllib.request as req
import urllib.error as err
from bs4 import BeautifulSoup
from sys import argv

def main(news_url):
    
    USAGE_MESSAGE = "="*20 + "\nUSAGE:\npython news_paywall_avoider.py URL\n"+20*"="
    try:
        p_elements = BeautifulSoup(req.urlopen(news_url).read(), 'html.parser').find_all("p")
        for ele in p_elements:
            print(ele.text, end=" ")
    except ValueError as e:
        print(f"\nBAD URL: Might need https:// in front\n{USAGE_MESSAGE}\n{e}")
    except err.HTTPError as e:
        print(f"\nHTTP Error\n{USAGE_MESSAGE}\n{e}")
    except:
        print(f"Unknown Error\n{USAGE_MESSAGE}\n")

if "__main__" == __name__:
    main(argv[1])
