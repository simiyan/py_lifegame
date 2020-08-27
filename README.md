# py_lifegame_gui

Lifegame-GUI with python

## 0.注意点

Readmeは作成中。依存関係等を先に記載。

### 0.1 依存package

下記のpakcageに依存。pipコマンドで記載。

- pip install PyQt5
- pip install opencv-python
- pip install PyQt5Designer
- pip install numpy

### 0.2 使い方

- GUIver  
pictui_call.pyを実行することで、ウィンドウが起動する。  
最初はすべて「死」=「バツ」のstatusで起動する。  
worldサイズはmainでcallしているlife_game()の引数の調整で変更可能。  
世代交代の間隔はlife_game()/time.sleep()の引数の調整で変更可能。[いずれ設定値にしたい]  
クリックで「生」と「死」を切り替えられる。　　
「Random」ですべてのstatusをランダムに設定。  
「Start」でlifegameをスタート。
「Stop/Pause」で世代交代を一時停止できる。  
「Reset」すると、全てのstatusを「死」に変更して, その世界の変化をビデオ化する。  
ビデオはmy_life_diaryフォルダに保存される。  

## 1.仕様 

### 1.1 基本ルール

- lifegameのルールに則る
  - 過疎：　Xに隣接する生きたセルが0から1個の場合，「過疎」により，Xは「死」状態となる．
  - 維持：　Xに隣接する生きたセルが２個の場合，Xの状態は変化しない．つまり，元が「死」なら次の状態は「死」であり，元が「生」なら次の状態も「生」となる．
  - 誕生：　Xに隣接する生きたセルが3個の場合，Xは無条件に「生」状態となる．
  - 過密：　Xに隣接する生きたセルが4個以上の場合：「過密」により，Xは「死」状態となる．

### 1.2 プログラム仕様

- 登場人物(クラス)は以下の通り。
  - 1.1のルールに従って動くlife
  - lifeに世代交代等の指示を出す、worldの監視者
  - lifeが存在するworld

## 2.仕様の詳細

### 2.1 lives
