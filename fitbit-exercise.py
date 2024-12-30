import sys
import json
import datetime
import csv

def main():
    # コマンドライン引数のチェック
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    try:
        # JSON ファイルを読み込む
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # JSON が配列であるかを確認
        if not isinstance(data, list):
            print("Error: JSON file must contain an array of objects.")
            sys.exit(1)
        
        # "activityName" が "ランニング" のオブジェクトをフィルター
        filtered_data = list(filter(lambda obj: obj.get("activityName") == "ランニング", data))
        
        # 必要な要素だけを抜き出した新しいオブジェクトの配列を作成
        mapped_data = list(map(lambda obj: {
            "startTime": datetime.datetime.strptime(obj.get("startTime"), "%m/%d/%y %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%SZ"),
            "distance": round(obj.get("distance") * 1000) if obj.get("distanceUnit") == "Kilometer" else obj.get("distance"),
            "duration": round(obj.get("duration") / 1000 / 60, 2),
            "distanceUnit": "meter" if obj.get("distanceUnit") == "Kilometer" else obj.get("distanceUnit"),
            "durationUnit": "minutes",
            "activityName": obj.get("activityName"),
            "source/type": obj.get("source", {}).get("type"),
            "source/name": obj.get("source", {}).get("name")
        }, filtered_data))
        
        # 出力ファイル名を作成 (入力ファイル名と同名で拡張子を変更)
        output_file = json_file + '.tsv'
  
        # 出力ファイルに書き出す
        with open(output_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=mapped_data[0].keys(), delimiter='\t')
            writer.writeheader()
            writer.writerows(mapped_data)

        print(f"File has been written to: {output_file}")    
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

