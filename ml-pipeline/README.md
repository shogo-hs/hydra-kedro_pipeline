## 使い方
ml-pipeline/conf 配下のconfig.yamlを編集し、利用するパラメータを設定。

ml-pipeline配下で以下を実行することでconfig.yamlに記載されたパラメータで実行。
```
python main.py
```


グリッドサーチを実行する場合は以下のコマンドを実行。

実行例
```
python main.py --multirun hparams.normalize=true,false
```
