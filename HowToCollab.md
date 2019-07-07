# Git を使った共同開発のやりかた

バージョン管理システム Git とそれを使ったオンラインサービス GitHub を使って共同開発を始めるための手順を説明します。
前提として、git のコマンドライン版がインストールされている必要があります。
macOS と Linux の場合は最初から入っています。
Windowsの場合は最初からは入っていないので、もしインストールされていない場合は、Git for Windows をインストールしてください。

## 【Git を使い始める時に最初に１回だけやること】
Windows の場合は、スタートメニューから Git bash を起動して、そこで下記のコマンドを入力してください。Macの場合はターミナルで実施してください。"ユーザ名"　のところは、メールアドレスと合わせて表示される自分の名前を英語名で書いてください。"メールアドレス" は公開してもかまわないアドレスを入れてください。

```sh
$ git config --global user.name "ユーザ名"
$ git config --global user.email "メールアドレス"
```

続いて、git でコミットログを書く時のエディタを指定します。Visual Studio Code の場合は "code" としてください。
Linux や Mac の場合は、”nano" が使いやすいかもしれません。使い方を知っている方は、"vi" でもオッケーです。

```
$ git config --global core.editor "code"
```

## 【GitHub を使い始めるときに最初に１回だけやること】
まだ GitHub のアカウントを持っていない方は、GitHub のサイトを開いてユーザー登録します。ユーザー名とメールアドレスとパスワードを聞かれますので、入力するときに忘れないようにメモしておいてください。

    https://github.com/

## 共同開発者にしてもらうための手続き
GitHub のアカウントを取得したら、chatbot project の共同開発者にしてもらうために、
チャットやメールなどで、chatbot リポジトリの管理者にアカウント名を連絡します。

共同開発者にしてもらうと、GitHub 上の chatbot リポジトリに自分で branch を追加することができます。
そうすると、ブランチに追加したコードをリポジトリの管理者に見てもらうことができるようになります。

chatbot リポジトリの管理者は、連絡を受けたら、chatbot project のページ

    https://github.com/HideKobayashi/chatbot

から、`Setting` タブを開き、左側のメニューから　`Collaborators` を選んで、アカウント名を検索し、`Add collaborator` ボタンを押します。

あなたは、共同開発者としてのお誘い (invitation) をメールで受け取ることになります。
メールには、共同開発者になることを受け入れるためのボタンが表示されているはずなので、それを押して、Web ページで適切な手続きを行います。


### SSH 公開鍵の登録（オプション）
GitHub を利用するときに、毎回パスワードを聞かれると手間がかかるので、パスワードを使わなくても安全に GitHub を利用できるようにするために、セキュアーシェルの秘密鍵と公開鍵を作成します。

Windows の場合は、スタートメニューから Git bash を起動して、そこで下記のコマンドを入力してください。Macの場合はターミナルで実施してください。
```sh
$ ssh-keygen
```
このコマンドを入力すると、対話的に新しいパスワードを入力するように聞かれますが、入力はせず Enter で進めてください。
これが終わると、ホームディレクトリの下の、`~/.ssh` というディレクトリに秘密鍵 `id_rsa` と公開鍵 `id_rsa.pub` のファイルができています。
```sh
$ ls ~/.ssh/
config  id_rsa  id_rsa.pub  known_hosts
```

`id_rsa.pub` を GitHub に登録します。そのためには、再び、GitHub ホームページ

    https://github.com/

を開いて、右上のあなたのアイコンをクリックし、開いたメニューの下の方にある、Settings という項目を選びます。画面の左に、Personal Settings というメニューが表示されるので、その中の、SSH and GPG keys というところをクリックします。右上のほうに New SSH key という緑色のボタンがあるので、それをクリックします。Title と Key という２つの欄が現れるので、Title は、今使っているパソコンと関係あるキーワードを書いてください。仕事で使っているマシンなら、Work PC とか。
Key のところは、 公開鍵 id_rsa.pub の内容をコピーして貼り付けてください。Add SSH key ボタンを押したら、完了です。

これで、パスワードを聞かれることなく git コマンドで GitHub に書き込むことができるようになりました。



## 【Git の使い方】
ここでは、Git を使ってソースコードを GitHub のリポジトリからクローン（ダウンロード）して、ブランチを作成し、コードを変更し、ブランチを GitHub のリポジトリにプッシュ、最後にプルリクエストを発行するところまで行います。

Windows の場合は、スタートメニューから Git bash を起動して、そこで下記のコマンドを入力してください。Macの場合はターミナルで実施してください。

### 1. 開発用のディレクトリに移動します。

```sh
$ cd Desktop/pyworks
```

### 2. Git コマンドで chatbot プロジェクトのソースコードをクローン（ダウンロード）します。

今回は開発用のディレクトリ chatbot-dev にダウンロードすることにします。

```sh
$ git clone https://github.com/HideKobayashi/chatbot.git chatbot-dev
```

これで、chatbot-dev というディレクトリ（フォルダ）ができます。
chatbot-dev ディレクトリに移動します。

```sh
$ cd chatbot-dev
```
このディレクトリは、Git でクローンして作られたので Git で管理されているディレクトリになります。Git で管理されるディレクトリの下には`.git` というディレクトリがあります。これをローカルリポジトリと呼びます。


### 4. ローカルリポジトリの状態を知る
ローカルリポジトリの状態を表示するには、`git status` を使います。
```sh
$ git status
```
特に異常がない場合は
```
On branch master
Your branch is up to date with 'origin/develop'.

nothing to commit, working tree clean
```
などと表示されます。

ローカルリポジトリのブランチを表示するには、`git branch` を使います。
```sh
$ git branch
```
今の場合は、
```
* master
```
と表示されるはずです。master ブランチで作業していることを示しています。

ローカルリポジトリの履歴を表示するには、`git log` を使います。
```sh
$ git log
```
履歴表示は上に行くほど新しいです。
履歴が長いときは、ページがスクロールして流れてしまわないように less が起動されていますので、スペースキーで次のページを表示、b キーで前のページに戻る、q キーで表示をやめることができます。

ローカルリポジトリの履歴を表示する `git log` の面白い機能として、グラフ表示も紹介します。
```sh
$ git log --graph --oneline
```
ブランチが分岐したりマージされる様子がグラフで表示されます。


### 4. ブランチ origin/develop をリモートからチェックアウト（ダウンロード）します。
まず、リモートディレクトリにどんなブランチがあるか表示します。
```sh
$ git branch -r
```

この出力は次のようなものかそれにいくつかのブランチが付け加えられたものになります。

```
  origin/HEAD -> origin/master
  origin/develop
  origin/master
```

リモートブランチに、master のほかに develop もあるはずです。

リモートブランチの develop をローカルにダウンロードしそれをチェックアウトして作業することにします。

```sh
$ git checkout -b  develop origin/develop
```

ブランチを表示します。

```sh
$ git branch
```

表示は下記のようになるはずです。

```
* develop
  master
```

これで、開発用のブランチがダウンロードできました。

このブランチは、

    1. 画面部分を form.html というファイルに分離してある。
    2. エンターキーで「発言」ボタンを押したのと同じことができる。

などが追加してあります。

develop ブランチは後で使用します。


### 5. ブランチ master を元に、新しいブランチを作成します。

新しいブランチを作成する前に、基準となるブランチに移ります。
master ブランチをチェックアウトします。

```sh
$ git checkout master
```

現在のブランチを確認します。

```sh
$ git branch
```
表示が次のように、`*` が master の方についていればオッケーです。
```
  develop
* master
```

次に、このブランチから分岐して、新しいブランチを作成します。
ブランチの名前は、用途に応じたものにするか、あなたのニックネームにするとよいでしょう。
たとえば、改造のテーマが天気予報であれば weather、 時刻回答であれば timereport、 占い機能追加であれば fortune です。

ここでは、占いの機能を追加したソースコードを開発するとして、fortune という名前のブランチを作成します。

```sh
$ git branch fortune
```

ブランチが作成されたか確認するには、次のようにします。
```sh
$ git branch
```
作成したブランチに移って作業するには、ブランチをチェックアウトします。

```sh
$ git checkout fortune
```
今いるブランチがどれなのかを知るには、次のようにします。
```sh
$ git branch
```

表示は次のようになるはずです。
```
  develop
* fortune
  master
```
今いるブランチ名の先頭に `*` がついています。

これで開発の準備が整いました。次はソースコードを編集します。


### 6. ソースコードを編集します。

さて、ここからがあなたの独自の開発を行うところです。

まず、ソースコードを編集する前に、バージョン管理の状態がどうなっているか見てみます。それには、次のようにします。

```sh
$ git status
```

次に、ソースコードを編集しましょう。すでに、別のディレクトリに編集済みのソースコードがある場合は、それをこのディレクトリにコピーしてきます。

ここでは、`../chatbot/` というディレクトリに編集済みのソースコードがあるとして、以下の４つのファイルをこのディレクトリにコピーします。

    ../chatbot/cgi-bin/botengine.py
    ../chatbot/cgi-bin/chatbot.py
    ../chatbot/cgi-bin/fortune.py
    ../chatbot/chatbot-data.json

下記のコマンドを実行してください。
```sh
$ cp ../chatbot/cgi-bin/*.py cgi-bin/
$ cp ../chatbot/chatbot-data.json 
```
続いて、git の状態をみてみます。

```sh
$ git status
```
４つのファイルが変更されたことが示されています。変更内容を見るには、次のようにします。

```sh
$ git diff
```

変更された内容が示されます。スペースキーでページを送ります。q キーで表示を抜けます。

### 7. 変更内容を登録する候補を準備します。
変更の登録は、複数のファイルを同時に行うことができますので、登録候補を `git add` コマンドでステージング（準備）します。
```sh
$ git add cgi-bin/*.py chatbot-data.json
```
ステージングの状態がどうなったか、`git status` で確認します。
```sh
$ git status
```

### 8. 変更内容を登録します。
これらを登録（コミット）するには、つぎのようにします。
```sh
$ git commit -m "占い機能追加。画面をくれりん仕様に変更。より乙女チックに。"
```
変更が登録されたか確認するには、`git log` を見ます。
```sh
$ git log
```

### 9. ローカルブランチをリモートリポジトリに追加します。
占い機能を追加したローカルブランチ fortune を、共同作業者に見てもらうため、リモートリポジトリに書き込み（プッシュ）します。
```sh
$ git push origin fortune
```
リモートブランチに書き込まれたかを確認するには、`git branch -r` を使います。
```sh
$ git branch -r
```
リストに`remotes/origin/fortune` が現れていれば成功です。
GitHubの Web ページでも確認しましょう。chatbot のページ

    https://github.com/HideKobayashi/chatbot

を開いて、左の方の、`Branch: master` となっているボタンを押すと、ブランチのリストが表示されます。その中に、fortune というブランチがあれば成功です。fortune を選んで、`cgi-bin` 以下のフォルダに　`fortune.py` が含まれていることを確認してください。 

これで、共同開発者を含む全ての人に自分が作成したコードを見てもらうことができるようになりました。
ここまでできたら、Chatbot project の管理者にチャットかメールで連絡して、コードを見てもらうとよいでしょう。


### 10. プルリクエストを送ります。
管理者に見てもらうということを GitHub の仕組みで行う方法があります。プルリクエスト (pull request) です。
上記のように、ローカルブランチ　fortune をリモートリポジトリに追加したら、次は、プルリクエストを送ります。

Web ブラウザで GitHub の Chatbot Project のページを開きます。

    https://github.com/HideKobayashi/chatbot

画面の左上の方、`Branch master` のとなりに `New pull request` というボタンがあるので、これをクリックします。
ボタンの設定を 左側 `base: develop` 右側 `compare: fortune` にします。
コメント欄には例えば下記のように記述します。

    占い機能を追加しました。コードをレビューしていただき、問題なければ develop ブランチにマージしていただければ幸いです。

あとは、共同開発者のレビューを待ちます。

### 11. develop ブランチへ fortune ブランチを統合（マージ）する
プルリクエストを送ってすんなりマージできることもありますが、できないこともあります。

そういうときは、develop ブランチへ fortune ブランチをマージする操作をローカルで行ってみます。

ここでは、マージさせたい本流のブランチを develop とします。
まず、develop をチェックアウトします。

```sh
$ git checkout develop
```
次に、develop ブランチへ fortune ブランチを統合します。

```sh
$ git merge fortune
```
これでうまく統合できれば良いですが、うまくできないときは、ソースコードをよく見て調整してください。


## 【Git コマンドのまとめ】
### 状態を見るためのコマンド
ソースコードの状態を見る。
```sh
$ git status
```

ローカルブランチの一覧を見る
```sh
$ git branch
```

リモートブランチの一覧を見る。
```sh
$ git branch -r
```

全て（リモートとローカル）のブランチの一覧を見る。
```sh
$ git branch -a
```

変更の履歴を見る。
```sh
$ git log
```

変更の履歴をグラフ化して見る。
```sh
$ git log --graph --oneline
```

変更した行を表示する
```sh
$ git diff
```

cgi-bin/form.html の変更した行を表示する。
```sh
$ git diff cgi-bin/form.html
```

### 変更を登録するコマンド

変更を登録する準備をする。 cgi-bin/fortune.py の場合。
```sh
$ git add cgi-bin/fortune.py
```

変更を登録する準備をする。全てのファイルの場合。
```sh
$ git add .
```

変更を登録（コミット）する。
```sh
$ git commit -m "変更点をわかりやすい文章で記入"
```

### リモートリポジトリとのやりとり

リモートリポジトリから master ブランチをダウンロード（クローン）する
```sh
$ git clone <リモートリポジトリ> <ディレクトリ名>
```

具体的には、
```sh
$ git clone https://github.com/HideKobayashi/chatbot.git chatbot-dev
```

リモートリポジトリからローカルリポジトリへ最新の master ブランチをとってくる。
```sh
$ git pull origin master
```

リモートリポジトリ の origin/develop ブランチをローカルリポジトリへ develop という名前でとってきてチェックアウトする。
```sh
$ git checkout -b develop origin/develop
```

ローカルリポジトリからリモートの　master ブランチへ　変更をアップロード（push）する
```sh
$ git push origin master
```

ローカルリポジトリからリモートの　develop ブランチへ　変更をアップロード（push）する
```sh
$ git push origin develop
```
