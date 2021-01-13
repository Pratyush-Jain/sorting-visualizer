from tkinter import *
from tkinter import font
import tkinter.font as font
from tkinter import ttk
import random
import time

class Alg:
    def bubbleSort(data):
        for i in range(len(data)-1):
            for j in range(len(data)-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    drawData(data,bar=[j+1],barColor='red')
                    
                    time.sleep(0.01)
            

    def insertionSort(data):
        for i in range(1,len(data)):
                val = data[i]
                 
                while val<data[i-1] and i>0:
                    drawData(data,bar=[i],barColor='red')
                    data[i],data[i-1]= data[i-1],data[i]
                    time.sleep(.001)
                    drawData(data,bar=[i+1],barColor='black')
                    time.sleep(.005)
                    i-=1
                    
        

    def merge(a, l, m, r): 
        n1 = m - l + 1
        n2 = r - m 
        L = [0] * n1 
        R = [0] * n2 
        for i in range(0, n1): 
            L[i] = a[l + i] 
        for i in range(0, n2): 
            R[i] = a[m + i + 1] 
    
        i, j, k = 0, 0, l 
        while i < n1 and j < n2: 
            if L[i] > R[j]: 
                a[k] = R[j] 
                j += 1
            else: 
                a[k] = L[i] 
                i += 1
            k += 1
            time.sleep(.001)
            drawData(a)
    
        while i < n1: 
            a[k] = L[i] 
            i += 1
            k += 1
            time.sleep(.001)
            drawData(a)
    
        while j < n2: 
            a[k] = R[j] 
            j += 1
            k += 1
            time.sleep(.001)
            drawData(a)

    def mergeSort(a): 
     
        current_size = 1
        
        # Outer loop for traversing Each 
        # sub array of current_size 
        while current_size < len(a) - 1:
             
            
            left = 0
            # Inner loop for merge call 
            # in a sub array 
            # Each complete Iteration sorts 
            # the iterating sub array 
            while left < len(a)-1: 
                
                # mid index = left index of 
                # sub array + current sub 
                # array size - 1 
                mid = min((left + current_size - 1),(len(a)-1))
                
                # (False result,True result) 
                # [Condition] Can use current_size 
                # if 2 * current_size < len(a)-1 
                # else len(a)-1 
                right = ((2 * current_size + left - 1, 
                        len(a) - 1)[2 * current_size 
                            + left - 1 > len(a)-1]) 
                                
                # Merge call for each sub array 
                Alg.merge(a, left, mid, right) 
                left = left + current_size*2
                
            # Increasing sub array size by 
            # multiple of 2 
            current_size = 2 * current_size 
    

    def selectionSort(data):
        
        for i in range(len(data)):
            minIndex = i
            #drawData(data,bar=[i],barColor='black')

            for j in range(i+1,len(data)):
                if data[minIndex]>data[j]:
                    minIndex = j
                drawData(data,bar=[minIndex],barColor='red')
                time.sleep(.001)
            
            data[minIndex],data[i] = data[i],data[minIndex]
            time.sleep(.001)
        
    def heapSort(data):
        pass
    def quickSort(data,start=0,end=None):
        if end is None:
            end = len(data)-1
        def partition(data,start,end):
            i = start-1
            pi = data[end]

            for j in range(start,end):
                if data[j]<pi:
                    i+=1
                    data[i],data[j]= data[j],data[i]
                    time.sleep(.001)
                    drawData(data,bar=[j])
            # bring the pivot to correct position
            data[end],data[i+1] = data[i+1],data[end]
            time.sleep(.001)
            #drawData(data)
            return(i+1)



        if start<end:
            time.sleep(.001)
            pivot = partition(data,start,end)
            drawData(data,bar=[pivot],barColor='black')
            time.sleep(0.001)
            Alg.quickSort(data,start,pivot-1)
            time.sleep(0.001)
            Alg.quickSort(data,pivot+1,end)    
        


root = Tk()
root.title('Sorting Algorithm Visualization')
root.geometry("600x600")
root.config(bg='#322f3d')
root.resizable(0,0)

OPTIONS={
    'Bubble Sort' : Alg.bubbleSort,
    'Insertion Sort' : Alg.insertionSort,
    'Merge Sort' : Alg.mergeSort,
    'Selection Sort' : Alg.selectionSort,
    'Heap Sort' : Alg.heapSort,
    'Quick Sort' : Alg.quickSort
}

   
# Widgets
frame_set = Frame(master=root,background='#4b5d67')
frame_set.pack(padx=10,pady=10)
frame_viz = Frame(master=root)
frame_viz.pack()
#'#93baba'
canvas = Canvas(frame_viz,width=600,height=505,bg='white')
canvas.pack()

# Combobox click callback function
def callback(event):
    randomize()
    
def randomize():
    global Algorithm,data
    Algorithm = option.get()
    data = random.sample(range(1,100),99)
    drawData(data)

def sort():
    btn_randomize["state"] = DISABLED
    global data,Algorithm
    if not data:
	    return
  
    Algo = OPTIONS[option.get()]
    Algo(data)
    drawData(data,'#86ff61')
    btn_randomize["state"] = NORMAL

# Draw the data on screen
def drawData(data,color= '#407d7d',bar=[],barColor='red'):
    canvas.delete("all")
    c_height = 505
    c_width = 600
    x = c_width/(len(data))

    normalizedData = [ i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        
        if i in bar:
            canvas.create_line(i*x,c_height-height*500,i*x,c_height,width=3,fill=barColor)
        else:  
            canvas.create_line(i*x,c_height-height*500,i*x,c_height,width=3,fill=color)
    root.update()

lbl_algo = Label(frame_set,text='Algorithm:',background='#4b5d67',foreground='white')
option = ttk.Combobox(frame_set,values=list(OPTIONS.keys()),state='readonly')
option.current(0)
option.bind("<<ComboboxSelected>>",callback)
style = ttk.Style()

style.map('TCombobox', focusfill=[('readonly','#505050')])
style.map('TCombobox', selectbackground=[('readonly', '#505050')])
style.map('TCombobox', selectforeground=[('readonly', 'white')])

#Set the color of dropdown list bg
root.option_add('*TCombobox*Listbox.background','#505050')
# Dropdown list text color
root.option_add('*TCombobox*Listbox.foreground','white')



btn_randomize = Button(master=frame_set,text='Randomize',padx=10,pady=10,command=randomize)
btn_sort = Button(master=frame_set,text='Sort',padx=10,pady=10,command=sort)
# Configs
btn_font = font.Font(size=16)
btn_randomize['font']= btn_font
btn_sort['font'] = btn_font



# Geometry Management

lbl_algo.pack(side='left',padx=5,pady=5)
option.pack(side='left',padx=5,pady=5)
btn_randomize.pack(side='left',padx=5,pady=5)
btn_sort.pack(side='left',padx=5,pady=5)

randomize()
root.mainloop()