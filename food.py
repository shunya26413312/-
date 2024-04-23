import random

import random

import random

def random_number():
    min = int(input("あなたの好きな番号を入れてください: "))
    max = int(input("先ほど入れた番号より大きい番号を入れてください: "))
    between_number = random.randint(min, max)

    for i in range(5):
        input_number = int(input("数字を当ててください: "))
        if between_number == input_number:
            return "勝ちました！正解の数字は " + str(input_number) + " です。"

        if i == 4:
            if between_number != input_number:
                print( "残念でした、ゲームオーバーです。正解の数字は " + str(between_number) + " でした。")
            
        else:
            print("残念！もう一度試してみてください。")

# 関数を呼び出してゲームを開始
random_number()