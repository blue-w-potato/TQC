def main():
    a = input()
    eight(a)

# 字數是否 >= 8
def eight(a):
    
    if len(a) >= 8:
        
        upper_letter(a)
            
    else:
        print('Invalid password')

# 檢查 a 當中是否存在大寫英文
def upper_letter(a):
    
    for i in a:
            
        if ord(i)<ord('A') or ord(i)>ord('Z'):
            
            letter_and_number(a)
            break
        
    else:
        print('Invalid password')

# 檢查是否滿足 a 當中只有英文字母和數字
def letter_and_number(a):
    
    # x 代表 a 當中存在數字
    # y 代表存在英文字母
    x,y = False,False
    
    for i in a.upper():# 只是要檢查是否存在字母，所以全部用大寫來檢查
        n = ord(i) 
        
        if ord('0')<=n<=ord('9'):# 0~9
            x = True
        elif ord('A')<=n<=ord('Z'):# A~Z
            y = True
        else: # 如果不是數字或字母，不進入下一個階段
            print('Invalid passward')
            break
        
    else:# 沒有不是字母也不是數字的字元
        
        if x and y:# 有字母也有數字
            print('Valid password')
        else:
            print('Invalid password')

if __name__ == '__main__':
    main()