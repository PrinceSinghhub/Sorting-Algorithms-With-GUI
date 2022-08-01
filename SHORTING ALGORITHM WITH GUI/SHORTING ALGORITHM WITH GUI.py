from tkinter import*
from tkinter import ttk
root = Tk()
root.title('SHORTING ALGORITHM WITH GUI')
root.geometry("1366x770")
photo=PhotoImage(file="i.png")
lable=Label(image=photo)
lable.place(x=50,y=200)
# root.resizable(False, False)
# todo color picker bg='#9ea0a3'
root.config(bg='#6e717a')
Label(root, text='SHORTING ALGORITHM WITH GUI', font='Verdana 35 bold',bg="#6e717a",fg='#00154f').pack()
Label(root, text='CODEX CODER', font='Verdana 15 bold', fg='#050505', bg="#6e717a").pack()
TextBox = Text(root, height=35, width=70, font='Verdana 10 bold',fg='#00154f')
TextBox.place(x = 700, y=110)

# todo combobox
def COMMAND():
    c=languages.get()
    if c == "Select Option":
        pass
    elif c!= "Select Option":
        eval(c+"()")

shorting=["BoobleShort","InsertionShort","SecletionShort","QuickShort","CountShort","MergeShort"]
languages=ttk.Combobox(root,values=shorting,state='readonly',justify=CENTER,font='Verdana 10 bold')
languages.place(x=50,y=200,width=200,height=40)
languages.set("Select Option")

INPUT = StringVar()

# todo boobleshort
def BoobleShort():
    TextBox.delete('1.0', END)

    x=INPUT.get().split()
    r = "_____Booble Short Algorithm By Codex Coder_____"
    TextBox.insert(END, r.center(120))
    TextBox.insert(END, "\n\n\n")


    List1 = []
    for i in x:
        List1.append(int(i))

    # todo Boobleshort
    instruction = "USER INPUT OUTPUT RESULT\n"
    TextBox.insert(END,instruction)
    a1 = f"UnShorted List is : {List1}\n"
    TextBox.insert(END, a1)

    for j in range(len(List1) - 1):
        for i in range(len(List1) - 1):
            if List1[i] > List1[i + 1]:
                List1[i], List1[i + 1] = List1[i + 1], List1[i]

    a1 = f"Sorted List is (Acceding Order): {List1}\n"
    TextBox.insert(END, a1)

    for j in range(len(List1) - 1):
        for i in range(len(List1) - 1):
            if List1[i] < List1[i + 1]:
                List1[i], List1[i + 1] = List1[i + 1], List1[i]

    a1 = f"Sorted List is (Decending Order): {List1}\n\n"
    TextBox.insert(END, a1)


    # todo alogrithm of booble short
    a='''x=[]
n=int(input("How many no to want run the programe"))
print("Enter a Number")
for a in range(n):
    x.append(int(input()))
for j in range (len(x)-1):
    for i in range (len(x)-1-j):
       if x[i]>x[i+1]:
            x[i],x[i+1] = x[i+1],x[i]
            print(x)
       else:
           print(x)
       print()
print(x)
'''
    d="BOOBLE SHORT ALGORITHM\n"
    TextBox.insert(END,d)
    TextBox.insert(END, a)
    TextBox.insert(END, "\n\n")

    result="Booble Short Algorithm Analysis\n"
    TimeComplexcity = '''Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complecity: 1
Booble Short Algorithm are Internal Shorting Algorithm
Booble Short Algorithm are Non-Recursive Shorting Algorithm
Stability: Yes Booble Short Algorithm Are Stable Algorithm
Adpative: Yes Booble Short Algorithm Are Adpative Algorithm'''

    TextBox.insert(END,result)
    TextBox.insert(END,TimeComplexcity)

# todo insertion short
def InsertionShort():
    TextBox.delete('1.0', END)

    x = INPUT.get().split()
    r = "_____Insertion Short Algorithm By Codex Coder_____"
    TextBox.insert(END, r.center(120))
    TextBox.insert(END, "\n\n\n")

    a=[]
    for i in x:
        a.append(int(i))

    instruction = "USER INPUT OUTPUT RESULT\n"
    TextBox.insert(END, instruction)
    a1 = f"UnShorted List is : {a}\n"
    TextBox.insert(END, a1)

    # todo Insertionshort
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    a1 = f"Sorted List is (Acceding Order):{a}\n"
    TextBox.insert(END, a1)

    # todo Insertionshort
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    a1 = f"Sorted List is (Dessending Order): {a}\n\n"
    TextBox.insert(END, a1)

    # todo alogrithm of Insertion short
    x='''s=int(input("Inter Your List Size"))
A=[]
for a in range (s):
    x=int(input("Enter Element"))
    A.append(x)
for i in range (1,s):
    t=A[i]
    j=i-1
    while j>=0 and t<A[j]:
        A[j+1]=A[j]
        j=j-1
    A[j+1]=t
    print(A)
'''

    d = "INSERTION SHORT ALGORITHM\n"
    TextBox.insert(END, d)
    TextBox.insert(END, x)
    TextBox.insert(END, "\n\n")

    result = "Insertion Short Algorithm Analysis\n"
    TimeComplexcity = '''Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complecity: 1
Insertion Short Algorithm are Internal Shorting Algorithm
Insertion Short Algorithm are Non-Recursive Shorting Algorithm
Stability: Yes Insertion Short Algorithm Are Stable Algorithm
Adpative: Yes Insertion Short Algorithm Are Adpative Algorithm'''

    TextBox.insert(END, result)
    TextBox.insert(END, TimeComplexcity)

# todo Selection Short
def SecletionShort():
    TextBox.delete('1.0', END)

    x = INPUT.get().split()
    r = "_____Selection Short Algorithm By Codex Coder_____"
    TextBox.insert(END, r.center(120))
    TextBox.insert(END, "\n\n")

    num=[]
    for i in x:
        num.append(int(i))

    instruction = "USER INPUT OUTPUT RESULT\n"
    TextBox.insert(END, instruction)
    a1 = f"UnShorted List is : {num}\n"
    TextBox.insert(END, a1)

    # todo selection short
    l = len(num)
    for i in range(l):
        mean_value = i
        for j in range(i, l):
            if num[j] < num[mean_value]:
                mean_value = j
        temp = num[i]
        num[i] = num[mean_value]
        num[mean_value] = temp

    a1 = f"Sorted List is (Acceding Order):{num}\n"
    TextBox.insert(END, a1)

    l = len(num)
    for i in range(l):
        mean_value = i
        for j in range(i, l):
            if num[j] > num[mean_value]:
                mean_value = j
        temp = num[i]
        num[i] = num[mean_value]
        num[mean_value] = temp

    a1 = f"Sorted List is (Dessinding Order):{num}\n\n"
    TextBox.insert(END, a1)

# todo selection short algorithm
    x='''s=int(input("Inter Your List Size"))
num=[]
for a in range (s):
    x=int(input("Enter Element"))
    num.append(x)
l=len(num)
for i in range(l):
    mean_value = i
    for j in range(i,l):
        if num[j]<num[mean_value]:
            mean_value = j
    temp = num[i]
    num[i] = num[mean_value]
    num[mean_value] = temp
print(num)
'''

    d = "SELECTION SHORT ALGORITHM\n"
    TextBox.insert(END, d)
    TextBox.insert(END, x)
    TextBox.insert(END, "\n\n")

    result = "Selection Short Algorithm Analysis\n"
    TimeComplexcity = '''Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)
Space Complecity: 1
Selection Short Algorithm are Internal Shorting Algorithm
Selection Short Algorithm are Non-Recursive Shorting Algorithm
Stability: No Selection Short Algorithm Are Not Stable Algorithm
Adpative: No Selection Short Algorithm Are Not Adpative Algorithm'''

    TextBox.insert(END, result)
    TextBox.insert(END, TimeComplexcity)


# todo Quick Short Algorithm
def QuickShort():
    TextBox.delete('1.0', END)

    x = INPUT.get().split()
    r = "_____Quick Short Algorithm By Codex Coder_____"
    TextBox.insert(END, r.center(120))
    TextBox.insert(END, "\n\n")

    data = []
    for i in x:
        data.append(int(i))

    instruction = "USER INPUT OUTPUT RESULT\n"
    TextBox.insert(END, instruction)
    a1 = f"UnShorted List is : {data}\n"
    TextBox.insert(END, a1)

    def pivot_value(data, first, last):
        pivot = data[first]
        left = first + 1
        right = last

        while True:
            while left <= right and data[left] <= pivot:
                left = left + 1
            while left <= right and data[right] >= pivot:
                right = right - 1
            if right < left:
                break
            else:
                data[left], data[right] = data[right], data[left]

        data[first], data[right] = data[right], data[first]
        # print("for step how to run")
        # print(data)
        return right

    def quickshort(data, first, last):
        if first <= last:
            a = pivot_value(data, first, last)
            quickshort(data, first, a - 1)
            quickshort(data, a + 1, last)

    # todo funcrion call
    b = len(data)
    quickshort(data, 0, b - 1)

    a1 = f"Sorted List is (Acceding Order):{data}\n"
    TextBox.insert(END, a1)

# todo decessinging order



    a1 = f"Sorted List is (Dessending Order):{data}\n\n"
    TextBox.insert(END, a1)

    # todo quick short algorithm
    r='''def pivot_value(data,first,last):
    pivot=data[first]
    left = first+1
    right = last

    while True:
        while left<=right and data[left] <= pivot:
            left = left+1
        while left <= right and data[right] >= pivot:
            right = right-1
        if right<left:
            break
        else:
            data[left],data[right] = data[right],data[left]

    data[first],data[right] = data[right],data[first]
    print("for step how to run")
    print(data)
    return right

def quickshort(data,first,last):
    if first<=last:
        a = pivot_value(data, first, last)
        quickshort(data, first, a - 1)
        quickshort(data, a + 1, last)

data=[10,6,5,4,3,2,1]
b=len(data)
quickshort(data,0,b-1)
print(f"Final Ans : {data}")
'''
    d = "QUICK SHORT ALGORITHM\n"
    TextBox.insert(END,d)
    TextBox.insert(END,r)
    TextBox.insert(END, "\n\n")

    result = "Quick Short Algorithm Analysis\n"
    TimeComplexcity = '''Best Case: O(nlogn)
Average Case: O(nlogn)
Worst Case: O(n^2)
Space Complecity: O(logn)
Quick Short Algorithm are Internal Shorting Algorithm
Quick Short Algorithm are Recursive Shorting Algorithm
Stability: No Quick Short Algorithm Are Not Stable Algorithm
Adpative: Yes Quick Short Algorithm Are Adpative Algorithm'''

    TextBox.insert(END, result)
    TextBox.insert(END, TimeComplexcity)


def CountShort():
    TextBox.delete('1.0', END)
    x = INPUT.get().split()
    r = "_____Count Short Algorithm By Codex Coder_____"
    TextBox.insert(END, r.center(120))
    TextBox.insert(END, "\n\n\n")

    List1 = []
    for i in x:
        List1.append(int(i))

    # todo Boobleshort
    instruction = "USER INPUT OUTPUT RESULT\n"
    TextBox.insert(END, instruction)
    a1 = f"UnShorted List is : {List1}\n"
    TextBox.insert(END, a1)
    if len(List1)<2:
        a1 = f"Sorted List is :{List1}\n\n"
        TextBox.insert(END, a1)

    elif len(List1)>=2:
        def shorting(count_data):
            A = count_data

            Result = []

            for i in range(len(A)):

                if A[i] == 1:

                    Result.append(i)

                elif A[i] > 1:
                    d = A[i]
                    while (d >= 1):
                        Result.append(i)
                        d -= 1

            '''    0 1 2 3 4 5 6
               li=[6,6,6,5,2,1,1]

               max=6+1
               cont_list=[0]*6
                           0 1 2 3 4 5 6
               count_list=[0,2,1,0,0,1,3]
               r[]
               count_list=[0,2,1,0,0,1,3]
                           0 1 2 3 4 5 6
               r=[1,1,2,5,6,6,6]
               '''

            a1 = f"Sorted List is :{Result}\n\n"
            TextBox.insert(END, a1)


        def maxshort(List1):
            Max = max(List1) + 1
            cout_data = [0] * Max

            for i in List1:
                cout_data[i] += 1

            return cout_data

        b = maxshort(List1)
        shorting(b)




    # todo algrothm of Merge short

    x='''def shorting(count_data):
    A=count_data
    
    Result=[]
    
    for i in range(len(A)):
        if A[i] == 1:
            Result.append(i)
        
        elif A[i] > 1:
            d=A[i]
            while (d >= 1):
                Result.append(i)
                d-=1
    
    print("Sorted List is:",Result)

def maxshort(arr):
    Max=max(arr)+1
    cout_data = [0]*Max

    for i in arr:
        cout_data[i]+=1

    return cout_data

a=[6,6,6,5,2,1,1,0,0,7,7]
b=maxshort(a)
shorting(b)
print("No Counted List is : ",maxshort(a))'''

    d = "COUNT SHORT ALGORITHM\n"
    TextBox.insert(END, d)
    TextBox.insert(END, x)
    TextBox.insert(END, "\n\n")

    # todo anylysis

    result = "Count Short Algorithm Analysis\n"
    TimeComplexcity = '''Best Case: O(n+m)
Average Case: O(n+m)
Worst Case: O(n+m)
Space Complecity: O(n+m)
Count Short Algorithm are Internal Shorting Algorithm
Count Short Algorithm are Non Recursive Shorting Algorithm
Stability: No Count Short Algorithm Are Not Stable Algorithm
Adpative: No Count Short Algorithm Are Not Adpative Algorithm
Count Short Algorithm are take more much space'''

    TextBox.insert(END, result)
    TextBox.insert(END, TimeComplexcity)

def MergeShort():
    TextBox.delete('1.0', END)
    x = INPUT.get().split()
    r = "_____Merge Short Algorithm By Codex Coder_____"
    TextBox.insert(END, r.center(120))
    TextBox.insert(END, "\n\n\n")

    List1 = []
    for i in x:
        List1.append(int(i))

    instruction = "USER INPUT OUTPUT RESULT\n"
    TextBox.insert(END, instruction)
    a1 = f"UnShorted List is : {List1}\n"
    TextBox.insert(END, a1)

    # todo shorted process
    def merge_sort(arr1, arr2):
        x = len(arr1);
        y = len(arr2)
        A = arr1
        B = arr2
        Sorted_array = [0] * (x + y)
        i, j, k = 0, 0, 0
        while (i < x and j < y):
            if (A[i] < B[j]):
                Sorted_array[k] = A[i]
                i += 1;
                k += 1
            else:
                Sorted_array[k] = B[j]
                j += 1;
                k += 1
        while (i < x):
            Sorted_array[k] = A[i]
            i += 1
            k += 1
        while (j < y):
            Sorted_array[k] = B[j]
            j += 1
            k += 1
        return Sorted_array

    def break_array_and_sort(Arry):
        LOW = 0
        HIGH = len(Arry)
        # todo split our array
        mid_point = LOW + (LOW + HIGH) // 2
        R = Arry[mid_point:]
        L = Arry[:mid_point]
        R.sort();
        L.sort()
        result = merge_sort(L, R)


        # todo copy data in original array
        for i in range(HIGH):
            Arry[i] = result[i]

        a1 = f"Sorted List is :{Arry}\n\n"
        TextBox.insert(END, a1)


    break_array_and_sort(List1)

    # todo merge short algrothim

    x='''def mergeSort(arr):
        if len(arr) > 1:

            # todo find mid point of array
            mid = len(arr) // 2

            # todo Dividing the array elements
            L = arr[:mid]

            # todo right part
            R = arr[mid:]

            # todo Sorting the first half
            mergeSort(L)

            # todo Sorting the second half
            mergeSort(R)

            i = j = k = 0

            # todo Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # todo Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    # todo given array
    arr = [12, 11, 13, 5, 6, 7]
    print(f"Unsorted Array: {arr}")
    mergeSort(arr)
    t = []
    for i in arr:
        t.append(i)
    print(f"Sorted Array: {arr}")'''

    d = "MERGE SHORT ALGORITHM\n"
    TextBox.insert(END, d)
    TextBox.insert(END, x)
    TextBox.insert(END, "\n\n")

    # todo algorith, anylysis

    result = "Merge Short Algorithm Analysis\n"
    TimeComplexcity = '''Best Case: O(nlogn)
Average Case: O(nlogn)
Worst Case: O(nlogn)
Space Complecity: O(n)
Merge Short Algorithm are External Shorting Algorithm
Merge Short Algorithm are Recursive Shorting Algorithm
Stability: Yes Merge Short Algorithm Are Stable Algorithm
Adpative: Yes Merge Short Algorithm Are Adpative Algorithm
Merge Short Algorithm are Slower Algorithm then Other'''

    TextBox.insert(END, result)
    TextBox.insert(END, TimeComplexcity)

a = Entry(root, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=INPUT)
a.place(x=345, y=200)
Button(root, text='Search', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', command=COMMAND).place(x=115, y=160)
label = Label(root,text="User Input",bg='#f2bc94', fg='#00154f', font='Verdana 12 bold')
label.place(y=160,x=450)
# Button(root, text='INSERTION SHORT', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', command=InsertionShort).place(x=100, y=200)
# Button(root, text='SELECTION SHORT', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', command=SecletionShort).place(x=100, y=270)
# Button(root, text='QUICK SHORT', bg='#f2bc94', fg='#00154f', font='Verdana 10 bold', command=QuickShort).place(x=100, y=340)
root.mainloop()