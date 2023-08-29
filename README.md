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