# 这里编写你的代码
num=input("请输入一个5位数字：")
if len(num)!=5 or not num.isdigit():
    print("错误：请输入一个5位数字")
else:
    # 判断是否为回文数
    if num==num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
   
