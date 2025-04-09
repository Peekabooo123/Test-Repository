import tkinter as tk
from tkinter import ttk
import random
# from playsound import playsound
import os

class KanaLearner:
    def __init__(self, root):
        self.root = root
        self.root.title("日语假名学习助手")
        self.flag = 0
        
        # 平假名数据（清音）
        self.hiragana = [
            {'kana': 'あ', 'romaji': 'a', 'sound': 'sounds/a.mp3'},
            {'kana': 'い', 'romaji': 'i', 'sound': 'sounds/i.mp3'},
            {'kana': 'う', 'romaji': 'u', 'sound': 'sounds/u.mp3'},
            {'kana': 'え', 'romaji': 'e', 'sound': 'sounds/e.mp3'},
            {'kana': 'お', 'romaji': 'o', 'sound': 'sounds/o.mp3'},
            
            {'kana': 'か', 'romaji': 'ka', 'sound': 'sounds/ka.mp3'},
            {'kana': 'き', 'romaji': 'ki', 'sound': 'sounds/ki.mp3'},
            {'kana': 'く', 'romaji': 'ku', 'sound': 'sounds/ku.mp3'},
            {'kana': 'け', 'romaji': 'ke', 'sound': 'sounds/ke.mp3'},
            {'kana': 'こ', 'romaji': 'ko', 'sound': 'sounds/ko.mp3'},
            
            {'kana': 'さ', 'romaji': 'sa', 'sound': 'sounds/sa.mp3'},
            {'kana': 'し', 'romaji': 'shi', 'sound': 'sounds/shi.mp3'},
            {'kana': 'す', 'romaji': 'su', 'sound': 'sounds/su.mp3'},
            {'kana': 'せ', 'romaji': 'se', 'sound': 'sounds/se.mp3'},
            {'kana': 'そ', 'romaji': 'so', 'sound': 'sounds/so.mp3'},
            
            {'kana': 'た', 'romaji': 'ta', 'sound': 'sounds/ta.mp3'},
            {'kana': 'ち', 'romaji': 'chi', 'sound': 'sounds/chi.mp3'},
            {'kana': 'つ', 'romaji': 'tsu', 'sound': 'sounds/tsu.mp3'},
            {'kana': 'て', 'romaji': 'te', 'sound': 'sounds/te.mp3'},
            {'kana': 'と', 'romaji': 'to', 'sound': 'sounds/to.mp3'},
            
            {'kana': 'な', 'romaji': 'na', 'sound': 'sounds/na.mp3'},
            {'kana': 'に', 'romaji': 'ni', 'sound': 'sounds/ni.mp3'},
            {'kana': 'ぬ', 'romaji': 'nu', 'sound': 'sounds/nu.mp3'},
            {'kana': 'ね', 'romaji': 'ne', 'sound': 'sounds/ne.mp3'},
            {'kana': 'の', 'romaji': 'no', 'sound': 'sounds/no.mp3'},
            
            {'kana': 'は', 'romaji': 'ha', 'sound': 'sounds/ha.mp3'},
            {'kana': 'ひ', 'romaji': 'hi', 'sound': 'sounds/hi.mp3'},
            {'kana': 'ふ', 'romaji': 'fu', 'sound': 'sounds/fu.mp3'},
            {'kana': 'へ', 'romaji': 'he', 'sound': 'sounds/he.mp3'},
            {'kana': 'ほ', 'romaji': 'ho', 'sound': 'sounds/ho.mp3'},
            
            {'kana': 'ま', 'romaji': 'ma', 'sound': 'sounds/ma.mp3'},
            {'kana': 'み', 'romaji': 'mi', 'sound': 'sounds/mi.mp3'},
            {'kana': 'む', 'romaji': 'mu', 'sound': 'sounds/mu.mp3'},
            {'kana': 'め', 'romaji': 'me', 'sound': 'sounds/me.mp3'},
            {'kana': 'も', 'romaji': 'mo', 'sound': 'sounds/mo.mp3'},
            
            {'kana': 'や', 'romaji': 'ya', 'sound': 'sounds/ya.mp3'},
            {'kana': 'ゆ', 'romaji': 'yu', 'sound': 'sounds/yu.mp3'},
            {'kana': 'よ', 'romaji': 'yo', 'sound': 'sounds/yo.mp3'},
            
            {'kana': 'ら', 'romaji': 'ra', 'sound': 'sounds/ra.mp3'},
            {'kana': 'り', 'romaji': 'ri', 'sound': 'sounds/ri.mp3'},
            {'kana': 'る', 'romaji': 'ru', 'sound': 'sounds/ru.mp3'},
            {'kana': 'れ', 'romaji': 're', 'sound': 'sounds/re.mp3'},
            {'kana': 'ろ', 'romaji': 'ro', 'sound': 'sounds/ro.mp3'},
            
            {'kana': 'わ', 'romaji': 'wa', 'sound': 'sounds/wa.mp3'},
            {'kana': 'を', 'romaji': 'wo', 'sound': 'sounds/wo.mp3'},
            {'kana': 'ん', 'romaji': 'n', 'sound': 'sounds/n.mp3'}
        ]

        # 片假名数据（清音）
        self.katakana = [
            {'kana': 'ア', 'romaji': 'a', 'sound': 'sounds/a.mp3'},
            {'kana': 'イ', 'romaji': 'i', 'sound': 'sounds/i.mp3'},
            {'kana': 'ウ', 'romaji': 'u', 'sound': 'sounds/u.mp3'},
            {'kana': 'エ', 'romaji': 'e', 'sound': 'sounds/e.mp3'},
            {'kana': 'オ', 'romaji': 'o', 'sound': 'sounds/o.mp3'},
            
            {'kana': 'カ', 'romaji': 'ka', 'sound': 'sounds/ka.mp3'},
            {'kana': 'キ', 'romaji': 'ki', 'sound': 'sounds/ki.mp3'},
            {'kana': 'ク', 'romaji': 'ku', 'sound': 'sounds/ku.mp3'},
            {'kana': 'ケ', 'romaji': 'ke', 'sound': 'sounds/ke.mp3'},
            {'kana': 'コ', 'romaji': 'ko', 'sound': 'sounds/ko.mp3'},
            
            {'kana': 'サ', 'romaji': 'sa', 'sound': 'sounds/sa.mp3'},
            {'kana': 'シ', 'romaji': 'shi', 'sound': 'sounds/shi.mp3'},
            {'kana': 'ス', 'romaji': 'su', 'sound': 'sounds/su.mp3'},
            {'kana': 'セ', 'romaji': 'se', 'sound': 'sounds/se.mp3'},
            {'kana': 'ソ', 'romaji': 'so', 'sound': 'sounds/so.mp3'},
            
            {'kana': 'タ', 'romaji': 'ta', 'sound': 'sounds/ta.mp3'},
            {'kana': 'チ', 'romaji': 'chi', 'sound': 'sounds/chi.mp3'},
            {'kana': 'ツ', 'romaji': 'tsu', 'sound': 'sounds/tsu.mp3'},
            {'kana': 'テ', 'romaji': 'te', 'sound': 'sounds/te.mp3'},
            {'kana': 'ト', 'romaji': 'to', 'sound': 'sounds/to.mp3'},
            
            {'kana': 'ナ', 'romaji': 'na', 'sound': 'sounds/na.mp3'},
            {'kana': 'ニ', 'romaji': 'ni', 'sound': 'sounds/ni.mp3'},
            {'kana': 'ヌ', 'romaji': 'nu', 'sound': 'sounds/nu.mp3'},
            {'kana': 'ネ', 'romaji': 'ne', 'sound': 'sounds/ne.mp3'},
            {'kana': 'ノ', 'romaji': 'no', 'sound': 'sounds/no.mp3'},
            
            {'kana': 'ハ', 'romaji': 'ha', 'sound': 'sounds/ha.mp3'},
            {'kana': 'ヒ', 'romaji': 'hi', 'sound': 'sounds/hi.mp3'},
            {'kana': 'フ', 'romaji': 'fu', 'sound': 'sounds/fu.mp3'},
            {'kana': 'ヘ', 'romaji': 'he', 'sound': 'sounds/he.mp3'},
            {'kana': 'ホ', 'romaji': 'ho', 'sound': 'sounds/ho.mp3'},
            
            {'kana': 'マ', 'romaji': 'ma', 'sound': 'sounds/ma.mp3'},
            {'kana': 'ミ', 'romaji': 'mi', 'sound': 'sounds/mi.mp3'},
            {'kana': 'ム', 'romaji': 'mu', 'sound': 'sounds/mu.mp3'},
            {'kana': 'メ', 'romaji': 'me', 'sound': 'sounds/me.mp3'},
            {'kana': 'モ', 'romaji': 'mo', 'sound': 'sounds/mo.mp3'},
            
            {'kana': 'ヤ', 'romaji': 'ya', 'sound': 'sounds/ya.mp3'},
            {'kana': 'ユ', 'romaji': 'yu', 'sound': 'sounds/yu.mp3'},
            {'kana': 'ヨ', 'romaji': 'yo', 'sound': 'sounds/yo.mp3'},
            
            {'kana': 'ラ', 'romaji': 'ra', 'sound': 'sounds/ra.mp3'},
            {'kana': 'リ', 'romaji': 'ri', 'sound': 'sounds/ri.mp3'},
            {'kana': 'ル', 'romaji': 'ru', 'sound': 'sounds/ru.mp3'},
            {'kana': 'レ', 'romaji': 're', 'sound': 'sounds/re.mp3'},
            {'kana': 'ロ', 'romaji': 'ro', 'sound': 'sounds/ro.mp3'},
            
            {'kana': 'ワ', 'romaji': 'wa', 'sound': 'sounds/wa.mp3'},
            {'kana': 'ヲ', 'romaji': 'wo', 'sound': 'sounds/wo.mp3'},
            {'kana': 'ン', 'romaji': 'n', 'sound': 'sounds/n.mp3'}
        ]
        # print(type(self.hiragana[0]))
        
        # 界面设置
        self.create_widgets()
        self.current_kana = None
        self.current_mode = "hiragana"
        self.show_random_kana()
    
    def create_widgets(self):
        # 模式选择
        self.mode_frame = ttk.Frame(self.root)
        self.mode_frame.pack(pady=10)
        
        ttk.Button(self.mode_frame, text="平假名", command=lambda: self.set_mode("hiragana")).grid(row=0, column=0)
        ttk.Button(self.mode_frame, text="片假名", command=lambda: self.set_mode("katakana")).grid(row=0, column=1)
        ttk.Button(self.mode_frame, text="全部", command=lambda: self.set_mode("all")).grid(row=0, column=2)
        
        # 假名显示
        self.kana_label = ttk.Label(self.root, text="", font=("MS Gothic", 200))
        self.kana_label.pack(pady=20)
        
        # 罗马字显示
        self.romaji_label = ttk.Label(self.root, text="", font=("Arial", 50))
        self.romaji_label.pack(pady=10)
        
        # 练习模式
        self.practice_frame = ttk.LabelFrame(self.root, text="练习模式")
        self.practice_frame.pack(pady=10, fill="x")
        
        self.answer_entry = ttk.Entry(self.practice_frame, width=20)
        self.answer_entry.grid(row=0, column=0, padx=5)
        
        self.button = ttk.Button(self.practice_frame, text="提交", command=self.check_answer)
        self.button.grid(row=0, column=1)
        # self.root.bind("<Return>", self.bind_enter_key)
        self.root.bind('<Return>', lambda event: self.button.invoke())
        
        self.result_label = ttk.Label(self.practice_frame, text="")
        self.result_label.grid(row=1, column=0, columnspan=2)
        
        # 控制按钮
        ttk.Button(self.root, text="下一个", command=self.show_random_kana).pack(pady=10)

    def bind_enter_key(self,event):
        self.button.invoke()

    def set_mode(self, mode):
        self.current_mode = mode
        self.show_random_kana()
    
    def show_random_kana(self):
        if self.current_mode == "hiragana":
            pool = self.hiragana
        elif self.current_mode == "katakana":
            pool = self.katakana
        else:
            pool = self.hiragana + self.katakana
        
        self.i = random.choice(range(len(self.hiragana)))
        self.current_kana = pool[self.i]
        # print(type(pool))
        print(self.i, self.current_kana['romaji'])

        self.kana_label.config(text=self.current_kana['kana'])
        self.romaji_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    
    def check_answer(self):
        if self.flag == 0:
            user_answer = self.answer_entry.get().strip().lower()
            correct_answer = self.current_kana['romaji'].lower()
            if user_answer:
                if user_answer == correct_answer:
                    self.result_label.config(text="正确！", foreground="green")
                    self.romaji_label.config(text=correct_answer)
                    self.flag += 1
                else:
                    self.result_label.config(text=f"错误，正确答案是：{correct_answer}", foreground="red")
                    self.romaji_label.config(text=correct_answer)
            else:
                self.result_label.config(text="Please enter your answer!", foreground="red")
                    
        else:
            self.show_random_kana()
            self.flag = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = KanaLearner(root)
    root.mainloop()

    