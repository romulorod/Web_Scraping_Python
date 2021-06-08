import os
from os import link
from bs4 import BeautifulSoup
import requests
from halo import Halo

base_url = ('http://www.ans.gov.br')
print('Esta é a URL base', base_url)
first_page = requests.get('http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar').content
soup = BeautifulSoup(first_page, 'html.parser')
first_link = soup.find("a", class_="alert-link").get('href')
print('\n O subdiretório para acessar a próxima página:', first_link)
html2 = base_url+first_link
print('\nA url base e o subdiretório para acessar o link completo da segunda página:', html2)
second_page = requests.get(html2).content
soup = BeautifulSoup(second_page, 'html.parser')
second_link = soup.find("a", class_="btn btn-primary btn-sm center-block").get('href')
print('\nEndereço do arquivo dentro da segunda página:', second_link)
print('\nEsse é o endereço completo do arquivo:', base_url+second_link)
file_path = base_url+second_link
print("\n")
spinner = Halo(text='Downloading file...', spinner='clock')
spinner.start()

cwd = os.path.dirname(os.path.realpath(__file__))
file = requests.get(file_path, allow_redirects=True).content

with open(f'{cwd}/Padrão_TISS_Componente_Organizacional_202103.pdf', 'wb') as pdf:
    pdf.write(file)

    spinner.stop()