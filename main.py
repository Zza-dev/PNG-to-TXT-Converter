from window import *

app=App()

#Defining the grid and turning off resizing to the size of its widgets
app.frame_left.grid(row = 1, column = 0)
app.frame_left.grid_propagate(False)

app.frame_left_down.grid(row = 3, column = 0)
#app.frame_left_down.grid_propagate(False)

#app.label.grid(row=0,column=0)

app.lbl.grid(row=1,column=4,rowspan=6,columnspan=8)

#app.listbox.grid(row = 0, column = 0,columnspan=3,rowspan=12)
app.button.grid(row=0,column=0)
app.clear_button.grid(row=0,column=3)

app.button_ocr_one.grid(row = 5, column = 0)
app.button_ocr_all.grid(row = 7, column = 0)

app.root.mainloop()
