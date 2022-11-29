import numpy as np
# 生成数据集，共九种组合
num_jobs_list = [10, 20, 30]
num_machines_list = [4, 6, 8]


for num_jobs in num_jobs_list:
    for num_machines in num_machines_list:
        with open("./dataset/{}-{}.txt".format(num_jobs, num_machines), "w") as f:
            # 写入工件数和机器数
            lines = ["{} {}\n".format(num_jobs, num_machines)]
            for i in range(num_jobs):
                line = ""
                for j in range(num_machines):
                    line += " " + " "  # 写入工件对应机器的耗时，随机生成
                lines.append(line+"\n")
            f.writelines(lines)
