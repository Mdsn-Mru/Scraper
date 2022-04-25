#A simple script to scrape weather data utilizing Python.


from requests_html import HTMLSession

s = HTMLSession()
query = 'Lebanon, TN'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0'})

#Data gathered
temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

#Output
print(query, temp, unit, desc)