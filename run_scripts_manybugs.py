import os

method_list = [
    # "pearson",
    # "spearman",
    # "kendall",
    # "chisquare",
    # "mutual_information",
    # "fisher_score",
    #"dstar",
    #"ochiai",
    #"barinel",
    # "ER1",
    # "ER5",
    # "GP02",
    # "GP03",
    # "GP19",
    # "Op2"
    "MLP-FL",
    "CNN-FL",
    "RNN-FL"
]

program_list = [
    "gzip-bug-2009-08-16-3fe0caeada-39a362ae9d",
     "gzip-bug-2009-09-26-a1d3d4019d-f17cbd13a1",
     "gzip-bug-2009-10-09-1a085b1446-118a107f2d",
     "gzip-bug-2010-01-30-fc00329e3d-1204630c96",
     "gzip-bug-2010-02-19-3eb6091d69-884ef6d16c",
    "libtiff-bug-2009-02-05-764dbba-2e42d63",
     "libtiff-bug-2009-06-30-b44af47-e0b51f3",
     "libtiff-bug-2009-08-28-e8a47d4-023b6df",
     "libtiff-bug-2009-09-03-6406250-6b6496b",
#    "libtiff-bug-2010-06-30-1563270-1136bdf",
#     "libtiff-bug-2010-11-27-eb326f9-eec7ec0",
     "libtiff-bug-2010-12-13-96a5fb4-bdba15c",
     "python-bug-69783-69784",
     "python-bug-69831-69833",
     "python-bug-69934-69935",
     "python-bug-70056-70059",
]

#program_list=["artificial_bug"]

program_list = [ "v3","v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11", "v12", "v13", "v14", "v15", "v16", "v17", "v18",
         "v19", "v20", "v21", "v22", "v23", "v24", "v25", "v26", "v28", "v29", "v30", "v31", "v32", "v33", "v35",
        "v36", "v37", "v38"]


method_para = ""
for method in method_list[:-1]:
    method_para += method + ","
method_para += method_list[-1]
#cp(python)=[0.5, 0.5, 0.15, 0.65, 0.1,	0.65, 0.5,	0.5, 0.5,# 1, 1,
#      0.5, 0.5,0.01, 0.01, 0.01]
cp=[0.1, 0.5, 0.5, 0.5, 0.55, 0.6, 0.55, 0.5, 0.1, 0.9,
    0.5, 0.75, 0.95, 0.1, 0.5, 0.9, 0.9, 0.8, 0.8, 0.8,
    0.1, 0.5, 0.1, 0.1, 0.1, 0.55, 0.5, 0.95, 0.1, 0.1,
    0.1, 0.1, 0.5, 0.6]
#cp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
i=1
for program in program_list:
    print(program,i)
    command = f"/opt/anaconda3/bin/python3.9 run.py -d SIR -p {program} -i any -m {method_para} -e lda_smote -ep {cp[i-1]} -cp {cp[i-1]}"
    i+=1
    os.system(command)
#for program in program_list:
#    print(program,i)
#    command = f"/opt/anaconda3/bin/python3.9 run.py -d SIR -p {program} -i any -m {method_para} -e lda_smote -ep {cp[i-1]} -cp {cp[i-1]}"
#    #command = f"/opt/anaconda3/bin/python3.9 run.py -d motivation -p {program} -i any -m {method_para} -e origin"
#    i+=1
#    os.system(command)

