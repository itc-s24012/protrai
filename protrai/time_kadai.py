# s24012
# 実行が確認出来たら時間を表示される「時計アプリ」を作ってみたいと思います
# 時計アプリはモジュール名「time_kadai.py」作成します
# 時計アプリを使いやすくバージョンアップデートしていきます

import datetime
import tkinter as tk # GUIでアプリを作ることができるモジュール

# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    #
    lbl.config(text=current_time)
    root.after(1000, update_time) # 自分をもう一回呼び出す
    
# tkinterのウインドウを作成
root = tk.Tk() # 初めてのおまじない

root.title("現在の時刻")
#
lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 20))
lbl.pack()

# 関数の呼び出し
update_time()


root.mainloop() 
