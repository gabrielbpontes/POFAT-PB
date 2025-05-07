import os
import re
import subprocess
from glob import glob

import pandas as pd
import requests
from bs4 import BeautifulSoup

URL_LINKS = 'https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf'
URL_DOWNLOAD = (
    'https://drive.usercontent.google.com/u/0/uc?id={}&export=download'
)
URL_DATASET = (
    'data/acidentes_pb.csv'
)
ANO_INICIO = 2020
ANO_FIM = 2025


def get_url_links() -> pd.DataFrame:
    content = requests.get(URL_LINKS).content
    soup = BeautifulSoup(content, 'html5lib')
    tables = soup.find_all('table')
    acidentes = tables[1].find_all('tr')

    data = {'name': [], 'key': [], 'ano': [], 'link_download': []}
    for acidente in acidentes:
        link = acidente.find('a')
        name = acidente.text
        if link and '(agrupados por ocorrência)' in name.lower():
            ano_match = re.search(r'[1-9]\d{3}', name)
            ano = int(ano_match.group(0)) if ano_match else None
            data['ano'].append(ano)
            data['name'].append(f'acidentes-{ano}.zip')
            data['key'].append(link.get('href').split('d/')[1].split('/')[0])
            data['link_download'].append(URL_DOWNLOAD.format(data['key'][-1]))

    return pd.DataFrame(data)


def filter_df_links(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df.query('ano >= @ANO_INICIO and ano <= @ANO_FIM')
    return df


def download_data(df: pd.DataFrame) -> pd.DataFrame:
    for link, name in zip(df.link_download.to_list(), df.name.to_list()):
        name = os.path.join('data', name)
        os_cmd_list = [
            'wget',
            '--limit-rate',
            '50000k',
            '--no-check-certificate',
            '-c',
            link,
            '-O',
            name,
        ]
        subprocess.run(os_cmd_list)


def unzip_files():
    zips = glob('data/*')

    for zip_file in zips:
        subprocess.run(['unzip', zip_file, '-d', 'data/'])
        os.remove(zip_file)


def concat_and_filter_dataset() -> pd.DataFrame:
    files = glob('data/*.csv')

    dfs = []
    for file in files:
        dfs.append(pd.read_csv(file, sep=';', encoding='latin1'))

    dataset = pd.concat(dfs)
    dataset = dataset.query("uf == 'PB'")
    dataset = dataset.dropna()

    return dataset

def remove_files():
    files = set(glob('data/*'))
    files = files - {URL_DATASET}
    for file in files:
        os.remove(file)

def main():
    os.makedirs('data', exist_ok=True)
    df = get_url_links()
    df = filter_df_links(df)
    download_data(df)
    unzip_files()
    dataset = concat_and_filter_dataset()
    dataset.to_csv(URL_DATASET, index=False)
    remove_files()


if __name__ == '__main__':
    main()
