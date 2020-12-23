# Kifu_Crawl
棋譜データベースにアクセスして自動で棋譜を取得できるプログラムです。  
Pythonで書かれてます。  
seleniumを使ったスクレイピング、並行処理の練習を兼ねて書きました  
# MultiKifClawler.py
MutiKifCrawler.pyは並行処理になってて、処理は早めです。  
chrome動かしてインターネットを経由する関係上、全体の動作は遅くなります。  
使うスレッド数や最初に開くサイトURL、戦型名を調整して使ってください  
# URL_Crawler.py  
MultiKifCrawler.pyを動かすために必要な  
URLが入った.txtファイルを作るためのプログラムです。  
セットにしてもよいのですが、それぞれ処理に時間がかかるので  
別々にしました  
