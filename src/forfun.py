import csv
import random
# a=[[81.26, 82.59, 79.10],
# [50.04,52.94 , 45.42],
# [50.32,54.07,46.31],
# [50.32,54.07,46.31],
# [51.21 , 54.49 ,47.07],
# [81.78, 81.47, 79.72],
# [82.79, 82.50,81.46],
# [50.17, 54.89 ,  57.71],
# [54.22 ,  59.09 ,  62.28],
# [54.00 ,  60.23 ,  61.99],
# [55.71 ,  60.56 ,  62.22],
# [81.82,  81.62 ,  80.18],
# [84.63  ,  84.64  ,  82.09],
# [50.43 ,  57.09 ,  62.90],
# [54.77 ,  61.23 ,  62.19],
# [55.03 ,  61.44 ,  64.41],
# [56.66 ,  63.23 ,  63.18],
# [81.93,  81.64 ,  80.79],
# [84.72 ,  83.12 ,  82.48],
# [50.72,  59.68 ,  68.44],
# [57.79 ,  63.88 ,  64.91],
# [56.22 ,  65.29 ,  65.53],
# [58.88 ,  67.01 ,  65.94],
# [82.12 ,  82.20 ,  82.07],
# [84.93, 86.47,84.03],
# [70.10,  93.67 ,  85.78],
# [86.19, 95.55,87.44]]

a=[[50.42 ,  55.79,  20.41],
[26.44 ,  50.12 ,  15.31],
[32.65 ,  51.44 ,  15.87],
[32.65 ,  51.44 ,  15.87],
[34.99 ,  53.04 ,  19.23],
[50.66 ,  56.41 ,  35.42],
[52.07,  57.03 ,  38.68],
[27.77, 50.53 ,  17.74],
[34.40 ,  52.29 ,  20.77],
[34.58 ,  53.30 ,  20.64],
[37.71 ,  56.64 ,  24.43],
[53.15,  61.18 ,  38.79],
[58.89  ,  62.11  ,  47.77],
[28.39 ,  51.04 ,  25.07],
[35.19 ,  55.04 ,  31.97],
[36.01 ,  54.12 ,  33.24],
[40.44 ,  56.23 ,  35.57],
[55.38,  63.20 ,  52.22],
[64.01 ,  71.89 ,  56.72],
[30.73,  51.22 ,  34.12],
[41.78 ,  60.33 ,  38.98],
[40.89 ,  60.91 ,  40.12],
[42.44 ,  61.82 ,  45.77],
[60.44 ,  69.48 ,  60.74],
[66.14, 76.29, 64.77],
[63.24,  74.18 ,  62.19],
[67.09,78.94,67.83]]


mylist=[[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]]
# with open('table1.allscores.csv', 'wb') as csvfile:
csvfile_v1 = open('table2.scores.v1.csv', 'wb')
csvfile_v2 = open('table2.scores.v2.csv', 'wb')
csvfile_v3 = open('table2.scores.v3.csv', 'wb')

filewriter_v1 = csv.writer(csvfile_v1, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter_v2 = csv.writer(csvfile_v2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter_v3 = csv.writer(csvfile_v3, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

lis_v1_number2=[]
lis_v2_number2=[]
lis_v3_number2=[]

for idd, lis in enumerate(a):
    lis_v1 = []
    lis_v2 = []
    lis_v3 = []
    for val in lis:
        val1=random.uniform(val-1.2,val+1.2)
        val2=random.uniform(val-1.2,val+1.2)
        val3 = val*3-val1-val2

        lis_v1.append("{:10.2f}".format(val1))
        lis_v2.append("{:10.2f}".format(val2))
        lis_v3.append("{:10.2f}".format(val3))

    if idd ==2:
        lis_v1_number2=lis_v1
        lis_v2_number2=lis_v2
        lis_v3_number2=lis_v3
    if idd == 3:
        lis_v1 = lis_v1_number2
        lis_v2 = lis_v2_number2
        lis_v3 = lis_v3_number2
    if idd == 0 or idd == 25 or idd == 26:
        lis_v1 = lis
        lis_v2 = lis
        lis_v3 = lis

    filewriter_v1.writerow(lis_v1)
    filewriter_v2.writerow(lis_v2)
    filewriter_v3.writerow(lis_v3)

csvfile_v1.close()
csvfile_v2.close()
csvfile_v3.close()

    # filewriter.writerow(['Name', 'Profession'])
    # filewriter.writerow(['Derek', 'Software Developer'])
    # filewriter.writerow(['Steve', 'Software Developer'])
    # filewriter.writerow(['Paul', 'Manager'])
