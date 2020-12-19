import bs4 as bs
import requests


def get_cat(url):
    response = requests.get(url).text
    soup = bs.BeautifulSoup(response, 'html.parser')
    s = soup.findAll('a', {'class': 'fix-facet-text'})
    return [c['href'] for c in s]


def recurse_cat(url):
    res = get_cat(url)

    if len(res) == 0:
            return

    for re in res:
        print(re)
        recurse_cat(base_url + re)


initial_url = 'https://www.adverts.ie/for-sale'
base_url = 'https://www.adverts.ie'

print('in')
recurse_cat(initial_url)


        
        

# [1]
# [1, 2, 3, 4, 5, 6, 7, 8]
# 1 = [11, 12, 13, 14, 15]
# 2 = [21, 22, 23, 24]
# 21 = [211, 212]
# 22 = [221, 222, 223]