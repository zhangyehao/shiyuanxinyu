#  Title  : 0912_ssr_location_segmentation
#  Author : YeHao Zhang
#  Email  : 3074675457@qq.com
#  Time   : 2023/9/12 12:09
import pandas as pd
import time
import gc
# 读取GFF文件
Bmus_gff = pd.read_csv("F:/dachuang/newwork/gff/Cetacea/genomic.gff", sep='\t', comment='#', header=None, names=["chromosome", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
# print(Bmus_gff.iat[0, 0])
chromosome = {"NC_045785.1": "1", "NC_045786.1": "2", "NC_045787.1": "3", "NC_045788.1": "4", "NC_045789.1": "5", "NC_045790.1": "6", "NC_045791.1": "7", "NC_045792.1": "8", "NC_045793.1": "9", "NC_045794.1": "10", "NC_045795.1": "11", "NC_045796.1": "12", "NC_045797.1": "13", "NC_045798.1": "14", "NC_045799.1": "15", "NC_045800.1": "16", "NC_045801.1": "17", "NC_045802.1": "18", "NC_045803.1": "19", "NC_045804.1": "20", "NC_045805.1": "21", "NC_045806.1": "X", "NC_045807.1": "Y", "NW": "NOT SURE", "NC_001601.1": "MT"}
for i in range(len(Bmus_gff)):
    if Bmus_gff.iat[i, 0][:2] == "NW":
        Bmus_gff.iat[i, 0] = chromosome[Bmus_gff.iat[i, 0][:2]]
    else:
        Bmus_gff.iat[i, 0] = chromosome[Bmus_gff.iat[i, 0]]
# print(Bmus_gff.head())
# 读目标基因文件（由0910_locate_gene生成）
Bmus_target_gene = pd.read_csv("F:/dachuang/newwork/gff/Cetacea/Cetacea_target_gene.csv")

for i in range(len(Bmus_target_gene)-2):
    k = 1
    if Bmus_target_gene.iat[i, 0] == "5":
        gene_index = Bmus_gff[(Bmus_gff["chromosome"] == Bmus_target_gene.iat[i, 1]) & (Bmus_gff["start"] == Bmus_target_gene.iat[i, 5])].index.tolist()[0]
        ssr_light = Bmus_target_gene.iat[i + 1, 5]
        ssr_right = Bmus_target_gene.iat[i + 1, 6]
        while k:
            if Bmus_gff.iat[gene_index + k, 2] == "exon":
                gene_exon_light = Bmus_gff.iat[gene_index + k, 3]
                gene_exon_right = Bmus_gff.iat[gene_index + k, 4]
                if gene_exon_right >= ssr_right and ssr_light >= gene_exon_light:
                    Bmus_target_gene.iat[i + 1, 0] = "exon"
                else:
                    pass

            if Bmus_gff.iat[gene_index + k, 2] == "gene":
                k = 0
            else:
                k += 1
    gc.collect()
    print("已完成", i + 3, "/", len(Bmus_target_gene))

Bmus_target_gene.to_csv("F:/dachuang/newwork/gff/Cetacea/Cetacea_target_gene_location_segmentation_{}.csv".format(time.strftime("%Y%m%d%H%M%S", time.localtime())), index=False, header=["location status", "chromosome", "sequence", "type-1/type", "type-2/repeat", "start", "end", "chain/ID", "content-1/motif", "content-2/group", "content-3/access", "content-4/query acc.ver", "content-5", "content-6", "content-7", "content-8", "content-9"])

print("恭喜！写入完成！")
