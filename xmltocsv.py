# Code to convert XML to CSV file

import pandas as pd

tree = ET.parse(os.getcwd() + "\\zip_file\\" + os.listdir(os.getcwd()+'\\zip_file')[0])

cols = [
    "FinInstrmGnlAttrbts.Id",
    "FinInstrmGnlAttrbts.FullNm",
    "FinInstrmGnlAttrbts.ClssfctnTp",
    "FinInstrmGnlAttrbts.CmmdtyDerivInd",
    "FinInstrmGnlAttrbts.NtnlCcy",
    "Issr"
]
rows = []

# Iterating through each tag
for i in tree.iter():
    if i.tag.split('}')[1] == "FinInstrmGnlAttrbts":
        for k in i.iter():
            if k.tag.split('}')[1] == "Id":
                id_ = k.text
            elif k.tag.split('}')[1] == "FullNm":
                fname = k.text
            elif k.tag.split('}')[1] == "ClssfctnTp":
                ctp = k.text
            elif k.tag.split('}')[1] == "CmmdtyDerivInd":
                cdi = k.text
            elif k.tag.split('}')[1] == "NtnlCcy":
                ncy = k.text
    if i.tag.split('}')[1] == "Issr":
        issr = i.text
        rows.append({
            "FinInstrmGnlAttrbts.Id": id_,
            "FinInstrmGnlAttrbts.FullNm": fname,
            "FinInstrmGnlAttrbts.ClssfctnTp": ctp,
            "FinInstrmGnlAttrbts.CmmdtyDerivInd": cdi,
            "FinInstrmGnlAttrbts.NtnlCcy": ncy,
            "Issr": issr
        })

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to CSV.
df.to_csv('csv_file.csv')