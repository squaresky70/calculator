import tkinter as tk  # tkinter 모듈을 가져옴

# 색상을 한 곳에 모아두면 나중에 바꾸기 편함
BG_COLOR = "#2b2b2b"       # 창 배경색
DISPLAY_BG = "#1e1e1e"     # 결과 표시창 배경색
DISPLAY_FG = "#ffffff"     # 결과 표시창 글자색
NUMBER_BG = "#4a4a4a"      # 숫자 버튼 배경색
NUMBER_FG = "#ffffff"      # 숫자 버튼 글자색
OPERATOR_BG = "#ff9500"    # 연산자(+ - * /) 버튼 배경색
OPERATOR_FG = "#ffffff"    # 연산자 버튼 글자색
CLEAR_BG = "#d9534f"       # C 버튼 배경색
EQUAL_BG = "#5cb85c"       # = 버튼 배경색
BTN_FONT = ("Arial", 18, "bold")  # 버튼 글씨체

# 메인 창 만들기
window = tk.Tk()
window.title("계산기")  # 창 제목 설정
window.geometry("300x400")  # 창 크기 설정 (가로x세로)
window.configure(bg=BG_COLOR)

# 계산 결과를 보여줄 입력창(Entry) 만들기
display = tk.Entry(
    window, justify="right", font=("Arial", 24),
    bg=DISPLAY_BG, fg=DISPLAY_FG, bd=0, insertbackground=DISPLAY_FG,
)
display.pack(fill="x", padx=10, pady=10, ipady=10)  # 가로로 꽉 채우고 여백 주기


# 버튼을 누르면 결과 표시창에 글자를 이어서 넣는 함수
def on_click(text):
    display.insert(tk.END, text)


# "=" 버튼을 누르면 화면의 수식을 계산해서 결과를 보여주는 함수
def on_equal():
    try:
        result = eval(display.get())  # 화면에 적힌 수식을 계산
        display.delete(0, tk.END)  # 화면 지우기
        display.insert(tk.END, str(result))  # 계산 결과 보여주기
    except ZeroDivisionError:
        display.delete(0, tk.END)  # 화면 지우기
        display.insert(tk.END, "Error")  # 0으로 나누면 Error 표시
    except Exception:
        display.delete(0, tk.END)  # 화면 지우기
        display.insert(tk.END, "오류")  # 그 외 계산이 안 되면 오류 표시


# "C" 버튼을 누르면 화면을 전부 지우는 함수
def on_clear():
    display.delete(0, tk.END)


# 버튼들을 담을 프레임(틀) 만들기
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(fill="both", expand=True, padx=8, pady=(0, 8))

# 연산자 기호 모음 (색을 다르게 칠하기 위해 구분용으로 사용)
OPERATORS = ("/", "*", "-", "+")

# 격자(grid)에 배치할 버튼 목록: (글자, 행, 열)
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 3),
]

# 목록을 하나씩 꺼내서 버튼으로 만들고 격자에 배치
for text, row, col in buttons:
    is_operator = text in OPERATORS
    btn = tk.Button(
        button_frame, text=text, font=BTN_FONT,
        bg=OPERATOR_BG if is_operator else NUMBER_BG,
        fg=OPERATOR_FG if is_operator else NUMBER_FG,
        bd=0, activebackground=OPERATOR_BG if is_operator else NUMBER_BG,
        command=lambda t=text: on_click(t),  # 눌렀을 때 그 버튼의 글자를 넣음
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

# "C" 버튼: 화면을 지우는 버튼
clear_btn = tk.Button(
    button_frame, text="C", font=BTN_FONT,
    bg=CLEAR_BG, fg="white", bd=0, activebackground=CLEAR_BG,
    command=on_clear,
)
clear_btn.grid(row=3, column=2, sticky="nsew", padx=4, pady=4)

# "=" 버튼은 맨 아래에 가로로 길게 배치
equal_btn = tk.Button(
    button_frame, text="=", font=BTN_FONT,
    bg=EQUAL_BG, fg="white", bd=0, activebackground=EQUAL_BG,
    command=on_equal,
)
equal_btn.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

# 버튼 크기가 창에 맞춰 늘어나도록 행/열 비율 설정
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

# 창을 계속 띄워두기 위한 반복문
window.mainloop()
