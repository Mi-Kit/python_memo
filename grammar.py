# 【標準入出力】
print("文字列")

# 構文の途中で改行を行いたいときは、バックスラッシュを使うことで
# 改行をしても同じ実行結果になります。
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
#　and かつ
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