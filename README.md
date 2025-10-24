
1. .env を用意（コピー → 編集）
cp .env.example .env   # 例: 雛形がある場合

変更した主な値：MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_ROOT_PASSWORD, DJANGO_SECRET_KEY, DJANGO_ALLOWED_HOSTS, DJANGO_DEBUG など

2. 初回ビルド & 起動
docker compose build
docker compose up -d
docker compose ps              # Up になっているか確認
docker compose logs -f db      # MySQL が "ready for connections" になるまで確認

3. コンテナを止めずに Django プロジェクトを作る（初回のみ）

4. アプリを作成（startapp）
# 例: myapp というアプリ
docker compose exec web python manage.py startapp myapp


5. マイグレーション & 管理ユーザー作成
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser

6. 開発サーバーの起動
方法A：一時的に起動（コンテナは止めない）
docker compose exec web python manage.py runserver 0.0.0.0:8000

方法B：up で自動起動したい（次回以降ラク）

docker-compose.yml の web.command を python manage.py runserver 0.0.0.0:8000 に変更

反映：

docker compose down
docker compose up -d


アクセス確認：

http://localhost:8000

7. MySQL に入って接続確認
# DBコンテナに入る
docker compose exec db bash

# MySQL クライアントで接続（.env の値に合わせること）
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE"

# 終了
exit

8. .env を変更したときの反映
変更が Django の環境変数のみ の場合
docker compose down
docker compose up -d

変更が MySQLのユーザー/DB名/パスワード の場合

既存データを消しても良い開発環境なら “初期化（ボリューム削除）” が簡単

docker compose down -v   # ← db_data も削除（DB初期化）
docker compose up -d
