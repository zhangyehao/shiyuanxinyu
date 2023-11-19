#  Title  : 0911_orthologus
#  Author : YeHao Zhang
#  Email  : 3074675457@qq.com
#  Time   : 2023/9/11 16:39
import pandas as pd
import time
import gc

data = pd.read_csv("E:/dachuang/newwork/Cetacea_filter_target_ssr_sites.csv")
# print(data.iat[0, 0])
ans = []
part_ans = ["query acc.ver", "Mmon", "Psin", "Bmus", "Ttru", "Mden", "Nasi", "Kbre", "Erob", "Bric", "Egla", "Oorc", "Hamp", "status"]
same_element = "query acc.ver"
for i in range(len(data)):
    if same_element != data.iat[i, 2]:
        same_element = data.iat[i, 2]
        # if part_ans[1] == 1 and part_ans[2] == 1 and part_ans[3] == 1 and part_ans[4] == 1 and part_ans[5] == 1 and part_ans[6] == 1 and part_ans[7] == 1 and part_ans[8] == 1 and part_ans[9] == 1 and part_ans[10] == 1 and part_ans[11] == 1 and part_ans[12] == 1:
        # 效果不理想，只筛出1个SSR
        # 关键步
        if part_ans.count(1) >= 8:
            part_ans[13] = 1
        ans.append(part_ans)
        part_ans = [same_element, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if data.iat[i, 24] == "GCA_005190385.3":
        part_ans[1] += 1
    elif data.iat[i, 24] == "GCA_008692025.1":
        part_ans[2] += 1
    elif data.iat[i, 24] == "GCA_009873245.3":
        part_ans[3] += 1
    elif data.iat[i, 24] == "GCA_011762595.1":
        part_ans[4] += 1
    elif data.iat[i, 24] == "GCA_025265405.1":
        part_ans[5] += 1
    elif data.iat[i, 24] == "GCA_026225855.1":
        part_ans[6] += 1
    elif data.iat[i, 24] == "GCA_026419965.1":
        part_ans[7] += 1
    elif data.iat[i, 24] == "GCA_028021215.1":
        part_ans[8] += 1
    elif data.iat[i, 24] == "GCA_028023285.1":
        part_ans[9] += 1
    elif data.iat[i, 24] == "GCA_028564815.1":
        part_ans[10] += 1
    elif data.iat[i, 24] == "GCA_937001465.1":
        part_ans[11] += 1
    elif data.iat[i, 24] == "GCA_949752795.1":
        part_ans[12] += 1
    else:
        part_ans[0] = "异常"

    if i % 30000 == 0:
        gc.collect()
        print("已完成{:2f}%".format((i+1)*100/len(data)))

ans_df = pd.DataFrame(ans)
ans_df.to_csv("E:/dachuang/newwork/gff/Cetacea_orthologus_result_{}.csv".format(time.strftime("%Y%m%d%H%M%S", time.localtime())), index=False, header=False)

