import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)

fpp = pd.read_excel(file_path,sheet_name="Detailed")

print(fpp.head(5))
