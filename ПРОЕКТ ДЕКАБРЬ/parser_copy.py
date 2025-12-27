import requests
from bs4 import BeautifulSoup
import time #по правилам нужно тормознуть на несколько секунд


def screach(sick_name):
    url = "https://ru.wikipedia.org/w/index.php?search=" + sick_name + ("&") + "title=Служебная%3AПоиск&profile=advanced&fulltext=1&ns0=1"

    payload = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Cookie': 'GeoIP=RU:TYU:Tyumen:57.15:65.54:v4; WMF-Last-Access-Global=24-Dec-2025; WMF-Uniq=TjpBW_EId-GbK_uJJHe9WgLTAAEBAFvdrR3n9XhcErQ7JdEsTc-srAVgkLDs0L_x; NetworkProbeLimit=0.001; WMF-DP=4da; WMF-Last-Access=24-Dec-2025'
    } #расказал (не правду) о себе чтобы не засекли

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        time.sleep(3) #тормоз чтобы не привлекать внимание
        bs = BeautifulSoup(response.text,"lxml")
        link = bs.find('div', 'mw-search-result-heading').find("a").get("href")
        url = "https://ru.wikipedia.org" + link
        response = requests.request("GET", url, headers=headers, data=payload)
        bs = BeautifulSoup(response.text,"lxml")
        all_text = [el.get_text() for el in bs.find_all("p")]
        return(all_text)
    return("")
