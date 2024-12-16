from bs4 import BeautifulSoup
import requests


def scrap():
    page = 1
    offers = []
    offer_count = 1
    while True:
        r = requests.get(f"https://www.pracuj.pl/praca/intern;kw/wroclaw;wp?rd=30&pn={page}")
        soup = BeautifulSoup(r.content)
        element = soup.find('span', {'data-test': 'top-pagination-max-page-number'})
        if element:
            max_page_number = int(element.text.strip())
        
        all_offers = soup.find_all('a', class_='tiles_cnb3rfy core_n194fgoq')
        if page > max_page_number:
            break
        for offer in all_offers:
            title = (offer.get('title').replace("Zobacz ofertę ", ""))
            link = offer.get('href')
            offers.append({offer_count:{"title":title, "link":link}})
            offer_count += 1
        page +=1
    return(offers)
