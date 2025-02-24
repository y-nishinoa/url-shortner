# Pythonランタイムを親イメージとして使用
FROM python:3.9

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 作業ディレクトリを/appに設定
WORKDIR /app

# 現在のディレクトリの内容をコンテナ内の/appにコピー
COPY . /app

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install -r requirements.txt

# ポートの公開
#EXPOSE 5000
#CMD ["flask", "run", "--host=0.0.0.0"]

# コンテナ起動時にapp.pyを実行
#CMD ["python", "app.py"]
CMD ["flask", "run"]

