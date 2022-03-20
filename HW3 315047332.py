#C:\\Users\\User\\Desktop\\שיעורים\\מבוא להנדסת ידע ונתונים\\ex3_text.txt
#A
import os.path
lst = []
def read_line(n,file):
    if (type(n) == int) and os.path.exists(file):
        text = open(file)
        for l in text:
            lst.append(l)
        if n <= len(lst):
            return lst[n - 1]
        else:
            return "line" ,n ,"doesn't exist"
    elif type(n) != int:
        return ("invalid input detected")
    else:
        return ("file not found")
                         
print(read_line(13,"C:\\Users\\User\\Desktop\\שיעורים\\מבוא להנדסת ידע ונתונים\\ex3_text.txt"))        
            
#%%
#B
import os.path
lst = []
lst1 = []
lst2 = []
num = 0
def longest_words(file):
    global num,lst,lst1
    if os.path.exists(file):
        text = open(file)
        for line in text:
            if num > 1:
                words = line.split()
                for word in words:
                   lst.append(word)
            else:
                num += 1
        for word in lst:
            words = word.split('.')
            for i in words:
                lst1.append(i)
        lst1 = sorted(lst1,key = len, reverse=True)
        return lst1[:5]
    else:
        return "file not found"

print(longest_words("C:\\Users\\User\\Desktop\\שיעורים\\מבוא להנדסת ידע ונתונים\\ex3_text.txt"))
                    
                    
                    
                    
                    
                    
                    
                    