import requests
from bs4 import BeautifulSoup


def screach(sick_name):
    url = "https://probolezny.ru/?q=" + sick_name

    payload = {}
    headers = {
    'Cookie': 'csrftoken=jhKdbYRqjGGNpf1apsrx790CB8uMxv8M; sessionid=jhzcbnq5ua4id3wouv2h8a5g66cmqmy1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print (response.text)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text,"lxml")
        link = bs.find('a', 'b-articles-list__item-link').get("href")
        url = "https://probolezny.ru" + link
        response = requests.request("GET", url, headers=headers, data=payload)
        bs = BeautifulSoup(response.text,"lxml")
        all_info = bs.find_all('div', 'b-article__text-part')
        simptomi = all_info[1].text
        lechenie = all_info[6].text
        profilactika = all_info[7].text
        return(simptomi, lechenie, profilactika)
    return("", "", "")

screach("Детский%20аутизм")