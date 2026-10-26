"""
Runs the calculation cells of the notebook (unchanged) and exports everything the web page needs
to data.json. Re-run this if the spreadsheet or the notebook logic changes.

Usage:  python export_data.py <notebook.ipynb> <results.xlsx> <out_data.json>
"""
import json, sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import textwrap

nb_path, xlsx, out = sys.argv[1:4]
nb = json.load(open(nb_path, encoding="utf-8"))
code = {c.get("id"): "".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"}

g = {"pd": pd, "plt": plt, "textwrap": textwrap}
exec(code["32f49746"], g)                 # settings cell (imports, titles)
g["DATA_FILE"] = xlsx                     # point at the spreadsheet we were given
exec(code["93070bbe"], g)                 # load + rank + averages: the notebook's own logic
df, mmss, clean = g["df"], g["mmss"], g["clean"]

def f4(x): return round(float(x), 4)

cats = sorted(df["category"].unique())
rows = []
for _, r in df.iterrows():
    chip_s, k5_s = r["chip_s"], r["k5_s"]
    rows.append({
        "b": str(r["bib"]),                         # bib
        "n": str(r["name"]),                        # masked name
        "g": r["gender"],                           # M / F
        "c": cats.index(r["category"]),             # category (index into "categories")
        "gun": clean(r["gun"]), "chip": clean(r["chip"]), "k5": clean(r["k5"]),
        "sp": f"{10 / (chip_s / 3600):.2f}",        # speed km/h, as shown on the card
        "pc": mmss(chip_s / 10),                    # whole-race pace
        "p5": mmss(k5_s / 5),                       # pace first 5 km
        "p10": mmss((chip_s - k5_s) / 5),           # pace second 5 km
        "s5": f4(r["speed_5"]), "s10": f4(r["speed_10"]),   # leg speeds for the chart
        "op": int(r["overall_pos"]), "gp": int(r["gender_pos"]), "cp": int(r["cat_pos"]),
        "opc": int(r["overall_pos_chip"]), "gpc": int(r["gender_pos_chip"]), "cpc": int(r["cat_pos_chip"]),
        "gt": int(r["gender_total"]), "ct": int(r["cat_total"]),
    })

def avg(sub): return [f4(sub["speed_5"].mean()), f4(sub["speed_10"].mean())]
averages = {
    "overall": avg(df),
    "gender": {gd: avg(df[df.gender == gd]) for gd in sorted(df.gender.unique())},
    "cat_gender": {f"{c}|{gd}": avg(df[(df.category == c) & (df.gender == gd)])
                   for c in cats for gd in sorted(df.gender.unique())
                   if len(df[(df.category == c) & (df.gender == gd)])},
}
data = {"total": int(g["total_runners"]), "categories": cats, "averages": averages, "runners": rows}
json.dump(data, open(out, "w", encoding="utf-8"), separators=(",", ":"), ensure_ascii=False)
print(f"wrote {out}: {len(rows)} runners")
