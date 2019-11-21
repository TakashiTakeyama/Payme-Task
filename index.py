import json
import csv

# JSONファイルのロード
json_dict = json.load(open('data/players.json', 'r'))
# list of dictの抽出
target_dicts = json_dict

with open('data/players.csv', 'w') as f:
    # dialectの登録
    csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
    # DictWriter作成
    fieldnames = ["id", "date_ym", "date_d", "date", "provider", "total_count", "registered_count", "unregistered_count"]
    writer = csv.DictWriter(f, fieldnames, dialect='dialect01')
    # CSVへの書き込み
    writer.writeheader()
    for target_dict in target_dicts:
        writer.writerow(target_dict)