# s24012 def4_kadai.py
#main関数を使ったおみくじ

import random
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

# エントリーポイントの定義
def main():
    kekka = omikuji()
    print("結果は",kekka,"です")

if __name__== "__main__":
    main()
