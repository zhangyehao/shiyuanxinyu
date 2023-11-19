#  Title  : 0910_locate_gene
#  Author : YeHao Zhang
#  Email  : 3074675457@qq.com
#  Time   : 2023/9/10 14:44
import csv
import gc
from win32com import client
import pandas as pd


# 读取CSV表格为列表
# csv列表[0]为列名
def read_csv(file_name):
    f = open(file_name, 'r')
    csvreader = csv.reader(f)
    final_list = list(csvreader)
    return final_list


target_ssr = read_csv("E:/dachuang/newwork/gff/Cetacea/Bmus_SSR.csv")
# print(type(target_ssr[1][0])) == str

target_gene = read_csv("E:/dachuang/newwork/gff/Cetacea/Bmus_Gene.csv")
# print(target_gene[:10])
ans = [["location status", "chromosome", "sequence", "type-1/type", "type-2/repeat", "start", "end", "chain/ID", "content-1/motif", "content-2/group", "content-3/access", "content-4/query acc.ver", "content-5", "content-6", "content-7", "content-8"]]

for i in range(1, len(target_ssr)):
    for j in range(1, len(target_gene)):
        if target_ssr[i][0] == target_gene[j][0]:
            l1 = eval(target_ssr[i][4]) - eval(target_gene[j][4])
            l2 = eval(target_ssr[i][5]) - eval(target_gene[j][4])
            r1 = eval(target_ssr[i][4]) - eval(target_gene[j][5])
            r2 = eval(target_ssr[i][5]) - eval(target_gene[j][5])

            if l1 < 0 and l2 < 0 and r1 < 0 and r2 < 0 and abs(l2) < 5000:
                ans.append(["left", ]+target_ssr[i])
                ans.append(list("1")+target_gene[j])
                ans.append(list("_"))

            if l1 > 0 and l2 > 0 and r1 > 0 and r2 > 0 and abs(r1) < 5000:
                ans.append(list("2") + target_gene[j])
                ans.append(["right", ] + target_ssr[i])
                ans.append(list("_"))

            if l1 < 0 < l2 and r1 < 0 and r2 < 0:
                ans.append(["reduplication", ] + target_ssr[i])
                ans.append(list("3") + target_gene[j])
                ans.append(list("_"))

            if l1 > 0 > r1 and l2 > 0 and r2 > 0:
                ans.append(list("4") + target_gene[j])
                ans.append(["reduplication", ] + target_ssr[i])
                ans.append(list("_"))

            if l1 > 0 > r1 and l2 > 0 > r2:
                ans.append(list("5") + target_gene[j])
                ans.append(["inside", ] + target_ssr[i])
                ans.append(list("_"))

            if l1 < 0 < l2 and r1 < 0 < r2:
                ans.append(["inside", ] + target_ssr[i])
                ans.append(list("6") + target_gene[j])
                ans.append(list("_"))

    gc.collect()
    print("已完成", i, "/", len(target_ssr)-1)

ans_df = pd.DataFrame(ans)
ans_df.to_csv("E:/dachuang/newwork/gff/target_gene.csv", index=False, header=False)

print("恭喜！写入完成！")
