# -*- coding: utf8 -*-
import sys
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

# ウィンドウタイトル
root.title(u"Title")

# ウインドウサイズ
root.geometry('400x300')

# ラベル
Static1 = tk.Label(text=u'Entry', foreground='#ff0000', background='#90caf9')

# .placeで位置指定。
Static1.place(x=10, y=80)

# 画面の上からいい感じに要素を配置したいときは.pack()

# Entryはテキストボックスのこと
Entry1 = tk.Entry()
Entry1.place(x=10, y=100)

Entry2 = tk.Entry(width=50)  # widthで幅指定。この場合は半角文字で50字分の幅ということ
Entry2.insert(tk.END, u'文字列') # Entryに最初から文字を入れておく場合はinsertメソッド
Entry2.pack()

# Entryの値を取得するgetメソッド
Entry2_value = Entry2.get()
print(Entry2_value)

# ボタン1が押されたら呼び出される関数
def deleteEntry(event):
    # Entryの中身をすべて削除
    Entry2.delete(0, tk.END)

# ボタン2が押されたら呼び出される関数
def showMessage(text):
    tkm.showinfo('ダイアログのタイトル', text)

# Button設置
Button1 = tk.Button(text=u'ボタン', width=50)
Button1.bind("<Button-1>", deleteEntry) # ボタンが押されたときに実行される関数をバインド
Button1.pack()

# メッセージボックスを表示
#  関数に引数を渡す場合はcommandオプションとlambda式を使う
Button2 = tk.Button(text=u'メッセージ表示', width=50, command=lambda: showMessage(Entry1.get()))
Button2.pack()

# リストボックス設置
ListBox1 = tk.Listbox(width=55, height=14)
ListBox1.pack()

# ボタンが押されたらリストボックスに、Entryの中身を追加
def addList(text):
    ListBox1.insert(tk.END, text)

# ボタンが押されたらリストボックスの選択されている部分を削除
def deleteSelectedList():
    # 選択されているリストの番号を格納
    selectedIndex = tk.ACTIVE
    # 上記を削除
    ListBox1.delete(selectedIndex)

Button3 = tk.Button(text=u'追加', width=50, command=lambda: addList(Entry2.get()))
Button3.pack()

Button4 = tk.Button(text=u'削除', width=50, command=lambda: deleteSelectedList())
Button4.pack()


# ダイアログの種類
  # tkm.showinfo('ダイアログのタイトル', '普通のダイアログ')
  # tkm.showwarning('ダイアログのタイトル', 'ワーニングダイアログ')
  # tkm.showerror('ダイアログのタイトル', 'エラーアイコンダイアログ')

  # YES/NOなダイアログ（YESがクリックされたら戻り値がtrue、NOならfalse）
    # tkm.askyesno('タイトル', 'YES/NO')

  # リトライキャンセルダイアログ（リトライがクリックされたら戻り値がtrue、キャンセルならfalse）
    # tkm.askretrycancel('タイトル', 'リトライ/キャンセル')

  # OK/NOダイアログ（リトライがクリックされたら戻り値が'yes'、キャンセルなら'no'）
    # tkm.askquestion('タイトル', 'OK/NO')

  # OK/CANCELダイアログ（OKがクリックされたら戻り値はtrue、キャンセルならfalse
    # tkm.askokcancel('タイトル', 'OK/CANCEL')

root.mainloop()
