import numpy as np
num_jobs_list = [100, 200, 300]
num_machines_list = [2, 3, 4]
for num_jobs in num_jobs_list:
    for num_machines in num_machines_list:
        with open("./dataset/{}-{}.txt".format(num_jobs, num_machines), "w") as f:
            lines = ["{} {}\n".format(num_jobs, num_machines)]
            for i in range(num_jobs):
                line = ""
                for j in range(num_machines):
                    line += " " + " "  
                lines.append(line+"\n")
            f.writelines(lines)
