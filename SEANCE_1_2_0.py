#-*- coding: utf-8 -*- 
from __future__ import division

import sys

#import spacy #this is for if spaCy is used
import tkinter as tk
import tkinter.font
import tkinter.filedialog
import tkinter.constants
import queue
from tkinter import messagebox

import os
import sys
import re
import platform
import glob
import math
from collections import Counter

from threading import Thread

def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)
	
if platform.system() == "Darwin":
	system = "M"
	title_size = 16
	font_size = 14
	geom_size = "425x650"
	color = "#ff771c"
elif platform.system() == "Windows":
	system = "W"
	title_size = 14
	font_size = 12
	geom_size = "450x650"
	color = "#ff771c"
elif platform.system() == "Linux":
	system = "L"
	title_size = 14
	font_size = 12
	geom_size = "450x650"
	color = "#ff771c"
	
#This creates a que in which the core TAALES program can communicate with the GUI
dataQueue = queue.Queue()

#This creates the message for the progress box (and puts it in the dataQueue)
progress = "...Waiting for Data to Process"
dataQueue.put(progress)

#This creates a function for starting a new thread. The arguments are what TAALES needs to run
#Def1 is the core TAALES program
def start_thread(def1, arg1, arg2, arg3):
	t = Thread(target=def1, args=(arg1, arg2, arg3))
	t.start()

		
#This is how the correct path is given for program files.
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)
	
class MyApp:
	def __init__(self, parent):
		
		#Creates font styles - Task: Make these pretty!
		
		
		helv14= tkinter.font.Font(family= "Helvetica Neue", size=font_size)
		times14= tkinter.font.Font(family= "Lucida Grande", size=font_size)
		helv16= tkinter.font.Font(family= "Helvetica Neue", size = title_size, weight = "bold", slant = "italic")
		
		#This defines the GUI parent (ish)
		self.myParent = parent
		
		#This creates the header text - Task:work with this to make more pretty!
		self.spacer1= tk.Label(parent, text= "SEntiment ANalysis and Cognition Engine", font = helv16, background = color)
		self.spacer1.pack()
		
		#This creates a frame for the meat of the GUI
		self.thestuff= tk.Frame(parent, background =color)
		self.thestuff.pack()
		#Currently, the sizes aren't doing anything...

		#Within the 'thestuff' frame, this creates a frame on the left for the buttons/input
		self.myContainer1 = tk.Frame(self.thestuff, background = color)
		self.myContainer1.pack(side = tk.RIGHT, expand = tk.TRUE)


		#Text to be displayed above the widgets AND for a line to be placed around the elements
		self.labelframe2 = tk.LabelFrame(self.myContainer1, text= "Instructions", background = color)
		self.labelframe2.pack(expand=tk.TRUE)
	
	#Checkbox	
		self.checkboxframe = tk.LabelFrame(self.myContainer1, text= "Indices", background = color, width = "45")
		self.checkboxframe.pack(expand=tk.TRUE)

		self.checkboxframe2 = tk.LabelFrame(self.myContainer1, text= "Words to Analyze", background = color, width = "45")
		self.checkboxframe2.pack(expand=tk.TRUE)
		
		self.myContainer2 = tk.Frame(self.myContainer1, background = color)
		self.myContainer2.pack(expand = tk.TRUE)
		
		self.checkboxframe3 = tk.LabelFrame(self.myContainer2, text= "Negation Control", background = color, width = "45")
		self.checkboxframe3.grid(row=1,column=2, sticky = "W")
		
		self.checkboxframe4 = tk.LabelFrame(self.myContainer2, text= "Components", background = color, width = "45")
		self.checkboxframe4.grid(row=1,column=1, sticky = "W")

		self.cb2_var = tk.IntVar()
		self.cb2 = ""
		
		self.cb3_var = tk.IntVar()
		self.cb3 = tk.Checkbutton(self.checkboxframe, text="GALC", variable=self.cb3_var,background = color)
		self.cb3.grid(row=1,column=1, sticky = "W")	
		self.cb3.bind("<Button-1>", self.clicker)
		self.cb3.deselect()
		
		self.cb4_var = tk.IntVar()
		
		self.cb4 = tk.Checkbutton(self.checkboxframe, text="EmoLex", variable=self.cb4_var,background = color)
		self.cb4.grid(row=1,column=2, sticky = "W")	
		self.cb4.deselect()
		self.cb4.bind("<Button-1>", self.clicker)

		self.cb5_var = tk.IntVar()
		
		self.cb5 = tk.Checkbutton(self.checkboxframe, text="ANEW", variable=self.cb5_var,background = color)
		self.cb5.grid(row=1,column=3, sticky = "W")	
		self.cb5.deselect()
		self.cb5.bind("<Button-1>", self.clicker)

		self.cb6_var = tk.IntVar()
		self.cb6 = tk.Checkbutton(self.checkboxframe, text="SENTIC", variable=self.cb6_var,background = color)
		self.cb6.grid(row=1,column=4, sticky = "W")	
		self.cb6.deselect()
		self.cb6.bind("<Button-1>", self.clicker)

		self.cb7_var = tk.IntVar()
		self.cb7 = tk.Checkbutton(self.checkboxframe, text="VADER", variable=self.cb7_var,background = color)
		self.cb7.grid(row=2,column=1, sticky = "W")	
		self.cb7.deselect()
		self.cb7.bind("<Button-1>", self.clicker)
		
		self.cb8_var = tk.IntVar()
		self.cb8 = tk.Checkbutton(self.checkboxframe, text="Hu-Liu", variable=self.cb8_var,background = color)
		self.cb8.grid(row=2,column=2, sticky = "W")	
		self.cb8.deselect()
		self.cb8.bind("<Button-1>", self.clicker)
		
		self.cb9_var = tk.IntVar()		
		self.cb9 = tk.Checkbutton(self.checkboxframe, text="GI", variable=self.cb9_var,background = color)
		self.cb9.grid(row=2,column=3, sticky = "W")			
		self.cb9.deselect()
		self.cb9.bind("<Button-1>", self.clicker)
		
		self.cb10_var = tk.IntVar()	
		self.cb10 = tk.Checkbutton(self.checkboxframe, text="Lasswell", variable=self.cb10_var,background = color)
		self.cb10.grid(row=2,column=4, sticky = "W")	
		self.cb10.deselect()
		self.cb10.bind("<Button-1>", self.clicker)


		self.cb11_var = tk.IntVar()
		self.cb11 = tk.Checkbutton(self.checkboxframe2, text="Nouns", variable=self.cb11_var,background = color)
		self.cb11.grid(row=1,column=2, sticky = "W")	
		self.cb11.deselect()
		
		self.cb12_var = tk.IntVar()		
		self.cb12 = tk.Checkbutton(self.checkboxframe2, text="Verbs", variable=self.cb12_var,background = color)
		self.cb12.grid(row=1,column=3, sticky = "W")	
		self.cb12.deselect()

		self.cb13_var = tk.IntVar()
		self.cb13 = tk.Checkbutton(self.checkboxframe2, text="Adjectives", variable=self.cb13_var,background = color)
		self.cb13.grid(row=1,column=4, sticky = "W")	
		self.cb13.deselect()

		self.cb14_var = tk.IntVar()		
		self.cb14 = tk.Checkbutton(self.checkboxframe2, text="Adverbs", variable=self.cb14_var,background = color)
		self.cb14.grid(row=1,column=5, sticky = "W")	
		self.cb14.deselect()
		
		self.cb15_var = tk.IntVar()		
		self.cb15 = tk.Checkbutton(self.checkboxframe2, text="All Words", variable=self.cb15_var,background = color)
		self.cb15.grid(row=1,column=1, sticky = "W")	
		self.cb15.deselect()

		self.cb16_var = tk.IntVar()		
		self.cb16 = tk.Checkbutton(self.checkboxframe3, text="Three Left", variable=self.cb16_var,background = color)
		self.cb16.grid(row=1,column=1, sticky = "W")	
		self.cb16.deselect()
				
		self.cb18_var = tk.IntVar()
		self.cb18 = tk.Checkbutton(self.checkboxframe4, text="Components", variable=self.cb18_var,background = color)
		self.cb18.grid(row=1,column=1, sticky = "W")	
		self.cb18.select()
		
		
		self.var_list = [self.cb2_var,self.cb3_var,self.cb4_var,self.cb5_var,self.cb6_var,self.cb7_var,self.cb8_var,self.cb9_var,self.cb10_var,self.cb11_var,self.cb12_var,self.cb13_var,self.cb14_var,self.cb15_var,self.cb16_var,self.cb18_var]
		
		self.box_list = [self.cb3,self.cb4,self.cb5,self.cb6,self.cb7,self.cb8,self.cb9,self.cb10,self.cb11,self.cb12,self.cb13,self.cb14,self.cb15,self.cb16,self.cb18]
		
		self.cb_all = tk.Button(self.checkboxframe, text = "  Select All  ",justify = tk.LEFT)
		self.cb_all.grid(row=1, column = 0)
		self.cb_all.bind("<Button-1>", self.cb_all_Click)

		self.cb_none = tk.Button(self.checkboxframe, text = "Select None")
		self.cb_none.grid(row=2, column = 0)
		self.cb_none.bind("<Button-1>", self.cb_none_Click)

				
		#This creates the list of instructions.	 There may be a better way to do this...
		self.instruct = tk.Label(self.labelframe2, height = "9", width = "45", justify = tk.LEFT, padx = "4", pady= "6", anchor = tk.W, font = helv14, text ="1. Select desired indices, types of words to analyze,\n    and whether negation control is desired.\n2. Choose the input folder (where your files are).\n3. Select the folder you want the output file to go in.\n4. Give a name to the output file.\n5. Press the 'Process Texts' button.\n6. Please reference the SEANCE Index Spreadsheet\n    and the SEANCE help file (www.kristopherkyle.com)\n    for further assistance in interpreting the output.")
		self.instruct.pack()
				
		#Creates Label Frame for Data Input area
		self.secondframe= tk.LabelFrame(self.myContainer1, text= "Data Input", background = color)
		self.secondframe.pack(expand=tk.TRUE) 
		#This Places the first button under the instructions.
		self.button1 = tk.Button(self.secondframe)
		self.button1.configure(text= "Select Input Folder")
		self.button1.pack()
		
		#This tells the button what to do when clicked.	 Currently, only a left-click
		#makes the button do anything (e.g. <Button-1>). The second argument is a "def"
		#That is defined later in the program.
		self.button1.bind("<Button-1>", self.button1Click)
		
		#Creates default dirname so if statement in Process Texts can check to see
		#if a directory name has been chosen
		self.dirname = ""
		
		#This creates a label for the first program input (Input Directory)
		self.inputdirlabel =tk.LabelFrame(self.secondframe, height = "1", width= "45", padx = "4", text = "Your selected input folder:", background = color)
		self.inputdirlabel.pack()
		
		#Creates label that informs user which directory has been chosen
		directoryprompt = "(No Folder Chosen)"
		self.inputdirchosen = tk.Label(self.inputdirlabel, height= "1", width= "44", justify=tk.LEFT, padx = "4", anchor = tk.W, font= helv14, text = directoryprompt)
		self.inputdirchosen.pack()
		
		#This creates the Output Directory button.
		self.button2 = tk.Button(self.secondframe)
		self.button2["text"]= "Choose Output Filename"
		#This tells the button what to do if clicked.
		self.button2.bind("<Button-1>", self.button2Click)
		self.button2.pack()
		self.outdirname = ""
		
		#Creates a label for the second program input (Output Directory)
		self.outputdirlabel = tk.LabelFrame(self.secondframe, height = "1", width= "45", padx = "4", text = "Your selected filename:", background = color)
		self.outputdirlabel.pack()
		
		#Creates a label that informs sure which directory has been chosen
		#outdirectoryprompt = "(No output Folder Chosen)"
		outdirectoryprompt = "(No Output Filename Chosen)"
		self.input2 = ""
		self.outputdirchosen = tk.Label(self.outputdirlabel, height= "1", width= "44", justify=tk.LEFT, padx = "4", anchor = tk.W, font= helv14, text = outdirectoryprompt)
		self.outputdirchosen.pack()
				
		self.BottomSpace= tk.LabelFrame(self.myContainer1, text = "Run Program", background = color)
		self.BottomSpace.pack()

		self.button3= tk.Button(self.BottomSpace)
		self.button3["text"] = "Process Texts"
		self.button3.bind("<Button-1>", self.runprogram)
		self.button3.pack()
		
		self.progresslabelframe = tk.LabelFrame(self.BottomSpace, text= "Program Status", background = color)
		self.progresslabelframe.pack(expand= tk.TRUE)
		
		#progress = "...Waiting for Data to Process"
		self.progress= tk.Label(self.progresslabelframe, height= "1", width= "45", justify=tk.LEFT, padx = "4", anchor = tk.W, font= helv14, text=progress)
		self.progress.pack()
		
		self.poll(self.progress)
		
	def cb_all_Click(self, event):
		for items in self.box_list[:8]:
			items.select()
		self.cb15.select()

	def cb_none_Click(self, event):
		for items in self.box_list[:8]:
			items.deselect()
		self.box_list[12].deselect()
	
	def clicker(self, event):
		item = self.box_list[12]
		item.select()	
		
	def entry1Return(self,event):
		input= self.entry1.get()
		self.input2 = input + ".csv"
		self.filechosenchosen.config(text = self.input2)
		self.filechosenchosen.update_idletasks()
	
	#Following is an example of how we can update the information from users...
	def button1Click(self, event):
		self.dirname = tkinter.filedialog.askdirectory(parent=root,title='Please select a directory')
		print(self.dirname)
		if self.dirname == "":
			self.displayinputtext = "(No Folder Chosen)"
		else: self.displayinputtext = '.../'+self.dirname.split('/')[-1]
		self.inputdirchosen.config(text = self.displayinputtext)
		

	def button2Click(self, event):
		self.outdirname = tkinter.filedialog.asksaveasfilename(parent=root, defaultextension = ".csv", initialfile = "results",title='Choose Output Filename')
		print(self.outdirname)
		if self.outdirname == "":
			self.displayoutputtext = "(No Output Filename Chosen)"
		else: self.displayoutputtext = '.../' + self.outdirname.split('/')[-1]
		self.outputdirchosen.config(text = self.displayoutputtext)
		
	def runprogram(self, event):
		self.poll(self.progress)
		import tkinter.messagebox
		if self.dirname is "":
			tkinter.messagebox.showinfo("Supply Information", "Choose Input Directory")
		if self.outdirname is "":
			tkinter.messagebox.showinfo("Choose Output Filename", "Choose Output Filename")
		if self.dirname is not "" and self.outdirname is not "":
	
			dataQueue.put("Starting Sentiment Tool...")
			start_thread(main, self.dirname, self.outdirname, self.var_list)

	def poll(self, function):
		
		self.myParent.after(10, self.poll, function)
		try:
			function.config(text = dataQueue.get(block=False))
			
			#root.update_idletasks()
		except queue.Empty:
			pass

def main(indir, outfile,var_list):		

		if var_list[5].get() == 1 or var_list[15].get() == 1: #if vader box  or component scores checked:
			from data_files.vaderSentiment import SentimentIntensityAnalyzer
		
		def dict_builder(database_file, number): #builds dictionaries from database files
			dict ={}

			for entries in database_file:  
				if entries[0] is '#': #ignores first line which contains category information
					continue
			
				entries = entries.split("\t")
				dict[entries[0]]=entries[number]
	
			return dict
	
		#This function deals with denominator issues that can kill the program:
		def safe_divide(numerator, denominator):
			if denominator == 0:
				index = 0
			else: index = numerator/denominator
			return index

		#this is almost the same as safe_divide, but creates proportions
		def proportion(numerator,denominator):
			if denominator == 0 and numerator == 0:
				index = 0
			elif denominator == 0:
				index = 1
			else: index = numerator/denominator
			return index
		
		def component_dicter(folder): #takes a folder of component files, turns it into dict
			dict = {}
			file_list = glob.glob(folder)
			for files in file_list:
				list = []
				comp = open(files,"rU").read().split("\n")
				for line in comp:
					list.append(line.split("\t"))
				if system !="W":
					key = files.split("/")[-1]
				else:
					key = files.split("\\")[-1]
				dict[key]=list
			
			return dict
				
		
		#function for dictionary
		def regex_count(dict, key, text, list, pos=None):
			counter = 0
			nwords = len(text.split())#text length
			##print pos, nwords
			for item in dict[key]:
				if item == "":
					continue #if it is empty, ignore it. Lots of empty keys
				#For wildcards and case
				if item[-1] == '*':#if item in list ends in wildcard
					my_regex = r'\b' + item[0:-1] + r'.*?\b'
					counter+= len(re.findall(my_regex, text, re.IGNORECASE))
				else:
					my_regex = r'\b' + item + r'\b'
					counter+= len(re.findall(my_regex, text, re.IGNORECASE))
			if list == "yes":
				variable_list.append(safe_divide(counter,nwords))
				if pos == None:
					header_list.append(key)
				else: header_list.append(key+pos)
			
			else: return safe_divide(counter,nwords)

		def DataDict_counter(in_text, data_dict,number,header,list):
			counter = 0
			sum_counter = 0
			nwords = len(in_text)
	
			for word in in_text:
				if word in data_dict:
					counter+=1
					sum_counter+=float(data_dict[word])
				else:
					if word in lemma_dict and lemma_dict[word] in data_dict:
						counter+=1
						sum_counter+=float(data_dict[lemma_dict[word]])
			if list == "yes":
				if number == 0: variable_list.append(safe_divide(sum_counter,counter))
				if number == 1: variable_list.append(safe_divide(sum_counter,nwords))
				header_list.append(header)
			else:
				if number == 0: variable=safe_divide(sum_counter,counter)
				if number == 1: variable=safe_divide(sum_counter,nwords)
				
				return variable

		def ListDict_counter(list_dict,key,in_text,list,pos=None):
			counter = 0
			nwords = len(in_text)
	
			for word in in_text:
				if word in list_dict[key]:
					counter+=1
				else:
					if word in lemma_dict and lemma_dict[word] in list_dict[key]:
						counter+=1
			if list == "yes":
				variable_list.append(safe_divide(counter,nwords))
				if pos == None:
					if "NRC" in key:
						key = key.replace("NRC","EmoLex")
					header_list.append(key)
				else: 
					if "NRC" in key:
						key = key.replace("NRC","EmoLex")
					header_list.append(key+pos)
			else:
				return safe_divide(counter,nwords)
				
		def Ngram_DataDict_counter(in_text, data_dict,header,list): #replaces Sentic Count
			counter = 0
			nwords = len(in_text)
			position = 0
			denominator = 0
			
			def single_count(word):
				key = 0
				if word in data_dict:
					key=1
				elif word in lemma_dict and lemma_dict[word] in data_dict:
						key =2
				return key
			
			def ngram_count(gram,n):
				yes = 0
				if gram in data_dict:
					yes +=n
				return yes
				
			for item in in_text:
				#This section ensures the text (or remaining portion of the text) is long enough to look for five-grams, etc.
				if position > len(in_text)-1: continue
				word = in_text[position]
				if len(in_text[position:]) < 2:
					if single_count(word) == 1:
						counter+=float(data_dict[word])
						denominator+=1
						position+=1
					elif single_count(word) == 2:
						counter+=float(data_dict[lemma_dict[word]])
						denominator+=1
						position+=1						
					else: position+=1
				
				bigram = " ".join(in_text[position:position +1])
				if len(in_text[position:]) < 3:
					yes = ngram_count(bigram,2)
					if yes > 0:
						counter+=float(data_dict[bigram])
						denominator+=1
						position+=yes
						continue
					if single_count(word) == 1:
						counter+=float(data_dict[word])
						denominator+=1
						position+=1
					elif single_count(word) == 2:
						counter+=float(data_dict[lemma_dict[word]])
						denominator+=1
						position+=1	
					else: position+=1
									
				trigram = " ".join(in_text[position:position +2])
				if len(in_text[position:]) < 4:
					yes = ngram_count(trigram,3)
					if yes > 0:
						counter+=float(data_dict[trigram])
						denominator+=1
						position+=yes
						continue
					yes = ngram_count(bigram,2)
					if yes > 0:
						counter+=float(data_dict[bigram])
						denominator+=1
						position+=yes
						continue
					if single_count(word) == 1:
						counter+=float(data_dict[word])
						denominator+=1
						position+=1
					elif single_count(word) == 2:
						counter+=float(data_dict[lemma_dict[word]])
						denominator+=1
						position+=1	
					else: position+=1
										
				quadgram = " ".join(in_text[position:position +3])
				if len(in_text[position:]) < 5:
					yes = ngram_count(quadgram,4)
					if yes > 0:
						counter+=float(data_dict[quadgram])
						denominator+=1
						position+=yes
						continue
					yes = ngram_count(trigram,3)
					if yes > 0:
						counter+=float(data_dict[trigram])
						denominator+=1
						position+=yes
						continue
					yes = ngram_count(bigram,2)
					if yes > 0:
						counter+=float(data_dict[bigram])
						denominator+=1
						position+=yes
						continue
					if single_count(word) == 1:
						counter+=float(data_dict[word])
						denominator+=1
						position+=1
					elif single_count(word) == 2:
						counter+=float(data_dict[lemma_dict[word]])
						denominator+=1
						position+=1	
					else: position+=1				
				
				#This functions on most of the text. It checks for five-grams. If none, quad-grams, etc.
				fivegram = " ".join(in_text[position:position +4])
				if len(in_text[position:]) > 4:
					yes = ngram_count(fivegram,4)
					if yes > 0:
						counter+=float(data_dict[fivegram])
						denominator+=1
						position+=yes
						continue
					yes = ngram_count(quadgram,4)
					if yes > 0:
						counter+=float(data_dict[quadgram])
						denominator+=1
						position+=yes
						continue
					yes = ngram_count(trigram,3)
					if yes > 0:
						counter+=float(data_dict[trigram])
						denominator+=1
						position+=yes
						continue
					yes = ngram_count(bigram,2)
					if yes > 0:
						counter+=float(data_dict[bigram])
						denominator+=1
						position+=yes
						continue
					if single_count(word) == 1:
						counter+=float(data_dict[word])
						denominator+=1
						position+=1
					elif single_count(word) == 2:
						counter+=float(data_dict[lemma_dict[word]])
						denominator+=1
						position+=1	
					else: position+=1
			
			if list == "yes":					
				variable_list.append(safe_divide(counter,denominator))
				header_list.append(header)
			else:
				return safe_divide(counter,denominator)

		inputfile = indir + "/*.txt"
		filenames = glob.glob(inputfile)

		outf=open(outfile, "w")
		
		print("Importing databases...\n")

		affect_list = open(resource_path('data_files/affective_list.txt'), 'rU').read()

		#this cleans up the affect list
		affect_list = re.sub('\t\t', '', affect_list)#makes all double tabs nothing
		affect_list = re.sub('\t\n', '\n', affect_list)#similar all the way down
		affect_list = re.sub(' \t', '\t', affect_list)
		affect_list = re.sub(' \n', '\n', affect_list)

		affect_list = affect_list.split('\n')
		affect_dict = {}

		punctuation = (".","!","?",",", ":",";", "'",'"')

		for line in affect_list:
			entries = line.split("\t") #splits entries in .csv file at tab
			affect_dict[entries[0]] = entries[1:]

		GI_list = open(resource_path('data_files/inquirerbasic.txt'), 'rU').readlines()
		GI_dict={}

		for line in GI_list:
			entries = line.split("\t") #splits entries in .csv file at tab
	
			GI_dict[entries[0]] = set(entries[1:])
			##print entries[0]
			
		#defines program files
		lemma_list = open(resource_path('data_files/e_lemma_py_format_lower.txt'), 'rU').readlines()
		anew_list = open(resource_path('data_files/affective_norms.txt'), 'rU').readlines()
		sentic_list = open(resource_path('data_files/senticnet_data.txt'), 'rU').readlines()
		lu_hui_positive = open(resource_path('data_files/positive_words.txt'), 'rU').read().split("\n")
		lu_hui_negative = open(resource_path('data_files/negative_words.txt'), 'rU').read().split("\n")
		
		components_2 = component_dicter(resource_path('components/C*.txt'))
		
			
		#creates dictionary for lemma list
		lemma_dict={}

		#Creates lemma dictionary, which may or may not be necessary with this database!

		#print "Compiling Lemma Dict...\n"
		for line in lemma_list:
			#ignores first lines
			if line[0] is '#':
				continue
			#allows use of each line:
			entries=line.split()
			#creates dictionary entry for each word in line:
			for word in entries:
				lemma_dict[word] = entries[0]
				##print lemma_dict

		#Creates a dictionaries with word:score pairings:

		valence = dict_builder(anew_list, 1)
		arousal = dict_builder(anew_list, 2)
		dominance = dict_builder(anew_list, 3)

		pleasantness = dict_builder(sentic_list, 1)
		attention = dict_builder(sentic_list, 2)
		sensitivity = dict_builder(sentic_list, 3)
		aptitude = dict_builder(sentic_list, 4)
		polarity = dict_builder(sentic_list, 5)

		def run_galc(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			if var != None:
				text = " ".join(text)

			
			regex_count(affect_dict,'Admiration/Awe_GALC',text,"yes",pos)
			regex_count(affect_dict,'Amusement_GALC',text,"yes",pos)
			regex_count(affect_dict,'Anger_GALC',text,"yes",pos)
			regex_count(affect_dict,'Anxiety_GALC',text,"yes",pos)
			regex_count(affect_dict,'Beingtouched_GALC',text,"yes",pos)
			regex_count(affect_dict,'Boredom_GALC',text,"yes",pos)
			regex_count(affect_dict,'Compassion_GALC',text,"yes",pos)
			regex_count(affect_dict,'Contempt_GALC',text,"yes",pos)
			regex_count(affect_dict,'Contentment_GALC',text,"yes",pos)
			regex_count(affect_dict,'Desperation_GALC',text,"yes",pos)
			regex_count(affect_dict,'Disappointment_GALC',text,"yes",pos)
			regex_count(affect_dict,'Disgust_GALC',text,"yes",pos)
			regex_count(affect_dict,'Dissatisfaction_GALC',text,"yes",pos)
			regex_count(affect_dict,'Envy_GALC',text,"yes",pos)
			regex_count(affect_dict,'Fear_GALC',text,"yes",pos)
			regex_count(affect_dict,'Feelinglove_GALC',text,"yes",pos)
			regex_count(affect_dict,'Gratitude_GALC',text,"yes",pos)
			regex_count(affect_dict,'Guilt_GALC',text,"yes",pos)
			regex_count(affect_dict,'Happiness_GALC',text,"yes",pos)
			regex_count(affect_dict,'Hatred_GALC',text,"yes",pos)
			regex_count(affect_dict,'Hope_GALC',text,"yes",pos)
			regex_count(affect_dict,'Humility_GALC',text,"yes",pos)
			regex_count(affect_dict,'Interest/Enthusiasm_GALC',text,"yes",pos)
			regex_count(affect_dict,'Irritation_GALC',text,"yes",pos)
			regex_count(affect_dict,'Jealousy_GALC',text,"yes",pos)
			regex_count(affect_dict,'Joy_GALC',text,"yes",pos)
			regex_count(affect_dict,'Longing_GALC',text,"yes",pos)
			regex_count(affect_dict,'Lust_GALC',text,"yes",pos)
			regex_count(affect_dict,'Pleasure/Enjoyment_GALC',text,"yes",pos)
			regex_count(affect_dict,'Pride_GALC',text,"yes",pos)
			regex_count(affect_dict,'Relaxation/Serenity_GALC',text,"yes",pos)
			regex_count(affect_dict,'Relief_GALC',text,"yes",pos)
			regex_count(affect_dict,'Sadness_GALC',text,"yes",pos)
			regex_count(affect_dict,'Shame_GALC',text,"yes",pos)
			regex_count(affect_dict,'Surprise_GALC',text,"yes",pos)
			regex_count(affect_dict,'Tension/Stress_GALC',text,"yes",pos)
			regex_count(affect_dict,'Positive_GALC',text,"yes",pos)
			regex_count(affect_dict,'Negative_GALC',text,"yes",pos)

		def run_nrc(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			
			ListDict_counter(GI_dict,'Anger_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Anticipation_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Disgust_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Fear_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Joy_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Negative_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Positive_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Sadness_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Surprise_NRC',text,"yes",pos)
			ListDict_counter(GI_dict,'Trust_NRC',text,"yes",pos)		

		def run_anew(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			
			DataDict_counter(text, valence,0,"Valence"+pos,"yes")#valence_average = 
			DataDict_counter(text, valence,1,"Valence_nwords"+pos,"yes")#valence_average_nwords = 
			DataDict_counter(text, arousal,0,"Arousal"+pos,"yes")#arousal_average = 
			DataDict_counter(text, arousal,1,"Arousal_nwords"+pos,"yes")#arousal_average_nwords = 
			DataDict_counter(text, dominance,0,"Dominance"+pos,"yes")#dominance_average = 
			DataDict_counter(text, dominance,1,"Dominance_nwords"+pos,"yes")#dominance_average_nwords = 

		def run_sentic(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			
			Ngram_DataDict_counter(text, pleasantness,"pleasantness"+pos,"yes")#norm_pleasant = 
			Ngram_DataDict_counter(text, attention,"attention"+pos,"yes")#norm_attention = 
			Ngram_DataDict_counter(text, sensitivity,"sensitivity"+pos,"yes")#norm_sensitivity = 
			Ngram_DataDict_counter(text, aptitude,"aptitude"+pos,"yes")#norm_aptitude = 
			Ngram_DataDict_counter(text, polarity,"polarity"+pos,"yes")#norm_polarity = 

		def run_vader(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			
			if var != None:
				text = " ".join(text)
			try:
				analyzer = SentimentIntensityAnalyzer()
				vs = analyzer.polarity_scores(text)
				variable_list.append(vs['neg']) #vader_negative #relies on vader lexicon
				variable_list.append(vs['neu']) #vader_neutral #relies on vader lexicon
				variable_list.append(vs['pos'])#vader_positive #relies on vader lexicon
				variable_list.append(vs['compound'])#vader_compound = #vader lexicon and rules. most accurate	
			except UnicodeEncodeError:
				variable_list.append("Error")
				variable_list.append("Error")
				variable_list.append("Error")
				variable_list.append("Error")
			
			vader_header = ["vader_negative"+pos,"vader_neutral"+pos,"vader_positive"+pos,"vader_compound"+pos]
			for items in vader_header: header_list.append(items)
			
		def run_lu_hui(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			
			lu_hui_positive_count = 0
			lu_hui_negative_count = 0
			lu_hui_pos_neg_count = 0

			for word in text:

				if word in lu_hui_positive:
					lu_hui_positive_count += 1
					lu_hui_pos_neg_count += 1

				if word in lu_hui_negative:
					lu_hui_negative_count += 1
					lu_hui_pos_neg_count += 1

			variable_list.append(safe_divide(lu_hui_positive_count,lu_hui_pos_neg_count))#lu_hui_pos_perc = 
			variable_list.append(safe_divide(lu_hui_negative_count,lu_hui_pos_neg_count))#lu_hui_neg_perc = 
			variable_list.append(safe_divide(lu_hui_positive_count,nwords))#lu_hui_pos_nwords = 
			variable_list.append(safe_divide(lu_hui_negative_count,nwords))#lu_hui_neg_nwords = 
			variable_list.append(proportion(lu_hui_positive_count,lu_hui_negative_count))#lu_hui_prop = 
			lu_hui_header = ["hu_liu_pos_perc"+pos,"hu_liu_neg_perc"+pos,"hu_liu_pos_nwords"+pos,"hu_liu_neg_nwords"+pos,"hu_liu_prop"+pos]
			for items in lu_hui_header: header_list.append(items)

		def run_gi(text,var=None):
			if var == None:
				pos = ""
			else: pos = var
			
			ListDict_counter(GI_dict,"Positiv_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Negativ_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Pstv_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Affil_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ngtv_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Hostile_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Strong_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Power_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Weak_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Submit_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Active_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Passive_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Pleasur_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Pain_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Feel_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Arousal_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Emot_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Virtue_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Vice_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ovrst_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Undrst_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Academ_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Doctrin_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Econ_2_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Exch_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Econ_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Exprsv_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Legal_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Milit_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Polit_2_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Polit_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Relig_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Role_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Coll_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Work_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ritual_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Socrel_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Race_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Kin_2_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Male_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Female_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Nonadlt_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Hu_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ani_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Place_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Social_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Region_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Route_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Aquatic_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Land_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Sky_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Object_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Tool_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Food_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Vehicle_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Bldgpt_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Comnobj_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Natobj_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Bodypt_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Comform_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Com_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Say_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Need_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Goal_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Try_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Means_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Persist_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Complet_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Fail_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Natrpro_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Begin_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Vary_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Increas_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Decreas_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Finish_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Stay_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Rise_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Exert_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Fetch_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Travel_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Fall_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Think_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Know_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Causal_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ought_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Perceiv_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Compare_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Eval_2_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Eval_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Solve_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Abs_2_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Abs_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Quality_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Quan_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Numb_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ord_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Card_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Freq_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Dist_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Time_2_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Time_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Space_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Pos_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Dim_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Rel_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Color_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Self_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Our_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"You_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Name_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Yes_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"No_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Negate_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Intrj_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Iav_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Dav_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Sv_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Ipadj_GI",text,"yes",pos)
			ListDict_counter(GI_dict,"Indadj_GI",text,"yes",pos)

		def run_lasswell(text,var=None):
			if var == None:
				pos = ""
			else: pos = var

			ListDict_counter(GI_dict,"Powgain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powloss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powends_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powaren_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powcon_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powcoop_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powaupt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powpt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powdoct_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powauth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powoth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Powtot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rcethic_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rcrelig_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rcgain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rcloss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rcends_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rctot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rspgain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rsploss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rspoth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Rsptot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Affgain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Affloss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Affpt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Affoth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Afftot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wltpt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlttran_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wltoth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlttot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlbgain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlbloss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlbphys_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlbpsyc_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlbpt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Wlbtot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Enlgain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Enlloss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Enlends_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Enlpt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Enloth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Enltot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Sklasth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Sklpt_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Skloth_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Skltot_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Trngain_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Trnloss_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Tranlw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Meanslw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Endslw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Arenalw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Ptlw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Nation_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Anomie_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Negaff_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Posaff_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Surelw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"If_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Notlw_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"Timespc_Lasswell",text,"yes",pos)
			ListDict_counter(GI_dict,"formlw_Lasswell",text,"yes",pos)

		def component_count(component,header):
			output = 0
			item_number = 0
			
			for item in component:
				item_number +=1
				number = "blank"
				variable = item[0]
				
				cut_var = variable.split("_")
				eigen = float(item[1])
				
				if len(cut_var) > 1:
					if "2" in variable:
						target_name = "_".join(cut_var[0:3])
					else: target_name = "_".join(cut_var[0:2]) #first part of name to identify list
				else:target_name = cut_var[0]
				
				if "neg_3" in variable: #check for negation
					
					if "_nouns" in variable:
						input = noun_text_neg_3
					elif "_verbs" in variable:
						input = verb_text_neg_3
					elif "_adjectives" in variable:
						input = adjective_text_neg_3
					elif "_adverbs" in variable:
						input = adverb_text_neg_3
					else:
						input = neg_3_text
				
				else:
					if "_nouns" in variable:
						input = noun_text
					elif "_verbs" in variable:
						input = verb_text
					elif "_adjectives" in variable:
						input = adjective_text
					elif "_adverbs" in variable:
						input = adverb_text
					else:
						input = text_2
											
				if "_GI" in variable or "_Lasswell" in variable or "_NRC" in variable:
					number = ListDict_counter(GI_dict,target_name,input,"no")
				
				if "_GALC" in variable:
					input = " ".join(input)
					number = regex_count(affect_dict,target_name,input,"no")
				
				#ANEW
				if "Valence" in variable or "Arousal" in variable or "Dominance" in variable:
					if len(cut_var) > 1 and cut_var[1] == "nwords":
						if cut_var[0] == "Valence":
							number = DataDict_counter(input, valence,1,"","")
						if cut_var[0] == "Arousal":
							number = DataDict_counter(input, arousal,1,"","")
						if cut_var[0] == "Dominance":
							number = DataDict_counter(input, dominance,1,"","")

					else:
						if cut_var[0] == "Valence":
							number = DataDict_counter(input, valence,0,"","")
						if cut_var[0] == "Arousal":
							number = DataDict_counter(input, arousal,0,"","")
						if cut_var[0] == "Dominance":
							number = DataDict_counter(input, dominance,0,"","")
						
				#SENTIC
				if "pleasantness" in variable:
					#Ngram_DataDict_counter(in_text, data_dict,header,list)
					number = Ngram_DataDict_counter(input, pleasantness,"pleasantness","no")
				if "attention" in variable:
					number = Ngram_DataDict_counter(input, attention,"attention","no")
				if "sensitivity" in variable:
					number = Ngram_DataDict_counter(input, sensitivity,"sensitivity","no")
				if "aptitude" in variable:
					number = Ngram_DataDict_counter(input, aptitude,"aptitude","no")
				if "polarity" in variable:
					number = Ngram_DataDict_counter(input, polarity,"polarity","no") 
				
				#Vader
				if "vader" in variable:
					input = " ".join(input)
					
					try:
						analyzer = SentimentIntensityAnalyzer()
						vs = analyzer.polarity_scores(text)

						if "vader_negative" in variable:
							number = vs['neg']
						if "vader_neutral" in variable:
							number = vs['neu']
						if "vader_positive" in variable:
							number = vs['pos']
						if "vader_compound" in variable:
							number = vs['compound']				
					
					except UnicodeEncodeError:
						number = 0 #fix this!!!
				
				
				#LuHui
				
				if "lu_hui" in variable:
					lu_hui_positive_count = 0
					lu_hui_negative_count = 0
					lu_hui_pos_neg_count = 0

					for word in input:

						if word in lu_hui_positive:
							lu_hui_positive_count += 1
							lu_hui_pos_neg_count += 1

						if word in lu_hui_negative:
							lu_hui_negative_count += 1
							lu_hui_pos_neg_count += 1
					
					if "lu_hui_pos_perc" in variable:
						number = safe_divide(lu_hui_positive_count,lu_hui_pos_neg_count)
					if "lu_hui_neg_perc" in variable:
						number = safe_divide(lu_hui_negative_count,lu_hui_pos_neg_count)
					if "lu_hui_pos_nwords" in variable:
						number = safe_divide(lu_hui_positive_count,nwords)
					if "lu_hui_neg_nwords" in variable:
						number = safe_divide(lu_hui_negative_count,nwords) 
					if "lu_hui_prop" in variable:
						number = proportion(lu_hui_positive_count,lu_hui_negative_count)
				
				output += (number*eigen)
			
			variable_list.append(output)
			header_list.append(header)
		
		if var_list[9].get() == 1 or var_list[10].get() == 1 or var_list[11].get() == 1 or var_list[12].get() == 1 or var_list[15].get() == 1:
			dataQueue.put("Loading spaCy")
			root.update_idletasks()
			import spacy
			from spacy.util import set_data_path
			set_data_path(resource_path('en_core_web_sm'))
			nlp = spacy.load(resource_path('en_core_web_sm'))				
	
####Beginning of file iteration#######
		file_counter = 1
		nfiles = len(filenames)
		for filename in filenames:
			variable_list = []
			header_list = ["filename","nwords"]
			
			print(filename)
			filename1 = ("Processing: " + str(file_counter) + " of " + str(nfiles) + " files")
			
			if system != "W":
				filename_2 = filename.split("/")[-1]
			else:
				filename_2 = filename.split("\\")[-1]
			
			dataQueue.put(filename1)
			root.update_idletasks()
			
			
			Text= open(filename, 'r',errors = 'ignore').read()
			#the text has educated quotes and we want straight quotes. 
			text = re.sub("‘", "'", Text) #bottom heavy educated quote replaced by straight quotes
			text= re.sub("’", "'", text) #top heavy educated quote replaced by straight quotes
	
			nwords = len(text.split())
			
			for word in text:
				if word[-1] in punctuation:
					word = word[:-1]
	
			pre_text= open(filename, 'r',errors = 'ignore').read().lower().split()
			text_2 = []
			#Holder structure for lemmatized text:
			lemma_text=[]
			neg_3_text = []
			neg_list = ["aint", "arent", "cannot", "cant", "couldnt", "darent", "didnt", "doesnt",
					  "ain't", "aren't", "can't", "couldn't", "daren't", "didn't", "doesn't",
					  "dont", "hadnt", "hasnt", "havent", "isnt", "mightnt", "mustnt", "neither",
					  "don't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "mustn't",
					  "neednt", "needn't", "never", "none", "nope", "nor", "not", "nothing", "nowhere", 
					  "oughtnt", "shant", "shouldnt", "uhuh", "wasnt", "werent",
					  "oughtn't", "shan't", "shouldn't", "uh-uh", "wasn't", "weren't",  
					  "without", "wont", "wouldnt", "won't", "wouldn't", "rarely", "seldom", "despite"]
			neg_list_2 = ["n't", "aint", "arent", "cannot", "cant", "couldnt", "darent", "didnt", "doesnt",
					  "ain't", "aren't", "can't", "couldn't", "daren't", "didn't", "doesn't",
					  "dont", "hadnt", "hasnt", "havent", "isnt", "mightnt", "mustnt", "neither",
					  "don't", "hadn't", "hasn't", "haven't", "isn't", "mightn't", "mustn't",
					  "neednt", "needn't", "never", "none", "nope", "nor", "not", "nothing", "nowhere", 
					  "oughtnt", "shant", "shouldnt", "uhuh", "wasnt", "werent",
					  "oughtn't", "shan't", "shouldn't", "uh-uh", "wasn't", "weren't",  
					  "without", "wont", "wouldnt", "won't", "wouldn't", "rarely", "seldom", "despite"]



			for word in pre_text: #gets rid of punctuation attached to words
				if len(word) < 1: #new in 1.4
					continue
				if len(word)==1 and word in punctuation:
					continue
				if word[-1] in punctuation:
					word = word[:-1]
				if word[0] in punctuation:
					word = word[1:]					
				#Creates lemmatized text:
				if word in lemma_dict:
					lemma_text.append(lemma_dict[word])
				else:
					lemma_text.append(word)
				text_2.append(word)

			#####negation text maker####
			
			neg_check = []
			for items in text_2:
				neg_check.append(items)
				if len(neg_check)>4:
					neg_check = neg_check[1:]
				checker = 0
				##print neg_check
				for items in neg_check:
					if items in neg_list:
						checker+=1
				if checker > 0:
					continue
				else: neg_3_text.append(items)
			
			###end negation text maker###
			
				
			### Begin Creation of POS Lists: ###
			if var_list[9].get() == 1 or var_list[10].get() == 1 or var_list[11].get() == 1 or var_list[12].get() == 1 or var_list[15].get() == 1:
			
				noun_tags = "NN NNS NNP NNPS".split(" ") #consider whether to identify gerunds
				adjectives = "JJ JJR JJS".split(" ")
				verbs = "VB VBZ VBP VBD VBN VBG".split(" ")
				adverbs = ["RB"]
				pronouns = ["PRP", "PRP$"]
				pronoun_dict = {"me":"i","him":"he","her":"she"}

				pos_word_list = []
				pos_lemma_list = []
			
				noun_text = []
				noun_lemma_list = []
				adjective_text = []
				adjective_lemma_list = []
				verb_text = []
				verb_lemma_list = []
				adverb_text = []
				adverb_lemma_list = []

				noun_text_neg_3 = []
				adjective_text_neg_3 = []
				verb_text_neg_3 = []
				adverb_text_neg_3 = []
				
				tagged_text = nlp(text)
				
				for token in tagged_text:
					if token.tag_ in punctuation:
						continue
					
					if token.tag_ in pronouns:
						if token.text.lower() in pronoun_dict:
							lemma_form = pronoun_dict[token.text.lower()]
						else:
							lemma_form = token.text.lower()
					else:
						lemma_form = token.lemma_.lower()
					
					pos_word_list.append(token.text.lower())
					pos_lemma_list.append(lemma_form)
					
					if token.tag_ in noun_tags:
						noun_text.append(token.text.lower())
						noun_lemma_list.append(lemma_form)
					if token.tag_ in adjectives:
						adjective_text.append(token.text.lower())
						adjective_lemma_list.append(lemma_form)
					if token.tag_ in verbs:
						verb_text.append(token.text.lower())
						verb_lemma_list.append(lemma_form)
					if token.tag_ in adverbs:
						adverb_text.append(token.text.lower())
						adverb_lemma_list.append(lemma_form)							
				##print pos_word_list
				
				### for negation check counts ###
				neg_check = []
				for token in tagged_text:
					if token.tag_ in punctuation:
						continue
					### the following checks for negation in the span of 3 words to the left ###
					neg_check.append(token.text.lower())
					##print neg_check
					if len(neg_check)>4:
						neg_check = neg_check[1:]
					neg_checker = 0
					for items in neg_check:
						if items in neg_list_2:
							neg_checker +=1
					if neg_checker > 0:
						continue
					### if the negation check is clear, we go on to add the words ###	
					if token.tag_ in noun_tags:
						noun_text_neg_3.append(token.text.lower())
					if token.tag_ in adjectives:
						adjective_text_neg_3.append(token.text.lower())
					if token.tag_ in verbs:
						verb_text_neg_3.append(token.text.lower())
					if token.tag_ in adverbs:
						adverb_text_neg_3.append(token.text.lower())
			
			### end creation of POS lists ###
			
			variable_list = []
			

			#### Normal Program ####
			if var_list[1].get() == 1 and var_list[13].get() == 1: run_galc(text)
			if var_list[2].get() == 1 and var_list[13].get() == 1: run_nrc(text_2)
			if var_list[3].get() == 1 and var_list[13].get() == 1: run_anew(text_2)
			if var_list[4].get() == 1 and var_list[13].get() == 1: run_sentic(text_2)
			if var_list[5].get() == 1 and var_list[13].get() == 1: run_vader(Text)
			if var_list[6].get() == 1 and var_list[13].get() == 1: run_lu_hui(text_2)
			if var_list[7].get() == 1 and var_list[13].get() == 1: run_gi(text_2)
			if var_list[8].get() == 1 and var_list[13].get() == 1: run_lasswell(text_2)
			
			#### Normal Program Negation Controlled ####
			if var_list[1].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_galc(neg_3_text,"_neg_3")
			if var_list[2].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_nrc(neg_3_text,"_neg_3")
			if var_list[3].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_anew(neg_3_text,"_neg_3")
			if var_list[4].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_sentic(neg_3_text,"_neg_3")
			#if var_list[5].get() == 1 and var_list[13].get() == 1: run_vader(Text) #Vader already has negation control
			if var_list[6].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_lu_hui(neg_3_text,"_neg_3")
			if var_list[7].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_gi(neg_3_text,"_neg_3")
			if var_list[8].get() == 1 and var_list[13].get() == 1 and var_list[14].get() == 1: run_lasswell(neg_3_text,"_neg_3")

			#### Nouns Only ####			
			if var_list[1].get() == 1 and var_list[9].get() == 1: run_galc(noun_text,"_nouns")
			if var_list[2].get() == 1 and var_list[9].get() == 1: run_nrc(noun_text,"_nouns")
			if var_list[3].get() == 1 and var_list[9].get() == 1: run_anew(noun_text,"_nouns")
			if var_list[4].get() == 1 and var_list[9].get() == 1: run_sentic(noun_text,"_nouns")
			if var_list[5].get() == 1 and var_list[9].get() == 1: run_vader(noun_text,"_nouns")
			if var_list[6].get() == 1 and var_list[9].get() == 1: run_lu_hui(noun_text,"_nouns")
			if var_list[7].get() == 1 and var_list[9].get() == 1: run_gi(noun_text,"_nouns")
			if var_list[8].get() == 1 and var_list[9].get() == 1: run_lasswell(noun_text,"_nouns")
			
			#### Verbs Only ####
			if var_list[1].get() == 1 and var_list[10].get() == 1: run_galc(verb_text,"_verbs")
			if var_list[2].get() == 1 and var_list[10].get() == 1: run_nrc(verb_text,"_verbs")
			if var_list[3].get() == 1 and var_list[10].get() == 1: run_anew(verb_text,"_verbs")
			if var_list[4].get() == 1 and var_list[10].get() == 1: run_sentic(verb_text,"_verbs")
			if var_list[5].get() == 1 and var_list[10].get() == 1: run_vader(verb_text,"_verbs")
			if var_list[6].get() == 1 and var_list[10].get() == 1: run_lu_hui(verb_text,"_verbs")
			if var_list[7].get() == 1 and var_list[10].get() == 1: run_gi(verb_text,"_verbs")
			if var_list[8].get() == 1 and var_list[10].get() == 1: run_lasswell(verb_text,"_verbs")	
						
			#### Adjectives Only ####
			if var_list[1].get() == 1 and var_list[11].get() == 1: run_galc(adjective_text,"_adjectives")
			if var_list[2].get() == 1 and var_list[11].get() == 1: run_nrc(adjective_text,"_adjectives")
			if var_list[3].get() == 1 and var_list[11].get() == 1: run_anew(adjective_text,"_adjectives")
			if var_list[4].get() == 1 and var_list[11].get() == 1: run_sentic(adjective_text,"_adjectives")
			if var_list[5].get() == 1 and var_list[11].get() == 1: run_vader(adjective_text,"_adjectives")
			if var_list[6].get() == 1 and var_list[11].get() == 1: run_lu_hui(adjective_text,"_adjectives")
			if var_list[7].get() == 1 and var_list[11].get() == 1: run_gi(adjective_text,"_adjectives")
			if var_list[8].get() == 1 and var_list[11].get() == 1: run_lasswell(adjective_text,"_adjectives")	
						
			#### Adverbs Only ####
			if var_list[1].get() == 1 and var_list[12].get() == 1: run_galc(adverb_text,"_adverbs")
			if var_list[2].get() == 1 and var_list[12].get() == 1: run_nrc(adverb_text,"_adverbs")
			if var_list[3].get() == 1 and var_list[12].get() == 1: run_anew(adverb_text,"_adverbs")
			if var_list[4].get() == 1 and var_list[12].get() == 1: run_sentic(adverb_text,"_adverbs")
			if var_list[5].get() == 1 and var_list[12].get() == 1: run_vader(adverb_text,"_adverbs")
			if var_list[6].get() == 1 and var_list[12].get() == 1: run_lu_hui(adverb_text,"_adverbs")
			if var_list[7].get() == 1 and var_list[12].get() == 1: run_gi(adverb_text,"_adverbs")
			if var_list[8].get() == 1 and var_list[12].get() == 1: run_lasswell(adverb_text,"_adverbs")	

			#### Nouns Only Negation Checked ####			
			if var_list[1].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_galc(noun_text_neg_3,"_nouns_neg_3")
			if var_list[2].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_nrc(noun_text_neg_3,"_nouns_neg_3")
			if var_list[3].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_anew(noun_text_neg_3,"_nouns_neg_3")
			if var_list[4].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_sentic(noun_text_neg_3,"_nouns_neg_3")
			#if var_list[5].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_vader(noun_text_neg_3,"_nouns_neg_3")
			if var_list[6].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_lu_hui(noun_text_neg_3,"_nouns_neg_3")
			if var_list[7].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_gi(noun_text_neg_3,"_nouns_neg_3")
			if var_list[8].get() == 1 and var_list[9].get() == 1and var_list[14].get() == 1: run_lasswell(noun_text_neg_3,"_nouns_neg_3")
			
			#### Verbs Only Negation Checked ####
			if var_list[1].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_galc(verb_text_neg_3,"_verbs_neg_3")
			if var_list[2].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_nrc(verb_text_neg_3,"_verbs_neg_3")
			if var_list[3].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_anew(verb_text_neg_3,"_verbs_neg_3")
			if var_list[4].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_sentic(verb_text_neg_3,"_verbs_neg_3")
			#if var_list[5].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_vader(verb_text_neg_3,"_verbs_neg_3")
			if var_list[6].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_lu_hui(verb_text_neg_3,"_verbs_neg_3")
			if var_list[7].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_gi(verb_text_neg_3,"_verbs_neg_3")
			if var_list[8].get() == 1 and var_list[10].get() == 1and var_list[14].get() == 1: run_lasswell(verb_text_neg_3,"_verbs_neg_3")	
						
			#### Adjectives Only Negation Checked ####
			if var_list[1].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_galc(adjective_text_neg_3,"_adjectives_neg_3")
			if var_list[2].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_nrc(adjective_text_neg_3,"_adjectives_neg_3")
			if var_list[3].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_anew(adjective_text_neg_3,"_adjectives_neg_3")
			if var_list[4].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_sentic(adjective_text_neg_3,"_adjectives_neg_3")
			#if var_list[5].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_vader(adjective_text_neg_3,"_adjectives_neg_3")
			if var_list[6].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_lu_hui(adjective_text_neg_3,"_adjectives_neg_3")
			if var_list[7].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_gi(adjective_text_neg_3,"_adjectives_neg_3")
			if var_list[8].get() == 1 and var_list[11].get() == 1and var_list[14].get() == 1: run_lasswell(adjective_text_neg_3,"_adjectives_neg_3")	
						
			#### Adverbs Only Negation Checked ####
			if var_list[1].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_galc(adverb_text_neg_3,"_adverbs_neg_3")
			if var_list[2].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_nrc(adverb_text_neg_3,"_adverbs_neg_3")
			if var_list[3].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_anew(adverb_text_neg_3,"_adverbs_neg_3")
			if var_list[4].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_sentic(adverb_text_neg_3,"_adverbs_neg_3")
			#if var_list[5].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_vader(adverb_text_neg_3,"_adverbs_neg_3")
			if var_list[6].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_lu_hui(adverb_text_neg_3,"_adverbs_neg_3")
			if var_list[7].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_gi(adverb_text_neg_3,"_adverbs_neg_3")
			if var_list[8].get() == 1 and var_list[12].get() == 1and var_list[14].get() == 1: run_lasswell(adverb_text_neg_3,"_adverbs_neg_3")
						
			#Second Iteration of Components
			if var_list[15].get() == 1: component_count(components_2["C1.txt"],"negative_adjectives_component")
			if var_list[15].get() == 1: component_count(components_2["C2.txt"],"social_order_component")
			if var_list[15].get() == 1: component_count(components_2["C3.txt"],"action_component")
			if var_list[15].get() == 1: component_count(components_2["C4.txt"],"positive_adjectives_component")
			if var_list[15].get() == 1: component_count(components_2["C5.txt"],"joy_component")
			if var_list[15].get() == 1: component_count(components_2["C6.txt"],"affect_friends_and_family_component")
			if var_list[15].get() == 1: component_count(components_2["C7.txt"],"fear_and_digust_component")
			if var_list[15].get() == 1: component_count(components_2["C8.txt"],"politeness_component")
			if var_list[15].get() == 1: component_count(components_2["C9.txt"],"polarity_nouns_component")
			if var_list[15].get() == 1: component_count(components_2["C10.txt"],"polarity_verbs_component")
			if var_list[15].get() == 1: component_count(components_2["C11.txt"],"virtue_adverbs_component")
			if var_list[15].get() == 1: component_count(components_2["C12.txt"],"positive_nouns_component")
			if var_list[15].get() == 1: component_count(components_2["C13.txt"],"respect_component")
			if var_list[15].get() == 1: component_count(components_2["C14.txt"],"trust_verbs_component")
			if var_list[15].get() == 1: component_count(components_2["C15.txt"],"failure_component")
			if var_list[15].get() == 1: component_count(components_2["C16.txt"],"well_being_component")
			if var_list[15].get() == 1: component_count(components_2["C17.txt"],"economy_component")
			if var_list[15].get() == 1: component_count(components_2["C18.txt"],"certainty_component")
			if var_list[15].get() == 1: component_count(components_2["C19.txt"],"positive_verbs_component")
			if var_list[15].get() == 1: component_count(components_2["C20.txt"],"objects_component")
			

			
			if file_counter == 1:
				header = ",".join(header_list) + "\n"
				outf.write(header)
			
			variable_string_list=[] 
			for items in variable_list:
				variable_string_list.append(str(items))
			string = ",".join(variable_string_list)
			
			file_counter+=1
			#print(file_counter)
			outf.write ('{0}, {1}, {2}\n'
			.format(filename_2,nwords,string))
			
		outf.flush()#flushes out buffer to clean output file
		outf.close()#close output file	

		#Closing Message to let user know that the program did something
		
		finishmessage = ("Processed " + str(nfiles) + " Files")
		dataQueue.put(finishmessage)
		root.update_idletasks()
		if system == "M":
			#self.progress.config(text =finishmessage)
			tkinter.messagebox.showinfo("Finished!", "Your files have been processed by Sentiment Tool!")


if __name__ == '__main__':		
	root = tk.Tk()
	root.wm_title("SEANCE 1.2.0")
	root.configure(background = color)
	root.geometry(geom_size)
	myapp = MyApp(root)
	root.mainloop()
