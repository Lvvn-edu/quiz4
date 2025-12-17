import tkinter as tk

'''
Tkinter Place 佈局實作 (百分比自適應)
出處：根據題目規格自行撰寫
'''

root = tk.Tk()
root.title("Tkinter Place")
root.geometry("400x300")
root.resizable(True, True)

# 1. 左側欄 (寬度 10%)
tk.Frame(root, bg='lightgreen').place(relx=0, rely=0, relwidth=0.1, relheight=1.0)

# 2. 右側欄 (寬度 10%, 從 90% 位置開始)
tk.Frame(root, bg='lightblue').place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)

# 3. 紅色區塊 (寬 80%, 高 20%)
top_frame = tk.Frame(root, bg='red')
top_frame.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)

# Label 對齊 (使用 relx 均分位置，anchor='n' 靠上)
tk.Label(top_frame, text="left", bg='white').place(relx=0.2, rely=0, anchor='n')
tk.Label(top_frame, text="center", bg='white').place(relx=0.5, rely=0, anchor='n')
tk.Label(top_frame, text="Right", bg='white').place(relx=0.8, rely=0, anchor='n')

# 4. 黃色區塊 (寬 80%, 高 70%, 位於紅色下方)
tk.Frame(root, bg='yellow').place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

# 5. 藍色區塊 (寬 80%, 高 10%, 底部)
tk.Frame(root, bg='blue').place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1)

root.mainloop()