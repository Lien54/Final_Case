import tkinter as tk
from tkinter import CENTER, IntVar, messagebox as mb

questions = [
    "Q1. Hãy xác định câu lệnh dùng để khởi tạo Repository mới?",
    "Q2. Phải chèn module turtle trước khi sử dụng?",
    "Q3. Trong Python biến cần phải được khai báo trước khi gán cho nó một giá trị?",
    "Q4. Đâu là hàm Python trả về giá trị duy nhất của một đối tượng:",
    "Q5. Trong hàm print() 'sep' dùng để làm gì?"
]
answer_choice = [
    ["git commit",
    "git create",
    "git add",
    "git init"
    ],
    ["True", "False"],
    ["True", "False"],
    ["id()", "refnum()", "ref()", "identity()"],
    ["Để xuống dòng",
    "Để tạo ra các kí tự ngăn cách giữa các object",
    "Để in ra mà hình",
    "Để chèn kí tự vào cuối các object"
    ]
]
answers = [4, 2, 2, 1, 2]

    #!==== class to define QUIZ ====!#
class Quiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(questions)
        self.correct = 0
 
    def display_result(self):
        incorrect_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        incorrect = f"Wrong: {incorrect_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct}\n{incorrect}")
 
    def check_ans(self, q_no):
        if self.opt_selected.get() == answers[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
            window.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = tk.Button(window, text = "Next",
            command = self.next_btn, width = 10, bg = "#0B0766",
            fg = "white", font = ("Courier",16, "bold")
        )
        next_button.place(x = 400, y = 400)

        quit_button = tk.Button(window, text = "Quit",
            command = window.destroy, width = 5,
            bg = "#0F0D51", fg = "white", font = ("Courier", 16," bold")
        )
        quit_button.place(x = 1020, y = 75)
 
    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in answer_choice[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = tk.Label(window, text = questions[self.q_no],
            width = 80, background="#669BBC",
            font = ("Courier", 18,"bold"), anchor = "w")
        q_no.place(x = 70, y = 130)
 
    def display_title(self):
        title = tk.Label(window, text = "QUIZ OF PYTHON",
            width = 65, bg = "#0D638E", fg = "white",
            font = ("Courier", 24, "bold"),
            anchor = "center"
        )
        title.place(x=0, y=1)
 
    def radio_buttons(self):
        q_list = []
        y_pos = 180
        while len(q_list) < 4:
            radio_btn = tk.Radiobutton(window, text = " ",
                variable=self.opt_selected,
                value = len(q_list) + 1, font = ("Courier", 14),
                background = "#669BBC"
            )
            q_list.append(radio_btn)
            radio_btn.place(x = 150, y = y_pos)
            y_pos += 40
        return q_list
 
    #!==== Create the Window ====!#
window = tk.Tk()
window.title("QUIZ")

win_width = 1200
win_height = 520
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("{}x{}+{}+{}".format(
    win_width,
    win_height,
    width//2 - (win_width//2),
    height//2 - (win_height//2))
)
window.resizable(height = None, width = None)
window.config(background="#669BBC")
 
# create an object of the Quiz Class.
quiz = Quiz()
 
window.mainloop()
 
    #!==== END OF THE PROGRAM ====!#