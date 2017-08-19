'''
message = input("Enter a message to endcode or decode:\n")
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + 15
        letter = chr(value)
        if not letter.isupper():
            value -= 30
            letter = chr(value)
    output += letter
print("Mom will see",output)
#upper   ex:"Taiwan".upper()   TAIWAN
#lower   ex:"Taiwan".lower()   taiwan
#ord("A")    65   ("A"的十進制值)
#chr(65)     A    (65代表的字)


#查ASCII Table
'''
'''

#做出下面級數(不是功課)
1+2+3+4+5 + 10+11+12+13 + 20+21+22
#方法一，最簡單的方法
  #sum = 1+2+3+4+5+10+11+12+13+20+21+22
  #print(sum)
#方法二，限定用迴圈完成
sum = 0
for x in range(1,6):
    sum += x
for y in range(10,14):
    sum += y
for z in range(20,23):
    sum += z
print(sum,"完成囉")
'''
#方法三'四(迴圈)
#方法五，函式
'''
<方法二>的時候，用了3個迴圈做同樣的事情，現在要用函數簡化程式碼
  def sumfunction(start,end):
1.^^^ 定義函數 syntax (語法)
2.sumfunction 函數名稱            
3.start,end傳入的參數
4.return xxxx 回傳xxxx的值
'''
#定義函數的第一個方式，有回傳值
def sumfunction(start_value,end_value):
    sum1 = 0
    for loopcount in range(start_value,end_value):
        sum1 += loopcount
    return sum1
sum_end = sumfunction(1,6)
sum_end = sum_end + sumfunction(10,14)
sum_end = sum_end + sumfunction(20,23)
print(sum_end) # Debugger到這時候請用OVER，其他使用STEP看程式碼 



def main():
    c = 5 + 5
    print(c)
main()         #所有的程式碼都會有入口點， main()函數

#github python_algorithm


















