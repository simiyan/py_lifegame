# py_lifegame_gui

Lifegame-GUI with python

## 0.注意点

Readmeは作成中。依存関係等を先に記載。

### 0.1 依存package

CUIverは依存packageなし

### 0.2 使い方

- CUI-ver  
mkWorld.pyを実行することで、デバッグコンソールでライフゲームが実行される。  
worldサイズはmainでcallしているlife_game()の引数の調整で変更可能。  
世代交代の間隔はlife_game()/time.sleep()の引数の調整で変更可能。  
[いずれ設定値にしたい]

## 1.仕様

### 1.1 基本ルール

- lifegameのルールに則る
  - 過疎：　Xに隣接する生きたセルが0から1個の場合，「過疎」により，Xは「死」状態となる．
  - 維持：　Xに隣接する生きたセルが２個の場合，Xの状態は変化しない．つまり，元が「死」なら次の状態は「死」であり，元が「生」なら次の状態も「生」となる．
  - 誕生：　Xに隣接する生きたセルが3個の場合，Xは無条件に「生」状態となる．
  - 過密：　Xに隣接する生きたセルが4個以上の場合：「過密」により，Xは「死」状態となる．

### 1.2 プログラム仕様

- 登場人物(クラス)は以下の通り。
  - 1.1のルールに従って動くlife[lives]
  - lifeに世代交代等の指示を出す、worldの監視者[life_controller]
  - lifeが存在するworld[mkWorld]

## 2.仕様の詳細

### 2.1 lives

- lifeは命であるので次の機能を持つ
  - 初期statusは各lifeがrandomに決定する
  - 現在のstatus[生or死]を聞かれたら答える
  - 現在の場所[座標]を聞かれたら答える
  - 周辺のstatusの様子を聞き、次世代のstatusを決める
  - 次世代のstatusに進める

### 2.2 life_controller

- worldの監視者[life_controller]は次の機能を持つ  
  - lifeの召喚
  - 各lifeのstatus調査
  - とあるlifeの周辺座標のlist up
  - list upされた周辺座標から合計値を計算
  - 各lifeに世代交代を指示
  - 各lifeからstatusを聞き出して表示
- 実際にlifeオブジェクトを所持するのはこのクラス

### 2.3 mkWorld

- 
