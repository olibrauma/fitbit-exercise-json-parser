# fitbit-exercise-json-parser
Fitbit で計測したランニングの記録から、以下のデータを抜き出して TSV で書き出す。
- `startTime`: ISO 8601 形式の日付
- `distance`: メートル単位の走行距離
- `duration`: 分単位の走行時間。小数第 2 位まで
- `distanceUnit`: _**"meter"**_ になってるはず
- `durationUnit`: _**"minutes"**_ になってるはず
- `activityName`: _**"ランニング"**_ になってるはず
- `source/type`: _**"tracker"**_ 以外を見たことがない。他に何が入りうるんだろう？
- `source/name`: Fitbit のモデル名が入るはず

## 使い方
```bash
$ python fitbit-exercise.py path/to/exercise-{number}.json
```

スクリプトと同じフォルダに、JSON と同名の TSV が書き出される。Google Sheets などにコピペして使ってください。

## 使用するファイル
[Google データ エクスポート](https://takeout.google.com/?hl=ja) からダウンロードした Fitbit のデータを使う。使用するのは Fitbit フォルダの中の以下のファイル。

`/Takeout/Fitbit/Global Export Data/exercise-{number}.json`

中身はこんな感じ。注意点は
- 日付と時刻の様式は `MM/DD/YY hh:mm:ss` の順で UTC+0:00
- `duration` は (おそらく) ミリ秒
```jsonc
[
  {
    "activityName" : "ランニング",
    "distance" : 0.0,
    "distanceUnit" : "Kilometer",
    "duration" : 7000,
    "startTime" : "10/22/23 07:37:43",
    "source" : {
      "type" : "tracker",
      "name" : "Charge 5",
      // ...
    },
    // ...
  },
  // ...
]
```
