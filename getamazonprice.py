import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    price = soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative.apex-core-price-identifier > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay.apex-pricetopay-value > span:nth-child(2) > span.a-price-whole')
    return price[0].text.strip()

price = (getAmazonPrice("https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?crid=2Z9K7QG8X5Z3&keywords=automate+the+boring+stuff+with+python&qid=1685710866&sprefix=automate+the+boring%2Caps%2C316&sr=8-1"))
print('The price is '+price)