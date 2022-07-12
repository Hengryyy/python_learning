legs=int(input("legs "))
head=int(input("heads "))
a=[number for number in range(1,head+1)]
b=a[:]
for r in b:
    c=head-r
    answer=(4*r)+(2*c)
    if answer==legs:
        print("chicken: "+str(c)+"\nrabbits: "+str(r))
    elif answer!=legs:
        a.remove(r)
if len(a)==0:
    print("No Answer")