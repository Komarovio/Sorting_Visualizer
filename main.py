import random

from colors import *
from tkinter import *
from tkinter import ttk
from algorithms.bubble_sort import bubbleSort
from algorithms.merge_sort import mergeSort
from algorithms.quick_sort import quickSort
from algorithms.count_sort import count_sort

window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
# algo_list is to select which alforithm we want to use to sort
algo_list = ['Quick Sort', 'Bubble Sort', 'Merge Sort']

speed_name = StringVar()
# speed_list is for selecting sorting speed
speed_list = ['Fast', 'Medium', 'Slow']

# This empty list will be filled with random values every time we generate a new array
data = []

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# This function will generate array with random values every time we hit the generate button
def generate():
    global data

    data = []
    for _ in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for _ in range(len(data))])

# This function will set sorting speed
def set_speed():
    if speed_alg_menu.get() == 'Slow':
        return 0.3
    elif speed_alg_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()
    
    if sort_alg_menu.get() == 'Bubble Sort':
        bubbleSort(data, drawData, timeTick)
        
    elif sort_alg_menu.get() == 'Merge Sort':
        mergeSort(data, 0, len(data) - 1, drawData, timeTick)
        
    elif sort_alg_menu.get() == 'Quick Sort':
        quickSort(data, 0, len(data) - 1, drawData, timeTick)

UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
sort_alg_label = Label(UI_frame, text="Algorithm: ", bg=WHITE)
sort_alg_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
sort_alg_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
sort_alg_menu.grid(row=0, column=1, padx=5, pady=5)
sort_alg_menu.current(0)

# dropdown to select sorting speed 
speed_alg_label = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
speed_alg_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_alg_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_alg_menu.grid(row=1, column=1, padx=5, pady=5)
speed_alg_menu.current(0)

# sort button 
sort_button = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
sort_button.grid(row=2, column=1, padx=5, pady=5)

# button for generating array 
generate_button = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
generate_button.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array 
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()