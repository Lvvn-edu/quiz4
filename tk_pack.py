import tkinter as tk

'''
Tkinter Pack 佈局實作
出處：根據題目規格自行撰寫
'''

root = tk.Tk()
root.title("Tkinter Pack")
root.geometry("400x300")
root.resizable(True, True)  # 支援加分題自適應

# 1. 左側欄 (固定寬度 40)
left_sidebar = tk.Frame(root, bg='lightgreen', width=40)
left_sidebar.pack(side='left', fill='y')

# 2. 右側欄 (固定寬度 40)
right_sidebar = tk.Frame(root, bg='lightblue', width=40)
right_sidebar.pack(side='right', fill='y')

# 3. 中間區域：上層 (高度 60)
top_frame = tk.Frame(root, bg='red', height=60)
top_frame.pack(side='top', fill='x')
top_frame.pack_propagate(False) # 防止被 Label 撐開縮小

# 在紅色區塊內加入 Label
labels = ["left", "center", "Right"]
for text in labels:
    lbl = tk.Label(top_frame, text=text, bg='white', fg='black')
    # 使用 pack 的 side 並靠上對齊
    lbl.pack(side='left', expand=True, anchor='n')

# 4. 中間區域：下層 (高度 30)
bottom_frame = tk.Frame(root, bg='blue', height=30)
bottom_frame.pack(side='bottom', fill='x')

# 5. 中間區域：中層 (填滿剩餘空間)
# expand=True 搭配 fill='both' 是自適應的關鍵
middle_frame = tk.Frame(root, bg='yellow')
middle_frame.pack(side='top', fill='both', expand=True)

root.mainloop()