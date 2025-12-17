import tkinter as tk

'''
Tkinter Grid 佈局實作
出處：根據題目規格自行撰寫
'''

root = tk.Tk()
root.title("Tkinter Grid")
root.geometry("400x300")
root.resizable(True, True)

# 設定列與欄的權重 (Weight) 以達成自適應
root.columnconfigure(1, weight=1) # 中間欄可縮放
root.rowconfigure(1, weight=1)    # 黃色區域可縮放

# 1. 左側欄 (跨越 3 列)
left_sidebar = tk.Frame(root, bg='lightgreen', width=40)
left_sidebar.grid(row=0, column=0, rowspan=3, sticky='nsew')

# 2. 右側欄 (跨越 3 列)
right_sidebar = tk.Frame(root, bg='lightblue', width=40)
right_sidebar.grid(row=0, column=2, rowspan=3, sticky='nsew')

# 3. 上層紅色區塊 (固定高度 60)
top_frame = tk.Frame(root, bg='red', height=60)
top_frame.grid(row=0, column=1, sticky='nsew')
top_frame.grid_propagate(False)

# 紅色區塊內的 Labels
top_frame.columnconfigure((0,1,2), weight=1) # 均分三個位置
tk.Label(top_frame, text="left", bg='white').grid(row=0, column=0, sticky='n')
tk.Label(top_frame, text="center", bg='white').grid(row=0, column=1, sticky='n')
tk.Label(top_frame, text="Right", bg='white').grid(row=0, column=2, sticky='n')

# 4. 中層黃色區塊 (權重最高，填滿空間)
middle_frame = tk.Frame(root, bg='yellow')
middle_frame.grid(row=1, column=1, sticky='nsew')

# 5. 下層藍色區塊 (固定高度 30)
bottom_frame = tk.Frame(root, bg='blue', height=30)
bottom_frame.grid(row=2, column=1, sticky='nsew')

root.mainloop()