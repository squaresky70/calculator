import tkinter as tk  # tkinter 모듈을 가져옴

# 메인 창 만들기
window = tk.Tk()
window.title("계산기")  # 창 제목 설정
window.geometry("300x400")  # 창 크기 설정 (가로x세로)

# 계산 결과를 보여줄 입력창(Entry) 만들기
display = tk.Entry(window, justify="right", font=("Arial", 24))
display.pack(fill="x", padx=10, pady=10)  # 가로로 꽉 채우고 여백 주기

# 창을 계속 띄워두기 위한 반복문
window.mainloop()
