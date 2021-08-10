import os
import pandas as pd
import shutil

spisok = os.listdir(r'C:\Users\new2r\Desktop\FinCenter\prikazi_pr')



for i in spisok:
    name = i.split(' ')
    if name[0] == '№':
        del name[0]
    if name[0] == '1-2-4':
        del name[0]
    os.rename(f'C:\\Users\\new2r\\Desktop\\FinCenter\\prikazi_pr\\{i}', f'C:\\Users\\new2r\\Desktop\\FinCenter\\prikazi_pr\\\\{name[0].split(".")[0]}.pdf')
