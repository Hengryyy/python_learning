#输入腿和头的数量
legs=int(input("legs "))
head=int(input("heads "))
#创建一个数字列表a
a=[number for number in range(1,head+1)]
#复制一个a用来遍历，避免改变a
for r in a.copy():
    c=head-r
    answer=(4*r)+(2*c)
    #有解则打印答案
    if answer==legs:
        print("chicken: "+str(c)+"\nrabbits: "+str(r))
    #无解则删除a中该尝试兔子数量r
    elif answer!=legs:
        a.remove(r)
#无解则打印出没有答案
if len(a)==0:
    print("No Answer")
