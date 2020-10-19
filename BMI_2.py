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
def ad_data(data_list) :
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

# 加入字典
def dictionary_s(data_list) :
    students_status = {}
    for line in data_list :
        name = line[0]
        status = line[4]
        students_status[name] = status
    return students_status

def dictionary_B(data_list) :
    students_BMI = {}
    for line in data_list :
        name = line[0]
        BMI = line[3]
        students_BMI[name] = BMI
    return students_BMI

# 查尋學生狀況
def search(students_status,students_BMI) :
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

# 資料排序
def sort(data_list) :
    BMI_s = []
    Tall_s = []
    weight_s = []
    for d in data_list :
        name = d[0]
        tall = float(d[1])
        weight =float(d[2])
        BMI_n = float(d[3])
        BMI_s.append([name,BMI_n])
        Tall_s.append([name,tall])
        weight_s.append([name,weight])

    BMI_s.sort(key = lambda x:x[1])  # sort 用法
    Tall_s.sort(key = lambda x:x[1])
    weight_s.sort(key = lambda x:x[1])
    return BMI_s,Tall_s,weight_s  # 多回傳

# 圓餅圖
def matplotlib(data_list) :
    import os
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['MingLiU'] # 字型

    light = 0
    normal = 0
    over = 0
    fat = 0
    fat_n = 0
    fat_s = 0
    for d in data_list :
        status = d[4]
        if status == '過輕' :
            light += 1
        if status == '正常' :
            normal += 1
        if status == '過重' :
            over += 1
        if status == '輕度肥胖' :
            fat += 1
        if status == '中度肥胖' :
            fat_n += 1
        if status == '重度肥胖' :
            fat_s += 1
            
    light_p = round((100/len(data_list) * light),2)
    normal_p = round((100/len(data_list)*normal),2)
    over_p = round((100/len(data_list)*over),2)
    fat_p = round((100/len(data_list)*fat),2)
    fat_n_p = round((100/len(data_list)*fat_n),2)
    fat_s_p = round((100/len(data_list)*fat_s),2)

    labels = '過輕', '正常', '過重', '輕度肥胖', '中度肥胖', '重度肥胖'
    sizes = [light_p, normal_p, over_p, fat_p, fat_n_p, fat_s_p]
    explode = (0, 0, 0, 0, 0, 0) # 設置分離的距離，0表示不分離
    plt.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',
    shadow = True, startangle = 90)
    plt.axis('equal') # 畫出正圓形
    plt.savefig(os.path.join('result/', 'Pie chart.png'))
    plt.show() 

# 主程式
def main() :
    data_list = r_f('students_BMI.csv')
    data_list = ad_data(data_list)
    w_f('students_BMI.csv', data_list)
    students_status = dictionary_s(data_list)
    students_BMI = dictionary_B(data_list)
    search(students_status,students_BMI)
    # 定位(有多回傳值)
    BMI_s = sort(data_list)[0]
    Tall_s = sort(data_list)[1]
    weight_s = sort(data_list)[2]
    matplotlib(data_list)

main()
