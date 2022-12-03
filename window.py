from tkinter import *
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import filedialog as fd
import os
import cv2
import pytesseract
from PIL import Image, ImageTk

class App():
	
	root=ThemedTk(theme="equilux")
	root.geometry("1280x1024")
	root.title("OCR")
	root['bg']='grey'

	root.columnconfigure((0, 1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), weight=1, minsize=30)
	root.rowconfigure((0, 1, 2, 3,4,5,6,7,8,9,10,11,12), weight=1, minsize=30)

	frame_left=LabelFrame(root,height=1024,width=320,pady=0,padx=0)
	frame_left['bg']="grey"
	frame_left.columnconfigure((0, 1, 2, 3), weight=1, minsize=30)
	frame_left.rowconfigure((0, 1, 2, 3,4,5,6,7,8,9,10,11,12), weight=1, minsize=30)

	frame_left_down=Frame(root,height=2048,width=320,pady=0,padx=0)
	frame_left_down['bg']="grey"
	frame_left_down.columnconfigure((0, 1, 2), weight=1, minsize=30)
	frame_left_down.rowconfigure((0, 1, 2, 3,4,5,6,7,8,9,10,11,12), weight=1, minsize=30)
	
	
	img1 = Image.open("IMAGES/1.png")
	img2 = img1.resize((450, 350), Image.ANTIALIAS)
	original1=ImageTk.PhotoImage(img2)
	lbl=Label(root,image=original1)

	currentImage=None
	itemList=[]
	fileNames=[]
	count=0
	index=None
	# Tkinter passes an event object to onselect()
	def preview(evt):
    	
		w = evt.widget
		index = int(w.curselection()[0])
		App.index=index
		value = w.get(index)
		print(value)
		print(index)
		print(App.count)
		image = Image.open(App.itemList[index])

		# The (450, 350) is (height, width)
		image2 = image.resize((450, 350), Image.ANTIALIAS)

		original=ImageTk.PhotoImage(image)
		resized = ImageTk.PhotoImage(image2)
		#print(type(resized))
		App.lbl.configure(image=resized)
		App.lbl.photo = resized
		App.currentImage = (App.itemList[index])

	listbox = tk.Listbox(frame_left_down,height=150,selectmode=tk.EXTENDED)
	listbox.bind('<<ListboxSelect>>', preview)
	listbox.grid(row = 0, column = 0,columnspan=3,rowspan=12)
	
	

	def clear_selection():
		App.listbox.delete(0,END)

	def open_file():
		App.listbox.delete(0,END)
		App.count=0
		App.itemList=[]
		App.fileNames=[]

		files = fd.askopenfiles(mode='r', filetypes=[('Images', '*.png')])
		
		if files:
			for i in files:
				print(App.count)
				filepath=i.name
				basename = os.path.basename(filepath)
				App.fileNames.append(basename)
				App.itemList.append(i.name)
				print(App.itemList)
				App.listbox.insert(App.count, basename)
				App.count+=1
				


	def convert():
		result=pytesseract.image_to_string(App.currentImage)
		print(result)
		
		with open('Output/'+App.fileNames[App.index]+'.txt','w') as f:
			print(result,file=f)

	def convert_all():
		for i in App.itemList:
			result=pytesseract.image_to_string(i)
			print(result)
			x=App.itemList.index(i)
		
			with open('Output/'+App.fileNames[x]+'.txt','w') as f:
				print(result,file=f)


	button=Button(frame_left, text="Browse",command=open_file)
	clear_button=Button(frame_left, text="Clear",command=clear_selection)

	button_ocr_one=Button(root, text="Convert Current",command=convert)
	button_ocr_all=Button(root, text="Convert All",command=convert_all)

	
