# 讀取
def r_f(f_n) :
    data_list = []
    import os
    if os.path.isfile(f_n) :
        with open (f_n , 'r' , encoding = 'utf-8-sig') as f :
            for line in f :
                if '姓名' in line :
                    continue
                name, high , weight, BMI, status = line.strip().split(',')
                data_list.append([name, high, weight, BMI, status])
    else :
        print('找不到檔案')
        data_list = []
    return data_list

# 增加數據
def ad_data() :
    while True :
        answer = input('是否要再增加學生數據y/n: ')
        if answer == 'y' :
            name = input('請輸入名子: ')
            high = float(input('請輸入身高: '))
            weight = float(input('請輸入體種: '))
            BMI = round(weight / (pow ( high / 100, 2) ), 3) # round(a, 3) 取小數點到3位
            if BMI >= 35 :
                status = '重度肥胖'
            elif BMI >= 30 :
                status = '中度肥胖'
            elif BMI >= 27 :
                status = '輕度肥胖'
            elif BMI >= 24 :
                status = '過重'
            elif BMI >= 18.5 :
                status = '正常'
            else :
                status = '過輕'
            data_list.append([name, high, weight, BMI, status])
        elif answer == 'n' :
            break
        else :
            print('請輸入 y 或 n') 
    return data_list

# 寫入檔案
def w_f(f_n, data_list) :
    with open(f_n, 'w', encoding = 'utf-8') as f :
        f.write('姓名,身高,體重,BMI,狀態\n')
        for line in data_list :
            if '姓名, 身高, 體重, BMI, 狀況' in line :
                continue
            name = line[0]
            high = line[1]
            weight = line[2]
            BMI = line[3]
            status = line[4]
            f.write(name + ',' + str(high) + ',' + str(weight) + ',' + str(BMI) + ',' + status + '\n')

data_list = r_f('students_BMI.csv')
data_list = ad_data()
w_f('students_BMI.csv', data_list)


# 加入字典
students_status = {}
for line in data_list :
    name = line[0]
    status = line[4]
    students_status[name] = status
 
students_BMI = {}
for line in data_list :
    name = line[0]
    BMI = line[3]
    students_BMI[name] = BMI

# 查尋學生狀況
def search() :
    while True :
        print('離開查詢功能按 q ')
        name = input('請輸入學生名: ')
        if name in students_status : 
            students_message = [students_BMI[name], students_status[name]]
            print(name, 'BMI值為', students_message[0], '狀況:', students_message[1])
        elif name == 'q' :
            break
        else :
            print('查無此人')

search()