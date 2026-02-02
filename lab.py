#201
#year = int(input())

#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print("YES")
#else:
#    print("NO")



#202
##Sum
#a=int(input())
#b=0
#while a>0:
#    b+=a
#    a-=1
#print(b)



#203
#a=int(input())
#numbers=list(map(int, input().split())) 
#print(sum(numbers)) #через функцию sum суммируем массив



#204
#a=int(input())
#number=list(map(int, input().split()))

#total=0
#for i in number:
#    if i>0:
#        total+=1
#    else:
#        continue        
#print(total)



#205
#a=int(input())

#pow=1
#while pow<a:
#    pow*=2
#if pow==a:
#    print('YES')
#else:
#    print("NO")



#206
#a=int(input())
#numbers=list(map(int, input().split()))
#print(max(numbers))



#207
#a=int(input())
#number=list(map(int, input().split()))
#pos=number.index(max(number))
#print(pos+1)




#208
#a=int(input())
#pow=1
#while pow<=a:
#    print(pow, end=" ")
#    pow*=2




#209
#a=int(input())
#number=list(map(int, input().split()))

#max=max(number)
#min=min(number)
#for i in range(a):
#    if number[i]==max:
#        number[i]=min
#for i in range(a):
#    print(number[i], end=" ")



#210
#a=int(input())

#list=list(map(int, input().split()))
#list.sort(reverse=True)
#for i in range(a):
#    print(list[i], end=" ")



#211

#n, l, r = map(int, input().split())
#arr = list(map(int, input().split()))

#l -= 1
#r -= 1

# l мен r аралығын кері аударамыз
#arr[l:r+1] = arr[l:r+1][::-1]

# Нәтижені шығару
#for x in arr:
#    print(x, end=" ")



#212
#n = int(input())
#arr = list(map(int, input().split()))

#for i in range(n):
#    arr[i] = arr[i] ** 2

#for x in arr:
#    print(x, end=" ")



#213
#a=int(input())
#test=0
#if a<=1:
#    print("NO")
#else:
#    for i in range(1,a+1):
#        if a%i==0:
#            test+=1
#    if test==2:
#        print("YES")
#    else:
#        print("NO")




#214
#n = int(input())
#arr = list(map(int, input().split()))

#freq = {}

# әр элементтің санын есептейміз
#for x in arr:
#    if x in freq:
#        freq[x] += 1
#    else:
#        freq[x] = 1

#max_count = 0
#answer = None

# ең жиі кездесетін элементті табамыз
#for x in freq:
#    if freq[x] > max_count:
#        max_count = freq[x]
#        answer = x
#    elif freq[x] == max_count:
#        if x < answer:
#            answer = x

#print(answer)



#215
#a=int(input())
#b=set()
#for i in range(a):
#    c=input()
#    b.add(c)
#print(len(b))



#216
#a=int(input())
#list=(list(map(int, input().split())))
#s=set() 

#for i in list:
#    if i not in s: 
#        print("YES")
#        s.add(i)
#    else:
#        print("NO")



#217
#n = int(input())
#freq = {}

#i = 0
#while i < n:
#    number = input().strip()
#    if number in freq:
#        freq[number] += 1
#    else:
#        freq[number] = 1
#    i += 1

#count = 0
#for number in freq:
#    if freq[number] == 3:
#        count += 1

#print(count)



#218
#n = int(input())
#arr = []


#for i in range(n):
#    s = input()
#    arr.append(s)

#first_pos = {}

#for i in range(n):
#    if arr[i] not in first_pos:
#        first_pos[arr[i]] = i + 1   


#for s in sorted(first_pos):
#    print(s, first_pos[s])



#219
#n = int(input())
#doramas = {}

#for i in range(n):
#    name, k = input().split()
#    k = int(k)

#    if name in doramas:
#        doramas[name] += k
#    else:
#        doramas[name] = k

#for name in sorted(doramas):
#    print(name, doramas[name])



#220
#import sys
#input = sys.stdin.readline  # для очень больших данных

#n = int(input())
#doc = {}

#for _ in range(n):
#    command = input().split()
#    if command[0] == "set":
#        doc[command[1]] = command[2]
#    else:  # get
#        key = command[1]
#        if key in doc:
#            print(doc[key])
#        else:
#            print(f"KE: no key {key} found in the document")