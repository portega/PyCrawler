from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


def conecta(str_url):
    try:
        response = urlopen(str_url)
    except HTTPError as e:
        codigo = e.code
        txt = "ERROR"
    except URLError as e:
        codigo = 0
        txt = e.reason
    else:
        codigo = response.status
        txt = response.read()
    return [str_url, txt, codigo]

#url = input("URL a crawlear: ")
#print("Buscando", url)

base_url = "http://www.google.es"

resp = urlopen(base_url)

print("HTTP code = ", resp.status)

html_doc = resp.read()

soup = BeautifulSoup(html_doc, 'html.parser')

l_enlaces = []
for link in soup.find_all('a'):
    url = link.get('href')
    if url.startswith("/"):
        url = base_url + url

    resultado = conecta(url)
    l_enlaces.append(resultado)
    print("URL: %s, ESTADO: %s" % (url, resultado[2]))


