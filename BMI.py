print('歡迎來到BMI計算機')

high = float(input('請輸入身高:' ))
weight = float(input('請輸入體重:' ))
BMI = weight / (pow ( high / 100, 2) ) # 可以這樣寫

print('您BMI值為', BMI)

if BMI >= 35 :
    print('重度肥胖')
    if BMI >= 38 :
        print('非常危險')
elif BMI >= 30 :
    print('中度肥胖')
elif BMI >= 27 :
    print('輕度肥胖')
elif BMI >= 24 :
    print('過重')
elif BMI >= 18.5 :
    print('正常')
else :
    print('過輕')
    if BMI <= 15 :
        print('請看醫生')
