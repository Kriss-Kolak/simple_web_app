from bs4 import BeautifulSoup
import requests


def scrap(praca = None):
    if praca == None:
        return None
    else:
        page = 1
        offers = []
        offer_count = 1
        while True:
            try:
                r = requests.get(f"https://www.pracuj.pl/praca/{praca};kw/wroclaw;wp?rd=30&pn={page}")
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Bląd połączenia {e}")
                break
            soup = BeautifulSoup(r.content)

            if page == 1:
                element = soup.find('span', {'data-test': 'top-pagination-max-page-number'})
                if element:
                    max_page_number = int(element.text.strip())
                else:
                    max_page_number = 1


            all_offers = soup.find_all('a', class_='tiles_cnb3rfy core_n194fgoq')
            if page > max_page_number:
                break
            for offer in all_offers:
                title = (offer.get('title').replace("Zobacz ofertę ", ""))
                link = offer.get('href')
                offers.append({"title":title, "link":link})
                offer_count += 1
            page +=1
        return(offers)
