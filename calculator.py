import tkinter as tk  # tkinter 모듈을 가져옴

# 메인 창 만들기
window = tk.Tk()
window.title("계산기")  # 창 제목 설정
window.geometry("300x400")  # 창 크기 설정 (가로x세로)

# 계산 결과를 보여줄 입력창(Entry) 만들기
display = tk.Entry(window, justify="right", font=("Arial", 24))
display.pack(fill="x", padx=10, pady=10)  # 가로로 꽉 채우고 여백 주기


# 버튼을 누르면 결과 표시창에 글자를 이어서 넣는 함수
def on_click(text):
    display.insert(tk.END, text)


# "=" 버튼을 누르면 화면의 수식을 계산해서 결과를 보여주는 함수
def on_equal():
    try:
        result = eval(display.get())  # 화면에 적힌 수식을 계산
        display.delete(0, tk.END)  # 화면 지우기
        display.insert(tk.END, str(result))  # 계산 결과 보여주기
    except Exception:
        display.delete(0, tk.END)  # 화면 지우기
        display.insert(tk.END, "오류")  # 계산이 안 되면 오류 표시


# 버튼들을 담을 프레임(틀) 만들기
button_frame = tk.Frame(window)
button_frame.pack(fill="both", expand=True)

# 격자(grid)에 배치할 버튼 목록: (글자, 행, 열)
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 3),
]

# 목록을 하나씩 꺼내서 버튼으로 만들고 격자에 배치
for text, row, col in buttons:
    btn = tk.Button(
        button_frame, text=text, font=("Arial", 18),
        command=lambda t=text: on_click(t),  # 눌렀을 때 그 버튼의 글자를 넣음
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# "C" 버튼은 아직 기능 없이 배치만 함
clear_btn = tk.Button(button_frame, text="C", font=("Arial", 18))
clear_btn.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

# "=" 버튼은 맨 아래에 가로로 길게 배치
equal_btn = tk.Button(button_frame, text="=", font=("Arial", 18), command=on_equal)
equal_btn.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

# 버튼 크기가 창에 맞춰 늘어나도록 행/열 비율 설정
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# 창을 계속 띄워두기 위한 반복문
window.mainloop()
