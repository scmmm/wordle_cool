import pandas as pd
from pandas import  Series,DataFrame
path = 'C:\\Users\\mmmzx\\Desktop\\mmmtorch\\guess_world'

allchar = []

charcorrect = []
charhalf = []
charban = []
banned = [[]]
tmpstr = []

def checkword(s,looker):
    n = len(s)
    ans = 0
    for i in range(0,n) :
        if(s[i]==looker)  :
            ans=ans+1
    return ans

def checklen(s):
    n = len(s)
    return n

df = pd.read_csv(path+'\\word.csv')

#测定是否存在每一个字母，得到每一个字母的个数
# 先转化为string
df['word']=df['word'].apply(str)
for i in range(0,26)    :
    df['have'+chr(ord('a')+i)]=df['word'].apply(checkword,args=(chr(ord('a')+i)))
#得到每一个单词的长度
df['len']=df['word'].apply(checklen)

# 按照长度和字典序排序
df=df.sort_values(by=['len','word'])

df.to_csv(path+'\\test.csv',index=False,sep=',')

def valid_ban(word):
    count = 0
    for i in range(len(word)) :
        if(banned[i].count(word[i])) :
            count=count+1
            continue
    for i in range(len(word)):
        if(charban.count(word[i])) :
            count=count+1
            continue
    return count

def valid_correct(word):
    count = 0
    for i in range (len(charcorrect)) :
        tmp = len(charcorrect[i])
        tmpchar = charcorrect[i][tmp-1]
        tmpplace= int(charcorrect[i][0:tmp-1])
        if(word[tmpplace]==tmpchar) :
            count =count+1
    return count

def valid_guess(word):
    count = 0
    for i in range(len(word)) :
        if(charhalf.count(word[i])) :
            count=count+1
            continue
    return count

def valid_advice(word):
    count = 0
    for i in range(len(word)) :
        if(allchar.count(word[i])) :
            count=count+1
            continue
    return count

# 现在猜单词
def init():
    for i in range (0,26):
        allchar.append(chr(ord('a')+i))


def guess_word() :
    size = 0 
    for i in range(len(charban)):
        if(allchar.count(charban[i])):
            for j in range (allchar.count(charban[i])):
                allchar.remove(charban[i])
    for i in range(len(charhalf)):
        if(allchar.count(charhalf[i])):
            for j in range (allchar.count(charhalf[i])):
                allchar.remove(charhalf[i])
    # 当前确定的位置
    # 否则，尽量猜单词
    # 但是可能有猜不到的情况
    # 干脆看每个单词的匹配度
    # 定义匹配度 = 之前没查过的字母个数*2 - 冲突字母数字
    
    for row in df.itertuples():
        if(getattr(row, 'len')==length) :
            tmpword = getattr(row,'word')
            baspoint = 0
            baspoint = baspoint - valid_ban(tmpword)
            baspoint = baspoint + valid_guess(tmpword)*2
            baspoint = baspoint + valid_correct(tmpword)*5
            global tmpstr
            tmpstr.append([tmpword,baspoint])
            size = size+1

    tmpstr= sorted(tmpstr,key=(lambda x:x[1]),reverse=True)
    for i in range (min(size,30)) :
        print(tmpstr[i])



def advice_word() :
    # 直接遍历
    # 先把没有猜的数字猜一遍
    size = 0 
    for i in range(len(charban)):
        if(allchar.count(charban[i])):
            for j in range (allchar.count(charban[i])):
                allchar.remove(charban[i])
    for i in range(len(charhalf)):
        if(allchar.count(charhalf[i])):
            for j in range (allchar.count(charhalf[i])):
                allchar.remove(charhalf[i])
    # 当前确定的位置
    nowmust = len(charcorrect)
    nowcan = len(allchar)
    # 如果nowmust+nowcan 低于单词长度，那么就通过half里面的来凑
    # 否则，尽量猜单词
    # 但是可能有猜不到的情况
    # 干脆看每个单词的匹配度
    # 定义匹配度 = 之前没查过的字母个数*2 - 冲突字母数字
    
    for row in df.itertuples():
        if(getattr(row, 'len')==length) :
            tmpword = getattr(row,'word')
            baspoint = 0
            baspoint = baspoint - valid_ban(tmpword)
            baspoint = baspoint + valid_advice(tmpword)*2
            global tmpstr
            tmpstr.append([tmpword,baspoint])
            size = size+1

    tmpstr= sorted(tmpstr,key=(lambda x:x[1]),reverse=True)
    for i in range (min(size,30)) :
        print(tmpstr[i])


while(1):
    print('0 : 直接输入已经猜过的单词\n 1: 从头开始猜单词 \n2:结束当前轮猜单词')
    a = int(input())
    if(a == 0) :
        # 暂时还没做
        print()
    
    elif(a == 1) :
        # 首先输入单词长度
        length = int(input())
        banned = [[] for i in range (length+1)]
        init()
        while(1):
            # 输入合法单词序列
            # 例如对于abcdefgh,其中c，d位置正确，b存在字母但不是这个位置，其他不存在
            # 则输入两行
            # abcdefg
            # 0122000
            wordtest = str(input())
            if(wordtest=='-1'):
                break
            wordvalid = str(input())
            for i in range (0,length):
                if (wordvalid[i]=='2') :
                    charcorrect.append(str(i)+wordtest[i])
                    charhalf.append(wordtest[i])
                elif (wordvalid[i]=='1'):
                    charhalf.append(wordtest[i])
                    banned[i].append(wordtest[i])
                else :
                    charban.append(wordtest[i])
            for i in range(len(charban)):
                if(charhalf.count(charban[i])):
                    for j in range (charhalf.count(charban[i])):
                        charhalf.remove(charban[i])
            tmpstr=[]
            print('当前建议猜测的单词')
            advice_word()
            tmpstr=[]
            printf('当前可能的单词')
            guess_word()
    elif (a==2):
        break
    else :
        print('不合法输入\n')