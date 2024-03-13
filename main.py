from tkinter import*
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os as os
import numpy as np
import time
import random
import math

#book algorithm 2 is implemented using counting sort with highlighted range

#Book algorithm 1
def newinsertionSort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            j-= 1
            drawData(arr, ["RED" if x==j or x==j-1 else "BLUE" for x in range(len(arr))])
            time.sleep(speed)
        arr[j]= val

def advancedQuickSort(arr, low, high):
    while (low < high):

        if (high-low + 1<10):
            newinsertionSort(arr, low, high)
            break
 
        else:
            pivot = partition(arr, low, high)

            if pivot-low<high-pivot:
                advancedQuickSort(arr, low, pivot-1)
                low = pivot + 1
            else:
                advancedQuickSort(arr, pivot + 1, high)
                high = pivot - 1

#bucket sort
def bucketSort(array):
    max_value = max(array)
    size = max_value/len(array)
    num_buckets = int(len(array)/size)

    buckets_list= []
    for x in range(len(array)):
        buckets_list.append([])

    for i in range(len(array)):
        j = int (array[i] / size)
        if j != len (array):
            buckets_list[j].append(array[i])
        else:
            buckets_list[len(array) - 1].append(array[i])

    for z in range(len(array)):
        drawData(buckets_list[z], ["BLUE" for x in range(len(buckets_list[z]))])
        time.sleep(speed)
        insertionSort(buckets_list[z], 0)
        drawData(buckets_list[z], ["BLUE" for x in range(len(buckets_list[z]))])
        time.sleep(speed)
            
    output = []
    for x in range(len (array)):
        foutput = output + buckets_list[x]
        drawData(output, ["BLUE" for x in range(len(output))])
        time.sleep(speed)

# Radix sort
def countingSort_radix(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = int(array[i] // place)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = int(array[i] // place)
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
        drawData(array, ["BLUE" for x in range(len(array))])
        time.sleep(speed)

def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort_radix(array, place)
        place *= 10

# Counting sort
def countingSort(arr):
    maxElement= int(max(arr))
    countArrayLength = maxElement+1
    countArray = [0] * countArrayLength

    for el in arr: 
        countArray[int(el)] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1]

    outputArray = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        currentEl = int(arr[i])
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1
        drawData(outputArray, ["BLUE" for x in range(len(outputArray))])
        time.sleep(speed)

    arr.clear()
    for i in outputArray:
        arr.append(i)

# Heap Sort in python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        drawData(arr, ["RED" if x==i or x==largest else "BLUE" for x in range(len(arr))])
        time.sleep(speed)
        heapify(arr, n, largest)
  
def heapSort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        drawData(arr, ["RED" if x==i or x==0 else "BLUE" for x in range(len(arr))])
        time.sleep(speed)
        heapify(arr, i, 0)

# Quick sort in Python
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            drawData(array, ["RED" if x==i or x==j else "BLUE" for x in range(len(array))])
            time.sleep(speed)

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    drawData(array, ["RED" if x==i or x==j else "BLUE" for x in range(len(array))])
    time.sleep(speed)
    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

#Merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0
    j = 0
    k = l
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        drawData(arr, ["RED" if x==k else "BLUE" for x in range(len(arr))])
        time.sleep(speed)
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        drawData(arr, ["RED" if x==k else "BLUE" for x in range(len(arr))])
        time.sleep(speed)
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        drawData(arr, ["RED" if x==k else "BLUE" for x in range(len(arr))])
        time.sleep(speed)
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# Insertion sort in Python
def insertionSort(array, flag):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
          
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            if(flag):
                drawData(a, ["RED" if x==j or x==j+1 else "BLUE" for x in range(len(a))])
                time.sleep(speed)
        
        array[j + 1] = key

# Bubble sort in Python
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                drawData(a, ["RED" if j==x or j+1==x else "BLUE" for x in range(len(a))])
                time.sleep(speed)
        
a = []
b = []
y = []
n = 0
rmin = 0
rmax = 0
r_a = 0
r_b = 0
filepath = "none"
speed = 0.0

algos = [
    ("Bubble Sort", "O(n^2)", "O(1)"),
    ("Insertion Sort", "O(n^2)", "O(1)"),
    ("Merge Sort", "O(n log(n))", "O(n)"),
    ("Quick Sort", "O(n log(n))", "O(n)"),
    ("Heap Sort", "O(n log(n))", "O(1)"),
    ("Counting Sort", "O(n+k)", "O(n+k)"),
    ("Radix Sort", "O(n*k)", "O(n+k)"),
    ("Bucket Sort", "O(n+k)", "O(n+k)"),
    ("Advanced Quick Sort", "O(n log(n))", "O(n)")
]

def browseFiles(filepath):
    filepath = filedialog.askopenfilename(initialdir = os.getcwd, title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    try:
        if os.stat(filepath).st_size > 0:
            label_file_exp.configure(text="File path: " + filepath)
            readFile(filepath)
        else:
            canvas.delete("all")
            label_file_exp.configure(text="File Explorer")
            messagebox.showerror("Error", "File is empty!")
    except OSError:
        canvas.delete("all")
        label_file_exp.configure(text="File Explorer")
        messagebox.showerror("Error", "No File selected!")
        

def current_algo(event):
    algo = event.widget.get()
    if(algo == algos[0][0]):
        write_time_complexity(algos[0][1])
        write_space_complexity(algos[0][2])
    elif(algo == algos[1][0]):
        write_time_complexity(algos[1][1])
        write_space_complexity(algos[1][2])
    elif(algo == algos[2][0]):
        write_time_complexity(algos[2][1])
        write_space_complexity(algos[2][2])
    elif(algo == algos[3][0]):
        write_time_complexity(algos[3][1])
        write_space_complexity(algos[3][2])
    elif(algo == algos[4][0]):
        write_time_complexity(algos[4][1])
        write_space_complexity(algos[4][2])
    elif(algo == algos[5][0]):
        write_time_complexity(algos[5][1])
        write_space_complexity(algos[5][2])
    elif(algo == algos[6][0]):
        write_time_complexity(algos[6][1])
        write_space_complexity(algos[6][2])
    elif(algo == algos[7][0]):
        write_time_complexity(algos[7][1])
        write_space_complexity(algos[7][2])
    elif(algo == algos[8][0]):
        write_time_complexity(algos[8][1])
        write_space_complexity(algos[8][2])

def selected():
    algo = algmenu.get()
    k = rmax
    if not a:
        messagebox.showerror("Error", "No file selected!")
        return

    if a != y:
        messagebox.showerror("Error", "Data already sorted!")
        return
        
    if(algo == algos[0][0]):
        t = pow(n, 2)
        write_time_complexity(t)
        bubbleSort(a)
    elif(algo == algos[1][0]):
        t = pow(n, 2)
        write_time_complexity(t)
        insertionSort(a, 1)
    elif(algo == algos[2][0]):
        t = n * math.log(n, 2)
        t = round(t, 4)
        write_time_complexity(t)
        write_space_complexity(n)
        mergeSort(a, 0, len(a)-1)
    elif(algo == algos[3][0]):
        t = n * math.log(n, 2)
        t = round(t, 4)
        write_time_complexity(t)
        write_space_complexity(n)
        quickSort(a, 0, len(a)-1)
    elif(algo == algos[4][0]):
        t = n * math.log(n, 2)
        t = round(t, 4)
        write_time_complexity(t)
        heapSort(a)
    elif(algo == algos[5][0]):
        t = n + k
        write_time_complexity(t)
        write_space_complexity(t)
        countingSort(a)
    elif(algo == algos[6][0]):
        t = n * k
        write_time_complexity(t)
        write_space_complexity(n + k)
        radixSort(a)
    elif(algo == algos[7][0]):
        t = n + k
        write_time_complexity(t)
        write_space_complexity(t)
        bucketSort(a)
    elif(algo == algos[8][0]):
        t = n * math.log(n, 2)
        t = round(t, 4)
        write_time_complexity(t)
        write_space_complexity(n)
        advancedQuickSort(a, 0, len(a)-1)
    
    drawData(a, ["green" if a[x] >= r_a and a[x] <= r_b else "blue" for x in range(len(a))])
    messagebox.showinfo("Success", "Sorting completed!")

def set_speed(event):
    global speed 
    speed = 1 - speedbar.get()

def set_size(event):
    global n
    n = sizebar.get()

def set_min(event):
    global rmin
    rmin = int(rangemin.get())

def set_max(event):
    global rmax
    rmax = rangemax.get()

def set_a(event):
    global r_a
    r_a = range_a.get()

def set_b(event):
    global r_b
    r_b = range_b.get()

root = Tk()
root.title("ALGO PROJECT")
root.config(bg = "black")
#root.minsize(1000, 700)
root.resizable(0, 0)
window_width = 985 #int(2/3 * root.winfo_screenwidth())
window_height = 900 #int(2/3 * root.winfo_screenheight())
canvas_width = 960
canvas_height = 500
root.geometry(str(window_width) + "x" + str(window_height))
selection = StringVar()

frame1 = Frame(root, width=960, height=400, bg="grey")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
frame2 = Frame(root, width=960, height=400, bg="grey")
frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
frame3 = Frame(root, width=300, height=200, bg="black", border=5, relief="sunken")
frame3.grid(row=3, column=0, padx=10, pady=10, sticky="n")
frame1.columnconfigure(0, weight=1)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.columnconfigure(3, weight=1)
frame1.columnconfigure(4, weight=1)
frame1.columnconfigure(5, weight=1)

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="grey")
canvas.grid(row=2, column=0, padx=10, pady=10,)

label_select = Label(frame1, text="Select Algorithm:", bg='Grey')
label_select.grid(padx=5, pady=5)
label_file_exp = Label(frame2, text = "File Explorer", width = 135, height = 4, fg = "blue")
label_file_exp.grid(row=1, column = 0, padx=5, pady=5, sticky="nswe")
label_tcomp = Label(frame3, text = "Time Complexity: " + algos[0][1], background="black", fg = "white")
label_tcomp.grid(row=0, column = 0, padx=5, pady=5, sticky="n")
label_scomp = Label(frame3, text = "Space Complexity: " + algos[0][2], background="black", fg = "white")
label_scomp.grid(row=1, column = 0, padx=5, pady=5)

algmenu = ttk.Combobox(frame1, textvariable=selection, values=[x[0] for x in algos], width=22, state="readonly", justify=LEFT)
algmenu.grid(row=0, column = 1, padx=5, pady=5)
algmenu.current(0)
algmenu.bind("<<ComboboxSelected>>", current_algo)

speedbar = Scale(frame1, from_=0.5, to=1.0, width=22, length=100, digits=2, resolution=0.01, orient=HORIZONTAL, label="Speed:", command=set_speed)
speedbar.set(1)
speedbar.grid(row=1, column = 0, padx=5, pady=5)

sizebar = Scale(frame1, from_=0, to=1000, width=22, length=100, digits=3, resolution=1, orient=HORIZONTAL, label="Data Size:", command=set_size)
sizebar.set(50)
sizebar.grid(row=1, column = 1, padx=5, pady=5)

rangemin = Scale(frame1, from_=1, to=1000, width=22, length=100, digits=3, resolution=1, orient=HORIZONTAL, label="Min:", command=set_min)
rangemin.set(1)
rangemin.grid(row=1, column = 2, padx=5, pady=5)

rangemax = Scale(frame1, from_=1, to=1000, width=22, length=100, digits=3, resolution=1, orient=HORIZONTAL, label="Max:", command=set_max)
rangemax.set(100)
rangemax.grid(row=1, column = 3, padx=5, pady=5)

range_a = Scale(frame1, from_=0, to=1000, width=22, length=100, digits=3, resolution=1, orient=HORIZONTAL, label="Range a:", command=set_a)
range_a.set(0)
range_a.grid(row=1, column = 4, padx=5, pady=5)

range_b = Scale(frame1, from_=0, to=1000, width=22, length=100, digits=3, resolution=1, orient=HORIZONTAL, label="Range b:", command=set_b)
range_b.set(0)
range_b.grid(row=1, column = 5, padx=5, pady=5)

def write_time_complexity(t):
    label_tcomp.configure(text="Time Complexity: " + str(t))

def write_space_complexity(s):
    label_scomp.configure(text="Space Complexity: " + str(s))

def drawData(data, colorArray):
    canvas.delete("all")
    cwidth = canvas_width
    cheight = canvas_height
    x_width = cwidth / (len(data) + 1)
    offset = 10
    spacing = 3
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = cheight - height * 350
        x1 = (i + 1) * x_width + offset
        y1 = cheight
        
        if(x_width > 15):
            canvas.create_text(x0+7, y0-12, text=int(data[i]), fill="black")
        if(len(data) < 200):
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="black", width=1)
            continue
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="black", width=0)

    root.update_idletasks()

def generate():
    try:
        list = random.sample(range(rmin, rmax), n)
        return list
    except ValueError:
        messagebox.showinfo("Error", "Range is too small for the amount of data!")
        return 0

def deleteFile():
    if(os.path.exists("data.txt")):
        try:
            os.remove("data.txt")
        except IOError:
            messagebox.showinfo("File", "File in Use!")
            return
        canvas.delete("all")
        messagebox.showinfo("File Deleted", "File deleted successfully!")
    else:
        messagebox.showinfo("File Not Found", "File not found!")

def createFile():
    if(os.path.exists("data.txt")):
        msg_box = messagebox.askquestion("File Exists", "File already exists! Do you want to open existing file?", icon='warning')
        if msg_box == 'yes':
            readFile("data.txt")
        return

    list = generate()
    if(list == 0):
        messagebox.showinfo("Error", "File not created!")
        return

    file = open("data.txt", "w+")
    for i in range(len(list)):
        if(i == len(list)-1):
            file.write(str(list[i]))
            break
        file.write(str(list[i]) + " ")
    
    file.close()
    messagebox.showinfo("File Created", "File created successfully!")
    path = os.getcwd() + "\data.txt"
    readFile(path)

def readFile(path):
    file = open(path, "r")
    i = 0
    b = file.read()
    x = b.split(" ")
    a.clear()
    y.clear()
    for i in range(len(x)):
        a.append(float(x[i]))
        y.append(float(x[i]))
    Label(frame2, text = "File Opened: " + path, width = 100, height = 4, fg = "blue").grid(row=1, column = 0, padx=5, pady=5)
    drawData(a, ["BLUE" for x in range(len(a))])
    file.close()

def resetData():
    if not a:
        messagebox.showinfo("No Data", "No data to reset!")
        return
    a.clear()
    for i in y:
        a.append(i)
    drawData(a, ["BLUE" for x in range(len(a))])

button_start = Button(frame1,width=5, height=1, text="START", bg="white", command=lambda:selected()).grid(row=0, column = 2, padx=5, pady=5, sticky="w")
button_reset = Button(frame1,width=5, height=1, text="RESET", bg="white", command = resetData).grid(row=0, column = 2, padx=5, pady=5, sticky="n")
button_exit = Button(frame1,width=5, height=1, text="EXIT", bg="white", command=root.destroy).grid(row=0, column = 2, padx=5, pady=5, sticky="e")
button_browsefile = Button(frame2, width=10, text = "Browse Files",command = lambda: browseFiles(filepath)).grid(row=0, column = 0, padx=5, pady=5, sticky="w")
button_createfile = Button(frame2, width=10, text = "Create File",command = lambda: createFile()).grid(row=0, column = 0, padx=5, pady=5, sticky="n")
button_deletefile = Button(frame2, width=10, text = "Delete File",command = lambda: deleteFile()).grid(row=0, column = 0, padx=5, pady=5, sticky="e")

root.mainloop()