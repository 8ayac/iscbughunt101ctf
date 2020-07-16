# iscbughunt101ctf

## 概要

学校でやった講義「バグハント入門」の最終演習で使ったCTFの問題

## 問題リスト

- [SQLi101](./sqli101)
- [SSRF101](./ssrf101)
- [BuggyBase2](./buggybase2)

## Writeups

<http://caya8.hatenablog.com/entry/2020/07/16/083000>

## 各問題のデプロイ方法

### SQLi101

下記コマンドを実行したあと、<http://127.0.0.1:10070/>で問題にアクセスできる。

```shell-session
$ cd sqli101
$ docker-compose up -d
```

### SSRF101

下記コマンドを実行したあと、<http://127.0.0.1:10080/>で問題にアクセスできる。

```shell-session
$ cd ssrf101
$ docker-compose up -d
```

### BuggyBase2

下記コマンドを実行したあと、<http://127.0.0.1:10090/>で問題にアクセスできる。

```shell-session
$ cd buggybase2
$ docker-compose up -d
```

