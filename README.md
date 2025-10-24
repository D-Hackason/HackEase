# アプリ名
- HackEase(ハッキーズ)
  - Hackathon + easyを組み合わせた造語
  - 気軽にハッカソンを行えるようなアプリ

# 環境構築
1. .envファイルの準備
   - ```cp .env.example .env``` を実行し、環境変数を各自で変更する
     ```
      # 各自変更するもの
      MYSQL_DATABASE=your_database_name
      MYSQL_USER=your_username
      MYSQL_ROOT_PASSWORD=root_password
      MYSQL_PASSWORD=your_password
      DJANGO_SECRET_KEY=your_secret_key
      DJANGO_DEBUG=1 # 開発時は1のまま
  
      # 共通
      MYSQL_HOST=db
      MYSQL_PORT=3306
      DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
      TIME_ZONE=Asia/Tokyo```
    
2. 初回ビルド & 起動
   - Dockerイメージのビルドを行う
    <br>```docker compose build```
    - コンテナをバックグラウンドで起動
    <br>```docker compose up -d```
    - ```django-web```と```mysql-db```という2つのコンテナが起動できたかを確認
      <br>```docker compose ps```
3. 以下のURLにアクセスして開発サーバー起動<br>```http://localhost:8000```         

4. アプリを作成
   - 以下のコマンドでアプリ作成<br>```docker compose exec web python manage.py startapp アプリ名```
     
6. マイグレーション & 管理ユーザー作成
   - DBのマイグレーションファイルを作成<br> ```docker compose exec web python manage.py makemigrations```
   - DBをマイグレーション<br> ```docker compose exec web python manage.py migrate```
   - 管理者ユーザー(admin)作成<br> ```docker compose exec web python manage.py createsuperuser```


7. MySQL に入って接続確認
    - DBコンテナに入る<br> ```docker compose exec db bash```

    - MySQLクライアントで接続（```.env```の値に合わせること）
    <br> ```mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE"```
    <br> (例)： ```mysql -uappuser -papppass appdb```

8. コンテナ停止
  -  ```docker compose down```でコンテナを停止する
  -  ボリュームを削除してDBの内容を初期化する場合は <br> ```docker compose down -v```
  -  .env を変更したときの反映
      - 変更が Django の環境変数のみの場合
<br> ```docker compose down``` した後、```docker compose up -d```
      - 変更がMySQLのユーザー/DB名/パスワードの場合
     <br> ```docker compose down -v```した後、```docker compose up -d```
