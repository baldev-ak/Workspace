if __name__ == '__main__':
    n = int(input())
    
    result = 0
        
    for i in range(1,n+1):
        if i <= 9: 
            result = result *10 + i
        elif i>9 and i<99 :
            result = result * 100 + i
        elif i>99 and i < 150:
            result = result *1000 + i
    print(result)