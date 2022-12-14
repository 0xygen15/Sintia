import json
import tkinter as tk

#
# with open("old/dare.json", "r", encoding="utf8") as tf:
#     data_old = json.load(tf)
#
#
# lk = 6
# mk = 110
# hk = 79
# index = 0
#
# with open("data_d.txt", "r", encoding="utf8") as f:
#     data_new = [q for q in f]
#
# def text():
#     global index, data_new
#     q = data_new[index]
#     return q
#
# def w():
#     with open(file="old/dare.json", mode="w", encoding="utf8") as wf:
#         json.dump(data_old, wf, ensure_ascii=False, indent=6)
#     l, m, h = len(data_old["low"]), len(data_old["middle"]), len(data_old["high"])
#     print(f"L={l}, M={m}, H={h}")
#     with open("data_d.txt", "w", encoding="utf8") as ttxt:
#         for item in data_new:
#             ttxt.write(item)
#     print(f"remain: {len(data_new)}")
#
#
# def l1():
#     global lk
#     data_old["low"][len(data_old["low"]) + 1] = text()
#     lk += 1
#     data_new.remove(text())
#     w()
#     next_text()
#
# def m1():
#     global mk
#     data_old["middle"][len(data_old["middle"]) + 1] = text()
#     mk += 1
#     data_new.remove(text())
#     w()
#     next_text()
#
# def h1():
#     global hk
#     data_old["high"][len(data_old["high"]) + 1] = text()
#     hk += 1
#     data_new.remove(text())
#     w()
#     next_text()
#
#
# window = tk.Tk()
#
# window.title("Расфасовка")
# window.minsize(400, 100)
# window.config(padx=50, pady=50)
#
# text_ = tk.Label(text=text())
#
# def next_text():
#     global index, data_new
#     index += 1
#     text_.config(text=text())
#
#
# low_button = tk.Button(text="Общие", command=l1)
# middle_button = tk.Button(text="Узнать лучше", command=m1)
# high_button = tk.Button(text="Личные", command=h1)
#
# text_.grid(column=1, row=0)
# low_button.grid(column=0, row=1)
# middle_button.grid(column=1, row=1)
# high_button.grid(column=2, row=1)
#
# tk.mainloop()

"d"
# with open("database/truth.json", "r", encoding="utf8") as ft:
#     data = json.load(ft)
#     lt = [v for k, v in data["low"].items()]
#     mt = [v for k, v in data["middle"].items()]
#     ht = [v for k, v in data["high"].items()]
#
# with open("database/dare.json", "r", encoding="utf8") as fd:
#     data = json.load(fd)
#     ld = [v for k, v in data["low"].items()]
#     md = [v for k, v in data["middle"].items()]
#     hd = [v for k, v in data["high"].items()]
#
# with open("database/truth.json", "w", encoding="utf8") as ftw:
#     data = {"low": {}, "middle": {}, "high": {}}
#     lk = 1
#     mk = 1
#     hk = 1
#     for item1 in lt:
#         i1 = item1.replace("❓ ", "")
#         i2 = i1.replace("\n", "")
#         data["low"][lk] = i2
#         lk += 1
#     for item2 in mt:
#         i1 = item2.replace("❓ ", "")
#         i2 = i1.replace("\n", "")
#         data["middle"][mk] = i2
#         mk += 1
#     for item3 in ht:
#         i1 = item3.replace("❓ ", "")
#         i2 = i1.replace("\n", "")
#         data["high"][hk] = i2
#         hk += 1
#     json.dump(data, ftw, ensure_ascii=False, indent=6)
#
# with open("database/dare.json", "w", encoding="utf8") as ftd:
#     data = {"low": {}, "middle": {}, "high": {}}
#     lkd = 1
#     mkd = 1
#     hkd = 1
#     for item1 in ld:
#         i1 = item1.replace("❗️", "")
#         i2 = i1.replace("\n", "")
#         data["low"][lkd] = i2
#         lkd += 1
#     for item2 in md:
#         i1 = item2.replace("❗️", "")
#         i2 = i1.replace("\n", "")
#         data["middle"][mkd] = i2
#         mkd += 1
#     for item3 in hd:
#         i1 = item3.replace("❗️", "")
#         i2 = i1.replace("\n", "")
#         data["high"][hkd] = i2
#         hkd += 1
#     json.dump(data, ftd, ensure_ascii=False, indent=6)

"""w"""
# with open("database/never.txt", "r", encoding="utf8") as f:
#     data_old = [q for q in f]
#     data_new = []
#     for q in data_old:
#         if q == "\n":
#             pass
#         else:
#             n = ''.join([i for i in q if not i.isdigit()])
#             n1 = n.replace(" ", "", 0)
#             n2 = n1.replace("\n", "")
#             n3 = n2.replace(". ", "")
#             data_new.append(n3)
#
# with open("database/never_cleared.txt", "w", encoding="utf8") as f1:
#     for q in list(dict.fromkeys(data_new)):
#         f1.write(f"{q}\n")

"""n"""
# with open("database/never_cleared.txt", "r", encoding="utf8") as f:
#     data_raw = [n for n in f]
#
# with open("database/never.json", "r", encoding="utf8") as fo:
#     data_old = json.load(fo)
#
# index = 0
#
# def text():
#     global index, data_raw
#     q = data_raw[index]
#     return q
#
# def w():
#     with open(file="database/never_.json", mode="w", encoding="utf8") as wf:
#         json.dump(data_old, wf, ensure_ascii=False, indent=6)
#     l, m, h = len(data_old["low"]), len(data_old["middle"]), len(data_old["high"])
#     print(f"L={l}, M={m}, H={h}")
#     with open("database/never_cleared.txt", mode="w", encoding="utf8") as txt:
#         for item in data_raw:
#             txt.write(item)
#     print(f"Remain: {len(data_raw)}")
#
#
# def l1():
#     data_old["low"][len(data_old["low"]) + 1] = text()
#     data_raw.remove(text())
#     w()
#     next_text()
#
# def m1():
#     data_old["middle"][len(data_old["middle"]) + 1] = text()
#     data_raw.remove(text())
#     w()
#     next_text()
#
# def h1():
#     data_old["high"][len(data_old["high"]) + 1] = text()
#     data_raw.remove(text())
#     w()
#     next_text()
#
# def no():
#     data_raw.remove(text())
#     next_text()
#
#
# window = tk.Tk()
#
# window.title("Расфасовка")
# window.minsize(400, 100)
# window.config(padx=50, pady=50)
#
# text_ = tk.Label(text=text())
#
# def next_text():
#     global index, data_new
#     index += 1
#     text_.config(text=text())
#
#
# low_button = tk.Button(text="Общие", command=l1)
# middle_button = tk.Button(text="Узнать лучше", command=m1)
# high_button = tk.Button(text="Личные", command=h1)
# no_button = tk.Button(text="Пропустить", command=no)
#
# text_.grid(column=1, row=0)
# low_button.grid(column=0, row=1)
# middle_button.grid(column=1, row=1)
# high_button.grid(column=2, row=1)
# no_button.grid(column=1, row=2)
#
# tk.mainloop()

"""tdnew"""

# with open("database/dare.json", "r", encoding="utf8") as f:
#     do_json = json.load(f)
#     dol = []
#     for k, v in do_json["low"].items():
#         dol.append(v)
#     for k, v in do_json["middle"].items():
#         dol.append(v)
#     for k, v in do_json["high"].items():
#         dol.append(v)
#
# with open("database/all_d.txt", "w", encoding="utf8") as af:
#     for i in dol:
#         af.write(i)
#         af.write("\n")

with open("database/never_cleared.txt", "r", encoding="utf8") as af:
    dol = []
    for i in af:
        dol.append(i)

def remove_and_rewrite(i):
    dol.remove(i)
    with open("database/never_cleared.txt", "w", encoding="utf8") as aa:
        for item in dol:
            aa.write(item)

def get_length(a, b, c):
    return len(a), len(b), len(c)


with open("database/never.json", "r", encoding="utf8") as tr:
    new_data = json.load(tr)

def store():
    with open("database/never.json", "w", encoding="utf8") as tn:
        json.dump(new_data, tn, ensure_ascii=False, indent=6)

i = 0

while len(dol) >= 0:
    print("#" * 50)
    print("'1' for LIFESTYLE, '2' for ABSURD, '3' for RELATIONS, '4' for PERSONAL, '5' for ADULT, '6' to remove")
    a = input(f"\n{dol[i]}\n")
    r = dol[i]
    if a == "1":
        new_data["lifestyle"][len(new_data["lifestyle"]) + 1] = dol[i]
        remove_and_rewrite(r)
        store()
        print(f"Left: {len(dol)}")
        print(f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
              f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
        i += 1

    elif a == "2":
        new_data["absurd"][len(new_data["absurd"]) + 1] = dol[i]
        remove_and_rewrite(r)
        store()
        print(f"Left: {len(dol)}")
        print(
            f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
            f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
        i += 1
    elif a == "3":
        new_data["relations"][len(new_data["relations"]) + 1] = dol[i]
        remove_and_rewrite(r)
        store()
        print(f"Left: {len(dol)}")
        print(
            f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
            f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
        i += 1
    elif a == "4":
        new_data["personal"][len(new_data["personal"]) + 1] = dol[i]
        remove_and_rewrite(r)
        store()
        print(f"Left: {len(dol)}")
        print(
            f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
            f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
        i += 1
    elif a == "5":
        new_data["adult"][len(new_data["adult"]) + 1] = dol[i]
        remove_and_rewrite(r)
        store()
        print(f"Left: {len(dol)}")
        print(
            f'Current: L: {len(new_data["lifestyle"])}, A: {len(new_data["absurd"])}, R: {len(new_data["relations"])},'
            f' P: {len(new_data["personal"])}, Ad: {len(new_data["adult"])}')
        i += 1
    elif a == "6":
        remove_and_rewrite(r)
        store()
        i += 1





























