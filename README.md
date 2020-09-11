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

- lifeは命である。  
- 「どこにいる」と、  
  「生きている/死んでいる」と、  
  「周りの生死により、次世代はどうする」がわかる。  
- よって次の機能を持つ。
  - 初期statusは各lifeがrandomに決定する
  - 現在のstatus[生or死]を聞かれたら答える
  - 現在の場所[座標]を聞かれたら答える
  - 周辺のstatusの様子を聞き、次世代のstatusを決める
  - 次世代のstatusに進める

### 2.2 life_controller

- worldの監視者[life_controller]は次の機能を持つ。  
  - lifeの召喚
  - 各lifeのstatus調査
    - とあるlifeの周辺座標のlist up
    - list upされた周辺座標から合計値を計算
  - 各lifeに世代交代を指示
  - 各lifeからstatusを聞き出して表示

### 2.3 mkWorld

- world[mkWorld]は世界である。
- 「永続する」  
  「東西と南北に広がる」  
  「時間で移り変わる」特徴がある。  
- よって次の機能を持つ  
  - 任意の方向x, yに世界を展開する
  - 永続ループする
  - 一定時間ごとに監視者にlifeのstatusを変化させる
  - 実際に各オブジェクトを所持するのは、このクラス

## 3.将来的な追加点・変更点など

### 3.1 追加したいこと(GUI)

1. status変化理由の表示
2. lifeにrandomな氏名を与える  
   1. 1,2を合わせると「山田太郎は維持により生存した」のようなメッセージが表示される
3. status変化理由の充実
   1. 過疎 → 寂しくて, 維持:1 → 楽しくて  
   のように理由に人間味を持たせる
4. 有名なlifegameの変化パターンをautoで初期配置させる  
   例：「グライダー銃」「シュシュポッポ列車」
5. lifeに「3すくみの関係」を追加した時の変化をみる

## 99.その他

- 2020/09/04 PEP8チェックツール、flake8を適用してみた
  - 見つかった数：全ファイル中で53個
    - 一番多かったもの
      - W293 blank line contains whitespace(30個)
      - 理由
        - VScodeの自動indent機能のため。(改行すると勝手にindentしてくれる)
    - 他 blank lineやwhitespaceが目立つ
      - E211 whitespace before '('
      - E225 missing whitespace around operator
      - E301 expected 1 blank line, found [0-9]
      - E302 expected 2 blank lines, found [0-9]
      - E303 too many blank lines (5)
      - E305 expected 2 blank lines after class or function definition, found 0
      - E401 multiple imports on one line
      - F401 '*' imported but unused
      - F841 local variable 'change_result' is assigned to but never used
      - W291 trailing whitespace
      - W292 no newline at end of file
      - W391 blank line at end of file
