# quiz4
Pack: 先切割左右兩側固定寬度，再將中間剩餘空間切為 Top, Bottom，最後讓 Middle 填滿。

Grid: 使用 rowconfigure 與 columnconfigure 設定權重 (weight)，讓中間欄位與黃色列具備伸縮性。

Place: 全程使用相對尺寸（如 relwidth=0.8），確保在任何視窗大小下比例皆維持一致。
