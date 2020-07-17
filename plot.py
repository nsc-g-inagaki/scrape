import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# フォントの設定
matplotlib.rc('font', family='TakaoPGothic')

def plot_datas(datas):
    # データ保持の変数を初期化
    date, st_price, high_price, low_price, final_price = ([] for i in range(5))

    # データの2行目よりを処理
    for _, value in enumerate(datas[1:]):
        # 日付を取得　曜日抜きで
        date.append(value[0][:-3])
        # 始値を取得
        st_price.append(int(value[1]))
        # 高値を取得
        high_price.append(int(value[2]))
        # 安値を取得
        low_price.append(int(value[3]))
        # 終値を取得
        final_price.append(int(value[4]))

    # グラフのベースを作成
    fig, ax = plt.subplots(figsize=(13,5), facecolor='w')

    # グラフにグリッドを設定
    ax.grid(True)

    # グラフにデータを書く　日付, 始値, マーカー, ラベルを設定
    ax.plot(date, st_price, marker='.', label = datas[0][1])

    # グラフにデータを書く　日付, 高値, マーカー, ラベルを設定
    ax.plot(date, high_price, marker='.', label = datas[0][2])

    # グラフにデータを書く　日付, 安値, マーカー, ラベルを設定
    ax.plot(date, low_price, marker='.', label = datas[0][3])

    # グラフにデータを書く　日付, 終値, マーカー, ラベルを設定
    ax.plot(date, final_price, marker='.', label = datas[0][4])

    # 重複している値段を抜いて、すべての値段を配列にする
    data_set = set(st_price + high_price + low_price + final_price)
    y_values = list(data_set)

    # y軸の値を一番小さい値段と一番高い値段を20おきに設定
    ax.set_yticks(range(min(y_values), max(y_values), 20))
    
    # ラベルの設定　x軸のラベル　y軸ラベル　タイトル
    ax.set(xlabel='日付', ylabel='値', title='セラク株価')
    
    # 各ラインの説明項目を右上に設定
    fig.legend(loc='upper right')

    # 画像を保存
    fig.savefig(_generate_file_name(date[0], date[-1]), bbox_inches='tight', dpi=300)

# ファイル名を作成
def _generate_file_name(st_date, end_date):
    parent_path = Path(__file__).parent.absolute()

    return str(parent_path.joinpath(f"seraku_{st_date.replace('/', '-')}-{end_date.replace('/', '-')}.png"))


    

