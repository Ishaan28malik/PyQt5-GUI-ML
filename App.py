# Import required packages
import csv
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry
	
class App(Frame):
    # Initialise constructor
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()
    
	# GUI for retrieving data from the Laboratory Scientist.
	def initUI(self):
		self.num=[]
		self.parent.title("Compressive Strength")               # Title of GUI
		self.pack(fill=BOTH, expand=True)
		for i in range(9):
			self.num.append(StringVar()) 	
		res = StringVar()
		
		frame1 = Frame(self)
		frame1.pack(fill=X)

		lbl1 = Label(frame1, text="CEMENT", width=15)
		lbl1.pack(side=LEFT, padx=5, pady=5)

		entry1 = Entry(frame1,textvariable=self.num[0])
		entry1.pack(fill=X, padx=5, expand=True)

		frame2 = Frame(self)
		frame2.pack(fill=X)

		lbl2 = Label(frame2, text="BLAST FURNACE", width=15)
		lbl2.pack(side=LEFT, padx=5, pady=5)

		entry2 = Entry(frame2,textvariable=self.num[1])
		entry2.pack(fill=X, padx=5, expand=True)

		frame3 = Frame(self)
		frame3.pack(fill=X)

		lbl3 = Label(frame3, text="FLY ASH", width=15)
		lbl3.pack(side=LEFT, padx=5, pady=5)

		entry3 = Entry(frame3,textvariable=self.num[2])
		entry3.pack(fill=X, padx=5, expand=True)	

		frame4 = Frame(self)
		frame4.pack(fill=X)

		lbl4 = Label(frame4, text="WATER", width=15)
		lbl4.pack(side=LEFT, padx=5, pady=5)

		entry4 = Entry(frame4,textvariable=self.num[3])
		entry4.pack(fill=X, padx=5, expand=True)

		frame5 = Frame(self)
		frame5.pack(fill=X)

		lbl5 = Label(frame5, text="SUPERPLASTICIZER", width=15)
		lbl5.pack(side=LEFT, padx=5, pady=5)

		entry5 = Entry(frame5,textvariable=self.num[4])
		entry5.pack(fill=X, padx=5, expand=True)

		frame6 = Frame(self)
		frame6.pack(fill=X)

		lbl6 = Label(frame6, text="COARSE AGGREGATE", width=15)
		lbl6.pack(side=LEFT, padx=5, pady=5)

		entry6 = Entry(frame6,textvariable=self.num[5])
		entry6.pack(fill=X, padx=5, expand=True)

		frame7 = Frame(self)
		frame7.pack(fill=X)

		lbl7 = Label(frame7, text="FINE AGGREGATE", width=15)
		lbl7.pack(side=LEFT, padx=5, pady=5)

		entry7 = Entry(frame7,textvariable=self.num[6])
		entry7.pack(fill=X, padx=5, expand=True)

		frame8 = Frame(self)
		frame8.pack(fill=X)

		lbl8 = Label(frame8, text="AGE", width=15)
		lbl8.pack(side=LEFT, padx=5, pady=5)

		entry8 = Entry(frame8,textvariable=self.num[7])
		entry8.pack(fill=X, padx=5, expand=True)

		frame9 = Frame(self)
		frame9.pack(fill=X)

		lbl9 = Label(frame9, text="CONCRETE COMPRESSIVE STRENGTH", width=15)
		lbl9.pack(side=LEFT, padx=5, pady=5)

		entry9 = Entry(frame9,textvariable=self.num[8])
		entry9.pack(fill=X, padx=5, expand=True)

		frameC = Frame(self)
		frameC.pack(fill=X)

		btnplus = Button(frameC, text="Store", width=8, command=self.calc)
		btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

	def calc(self):
		l=[]
		try:
			for i in range(9):                        # iterating over different observations in the set of 9 attributes/features
				x=int(self.num[i].get())					
				l.append(self.num[i].get())
			
			with open('Concrete_Data.csv','a') as f:  
				writer = csv.writer(f)                # Store Data in CSV file
				writer.writerow(l)                    # Data will be stored Row-wise
			
		except:
			print('error')                            
		

def main():
    root = Tk()
    root.geometry("640x480")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
