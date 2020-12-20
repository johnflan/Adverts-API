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
        var_name = ('__'.join(re.replace('-', '_').split('/')[2:-2])).upper()
        var = f"{var_name} = '{re}'"

        # Can be faster... 
        myfile = open('categories.txt', 'a+')
        myfile.writelines(var + '\n')
        myfile.close()

        recurse_cat(base_url + re)


initial_url = 'https://www.adverts.ie/for-sale'
base_url = 'https://www.adverts.ie'

recurse_cat(initial_url)

# [1]
# [1, 2, 3, 4, 5, 6, 7, 8]
# 1 = [11, 12, 13, 14, 15]
# 2 = [21, 22, 23, 24]
# 21 = [211, 212]
# 22 = [221, 222, 223]