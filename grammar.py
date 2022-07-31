
# 【標準入出力】
print("文字列")


# 構文の途中で改行を行いたいときは、バックスラッシュを使うことで
# 改行をしても同じ実行結果になる。
print\
  ("実行結果は変わらない")

#【算術演算子】
# +-*/ 四則演算
# ** 累乗
# % 剰余
# // 整数の割り算（小数点以下切り捨て）

#【比較演算子】
# > より大きい
# < より小さい
# >= 以上
# <= 以下
# == 等価
# != 非等価

#【論理演算子】
# and かつ
# or あるいは
# not 否定

# Pythonはインデントで構文を認識します。
# for文・if文内で処理されてほしいコードは適切に字下げする必要があります。

# 【繰り返し処理】
for i in range(100):
  print("文字列")

# 【分岐処理】 ifを入れ子するときはelifと書きます。
time = "朝"
if time == "朝":
  print("おはよう")
elif time == "夜":
  print("こんばんは")
else:
  print("こんにちは")

# 【関数の定義】
def function_name(arg):      # function_name … 関数名,  arg … 引数
  local_variable = arg       # ローカル変数（関数内でのみ参照できる変数）
  #このインデントで関数の処理内容を書く
  local_variable *= 3        #演算した後の結果を変数に再代入する処理
  return local_variable      #returnで関数を抜ける。returnがない場合、Noneを返す関数になる

#【組み込み関数の使い方】
len("文字列") # 引数のオブジェクトの長さ（文字数など）を返す
str(100) # 引数のオブジェクトをStrデータ型に変換する
int('100') # 引数のオブジェクトをIntデータ型に変換する

# 例外処理
a = 10
b = 0
try:
  print(a/b)
except ZeroDivisionError: # 0除算のエラー発生を検知して下部に続くコードを実行
  print("bの値が0です")
# 注意として、try句の中で定義した変数はexcept句のなかで使用しないこと。
# ↑変数が定義される前に例外が発生すると、検知したものとは別の例外が発生するため。

# ドキュメンテーション文字列
# ⇒ 1行目に関数の説明、その下に引数とその型や返り値について書く。
def add(x,y):
  """
  x + yの値を返します。
  :param x: int.
  :param y: int.
  :return: int sum of x and y.
  """
  return x + y

# ～イテラブルなオブジェクトについて～
# イテラブルとは、繰り返し系の処理で要素を１つずつ取り出せるという意味。
# 様々な値を格納できるコンテナであり、格納した値のインデックスを持っている。

# 1.リスト … ミュータブル（変更可能）なコンテナ
fruit = list()
fruit = ["Apple","Orange","Pear"] # 角カッコの書き方なら、値を入れた状態で宣言できる
fruit.append("Banana") # リスト内の最後尾に新しい要素を追加するappendメソッド
print(fruit[1]) # インデックス指定の出力例。0から数えるので、この場合Orangeが出力される
# 存在しないインデックスを指定した場合、例外「IndexError: list index out of range」となる
fruit[2] = "Peach" # ミュータブルなので後から置き換え可能。この場合、PearがPeachに置き換わる
fruit.pop() # popメソッドを使用することでリストの最後尾から要素を除去できる
fruit_other = ["Grapes","Kiwi","Melon"]
fruit + fruit_other # +演算子で結合できる
