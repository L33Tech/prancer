import pandas as pd

table = pd.read_csv('content/clean_dialog.csv', encoding = 'unicode_escape')

file = open("lines" + ".txt", "w", encoding="utf-8")

for i in table["dialog"]:
    if str(i)[0] == " ":
        i = i[1:]
    file.writelines(str(i))
    file.write("\n")
    
print("Done!")