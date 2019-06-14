Conan C/C++ Package Managerの使い方のメモ

## Conanのインストール

```
pip install conan
```

## 自作モジュールのビルド
CMakeLists.txtには以下のような内容を記述する。
`conan_basic_setup`を実行すると自動的に全てのインクルードディレクトリ、リンクディレクトリが設定される。
`${CONAN_LIBS}`には依存するすべてのライブラリが含まれる。

```CMake
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test test.cpp)
target_link_libraries(test ${CONAN_LIBS})
```

`conanfile.txt`には依存するライブラリを設定する。

```
[requires]
testRTC/0.1@demo/testing

[generators]
cmake
```

以下のコマンドで依存ライブラリをインストールする。

```
conan install . --build=missing
```

以下のコマンドでCMake実行。別フォルダでできるかは不明。

```
cmake .
```


## パッケージの作成、テスト
以下のコマンドでサンプルを作成できる。
```
conan new Hello/0.1 -t
```

以下のコマンドでテストを実行。test_package以下のファイルは全てテスト用。

```
conan create . demo/testing
```

## パッケージのアップロード
今回は[JFlog Bintray](https://bintray.com)を使用する。

まずはサインインを行う。
![image](https://user-images.githubusercontent.com/6216077/59480739-cb65ce80-8e9c-11e9-9b3a-fcb0dfb7b963.png)

サインイン後、新規にリポジトリを作成する。
![image](https://user-images.githubusercontent.com/6216077/59480787-f4865f00-8e9c-11e9-958d-6442fd751755.png)

ここでTypeをConanに設定する。
![image](https://user-images.githubusercontent.com/6216077/59480818-1384f100-8e9d-11e9-8aea-686e346910be.png)

作成後、API Keyを取得する。
`Edit Profile`->`API Key`から取得できる。


以下のSET ME UP!をクリックしてください。

![image](https://user-images.githubusercontent.com/6216077/59481038-b76e9c80-8e9d-11e9-84f6-6a9765ffd1b3.png)

以下からコマンドによる作業になります。

![image](https://user-images.githubusercontent.com/6216077/59481117-087e9080-8e9e-11e9-90eb-db9bc3064707.png)

まずはConanクライアントの設定を行ってください。

```
conan remote add <リモート名> https://api.bintray.com/conan/<組織名>/<リポジトリ名>
conan user -p <APIKEY> -r <リモート名> <ユーザー名>
```

上記のリモート名は適当な名前を付けてください。

![image](https://user-images.githubusercontent.com/6216077/59481210-5398a380-8e9e-11e9-9b7c-f28531dc24a2.png)

リポジトリにファイルをアップロードします。
以下のコマンドだとインストール済みのパッケージ全てについてアップロードするかの選択が出てしまうため、1つだけアップロードする方法は要調査。

```
conan upload "*" -r <リモート名> --all
```


アップロードしたパッケージを使用する場合はconanfile.txtに以下のように(`パッケージ名/バージョン@user/channel`)記載する。

```
[requires]
testRTC/0.1@demo/testing
```
