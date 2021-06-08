import os
from os import link
from bs4 import BeautifulSoup
import requests
from halo import Halo


class WebScraping:
    def __init__(self, base_url, first_page, first_link, second_page, second_link, download_link):
        self.base_url = base_url
        self.first_page = first_page
        self.first_link = first_link
        self.second_page = second_page
        self.second_link = second_link
        self.download_link = download_link

    def get_base_url(self):
        base_url = ('http://www.ans.gov.br')
        print('Esta é a URL base:', base_url)

    def get_first_page(self, base_url):
        first_page = requests.get(
            'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar').content
        soup = BeautifulSoup(first_page, 'html.parser')
        first_link = soup.find("a", class_="alert-link").get('href')
        print('\nO subdiretório para acessar a próxima página:', first_link)
        html2 = base_url+first_link
        print('\nA url base e o subdiretório para acessar o link completo da segunda página:', html2)

    def get_second_page(self, base_url, second_link, html2):
        second_page = requests.get(html2).content
        soup = BeautifulSoup(second_page, 'html.parser')
        second_link = soup.find(
            "a", class_="btn btn-primary btn-sm center-block").get('href')
        print('\nEndereço do arquivo dentro da segunda página:', second_link)
        print('\nEsse é o endereço completo do arquivo:', base_url+second_link)

    def get_download_link(self, base_url, second_link):
        file_path = base_url+second_link
        print("\n")
        spinner = Halo(text='Downloading file...', spinner='clock')
        spinner.start()
        cwd = os.path.dirname(os.path.realpath(__file__))
        file = requests.get(file_path, allow_redirects=True).content
        with open(f'{cwd}/Padrão_TISS_Componente_Organizacional_202103.pdf', 'wb') as pdf:
            pdf.write(file)
        spinner.stop()


fazer_download = WebScraping('http://www.ans.gov.br', 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar', '/prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-marco-2021', 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-marco-2021', '/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padr%C3%A3o_TISS_Componente_Organizacional_202103.pdf', 
'http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padr%C3%A3o_TISS_Componente_Organizacional_202103.pdf')

fazer_download.get_base_url()
fazer_download.get_first_page('http://www.ans.gov.br')
fazer_download.get_second_page('http://www.ans.gov.br','/prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-marco-2021', 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/padrao-tiss-marco-2021')

fazer_download.get_download_link(
    'http://www.ans.gov.br', '/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padr%C3%A3o_TISS_Componente_Organizacional_202103.pdf')
