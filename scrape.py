import requests
import csv
import plot
from pathlib import Path
from bs4 import BeautifulSoup

# データのスクレープをする
def scrape_data():
    # 指定したURLのデータを取得する
    page = _get_html_data('https://www.nikkei.com/nkd/company/history/dprice/?scode=6199')

    # 株価の値段をページから取得
    price_data = _get_price_data_from_page(page)

    # データをファイルにエキスポートする
    _export_data(Path(__file__).parent.absolute()
        .joinpath(f"seraku_{price_data[1][0].replace('/', '-')[:-3]}-{price_data[-1][0].replace('/', '-')[:-3]}.csv"), 
        price_data)

    # データを画像にする
    plot.plot_datas(price_data)

# HTMLデータを取得する
def _get_html_data(url):
    # urlにリクエストを飛ばす
    response = requests.get(url)
    # BeautifulSoupでテキストをオブジェクト化
    soup = BeautifulSoup(response.text, 'html.parser')
    # ページデータを返す
    return soup

# HTMLページから株価情報を取得する
def _get_price_data_from_page(page):

    values = []
    data = []
    # ページからテーブルないの行をすべて抽出する
    table = page.find('table', class_='w668').findAll('tr')

    # タイトル行を取得してデータを加工
    [data.append(val.text.strip()) for val in table[0].findAll(class_='a-taC')]

    values.append(data)
    # データ行の処理
    for row in reversed(table[1:]):
        data = []
        # 日付前後の空文字を削除
        [data.append(val.text.strip()) for val in row.findAll(class_='a-taC')]
        # 値段の前後の空文字削除とカンマをなくす
        [data.append(val.text.strip().replace(',', '')) for val in row.findAll(class_='a-taR')]
        values.append(data)
    
    # 加工済みのデータを返す
    return values

# データのエキスポート
def _export_data(file_path, data):
    # ファイルにデータを出力
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == '__main__':
    scrape_data()

