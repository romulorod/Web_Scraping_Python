# -*- coding: utf-8 -*-

import os
from os import link
from bs4 import BeautifulSoup
import requests
from halo import Halo

class WebScraping:

    base_url = ""
    first_page = ""

    def __init__(self, base_url, first_page):
        self.set_base_url(base_url)
        self.set_first_url(first_page)
        
    def set_base_url(self, base_url):
        if base_url != "":
            self.base_url = base_url
            print('Esta é a URL base', base_url)

    def set_first_url(self, first_page):
        if first_page != "":
            self.first_page = first_page
            print('Esta é a primeira página', first_page)
    
    def get_first_page(self):
        first_page = requests.get(self.base_url + self.first_page).content
        soup = BeautifulSoup(first_page, 'html.parser')
        first_link = soup.find("a", class_="alert-link").get('href')
        print('\nO subdiretório para acessar a próxima página:', first_link)
        self.html2 = self.base_url+first_link
        print('\nA url base e o subdiretório para acessar o link completo da segunda página:', self.html2)

    def get_second_page(self):
        second_page = requests.get(self.html2).content
        soup = BeautifulSoup(second_page, 'html.parser')
        self.second_link = soup.find("a", class_="btn btn-primary btn-sm center-block").get('href')
        print('\nEndereço do arquivo dentro da segunda página:', self.second_link)
        print('\nEsse é o endereço completo do arquivo:', self.base_url+self.second_link)

    def get_download_link(self):
        file_path = self.base_url + self.second_link
        print("\n")
        spinner = Halo(text='Downloading file...', spinner='clock')
        spinner.start()
        cwd = os.path.dirname(os.path.realpath(__file__))
        file = requests.get(file_path, allow_redirects=True).content
        with open(f'{cwd}/Padrão_TISS_Componente_Organizacional_202103.pdf', 'wb') as pdf:
            pdf.write(file)
        spinner.stop()

    def run(self):
        self.get_first_page()
        self.get_second_page()
        self.get_download_link()
        


fazer_download = WebScraping(
    'http://www.ans.gov.br',
    '/prestadores/tiss-troca-de-informacao-de-saude-suplementar')

fazer_download.run()