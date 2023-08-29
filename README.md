# Kagawa_Univ_Search_Text_Book

## ライブラリー一覧とインストール

* selenium
```shell
$ pip3 install selenium==4.1.0
```

* bs4
```shell
$ pip3 install bs4
```

* requests
```shell
$ pip3 install requests
```

* pandas
```shell
$ pip3 install pandas
```

## Chrome Driverのインストール

* `zip`と`unzip`のインストール
```shell
$ sudo apt install unzip zip
```

* Driverのインストール
```shell
$ cd /usr/local/bin/
# Google Chromeのversionに合わせる
$ curl -O https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
```

* Driverの解凍
```shell
$ unzip chromedriver_linux64.zip
```

* 不要なzipファイルを削除
```shell
$ rm chromedriver_linux64.zip
```

## Google アプレッドシートの設定

1. [ここ](https://console.developers.google.com/)にアクセス

1. `プロジェクトの選択` > `NEW PROJECT`でプロジェクトを作成する

1. `API & Services` > `Enabled APIs & services`をクリック

    ![Alt text](https://github.com/IshigamiRyoichi/Kagawa_Univ_Search_Text_Book/blob/Search_Text_Book/image/image.png)

1. `+ENABLE APIS AND SERVICES`をクリック

    ![Alt text](https://github.com/IshigamiRyoichi/Kagawa_Univ_Search_Text_Book/blob/Search_Text_Book/image/image-1.png)

1. `Google Drive API`と`Google Aheets API`を検索し，2つのAPIを有効にする

    ![Alt text](https://github.com/IshigamiRyoichi/Kagawa_Univ_Search_Text_Book/blob/Search_Text_Book/image/image-2.png)

    ![Alt text](https://github.com/IshigamiRyoichi/Kagawa_Univ_Search_Text_Book/blob/Search_Text_Book/image/image-3.png)

1. `API & Services` > `Credentials`をクリック

    ![Alt text](https://github.com/IshigamiRyoichi/Kagawa_Univ_Search_Text_Book/blob/Search_Text_Book/image/image-4.png)

1. `CREATE CREDENTIALS`をクリック

1. サービスアカウントを作成する

1. `Service Accounts`の✐をクリック

    ![Alt text](https://github.com/IshigamiRyoichi/Kagawa_Univ_Search_Text_Book/blob/Search_Text_Book/image/image-5.png)

1. `KEYS` > `ADD KEY▼` > `Create new key` > `JSON` > `CREATE`

1. 保存されたJSONを`./json`に移動させる

1. Google スプレッドシートの`Share`をクリック

1. JSONの`client_email`のアドレスを追加 > `send`