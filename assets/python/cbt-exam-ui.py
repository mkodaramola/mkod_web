from tkinter import *
from tkinter.ttk import Button,Frame,Label,Style
import os




class window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master

	

	total_sec = 30

	def ui(MainFrame):
		
		scrW = MainFrame.winfo_screenwidth()
		scrH = MainFrame.winfo_screenheight()

		#MenuBar Frame
		s = Style()
		s.configure('topFrame.TFrame',background="green")
		topFrame = Frame(MainFrame,height=f"{scrH*(2/20)}",width=f"{scrW}",style="topFrame.TFrame")
		topFrame.pack(fill=X, pady=10)


		submit = Button(topFrame, text="Submit")
		submit.pack(side=RIGHT, fill=BOTH, expand=True)

		stopWatch = Label(topFrame,text="00:00", background="green", foreground="white", font=("Aerials","15"))
		stopWatch.pack(side=RIGHT, fill=BOTH, expand=True, padx=70)

		def calcApp():
			os.startfile("C:\\Windows\\system32\\calc.exe")

		calc = Button(topFrame, text="Calculator", command=calcApp)
		calc.pack(side=RIGHT, fill=BOTH, expand=True)
		
		def stop_watch():
			total_sec = window.total_sec 
			hr = total_sec//3600
			minutes = (total_sec-(hr*3600))//60
			sec = total_sec - ((hr*3600) + (minutes*60))
			
			

			if (hr == 0):
				stopWatch.config(text=f"{minutes}:{sec}")
			else:
				stopWatch.config(text=f"{hr}:{minutes}:{sec}")



			stopWatch.after(1000,stop_watch)
			window.total_sec -= 1
			if window.total_sec <= -1:
				MainFrame.destroy()
			

		stop_watch()

		logo = Label(topFrame,text="Logo.png", background="green", foreground="white")
		logo.pack(side=LEFT, fill=BOTH, expand=True)

		examTitle = Label(topFrame,text="Chemistry Test", background="green", foreground="white", font=('Impacts','20','bold'))
		examTitle.pack(side=LEFT, fill=BOTH, expand=True,padx=250)



		#________


		#ListBox Frame
		s = Style()
		s.configure('leftFrame.TFrame',background="green")
		leftFrame = Frame(MainFrame,height=f"{scrH}",width=f"{scrW*(1/5)}",style="leftFrame.TFrame")
		leftFrame.pack(side=LEFT,expand=True, fill=BOTH)
		w = int(scrW*(1/5))

		

		scroll = Scrollbar(leftFrame,orient="vertical")
		scroll.pack(side=RIGHT,fill=Y)

		
		l= Listbox(leftFrame, foreground="green", width=11, yscrollcommand=scroll.set, activestyle="dotbox", bg="#FFF", bd="5", font=("Helvitca","15"), selectborderwidth=0, selectbackground="green", selectmode=SINGLE)

		for i in range(100):
			l.insert(END,f"Question {i+1}")
		l.pack(side=LEFT,fill=BOTH, expand=True)

		scroll.config(command=l.yview)


		


		#_______



		s = Style()
		s.configure('rightFrame.TFrame',background="green")
		rightFrame = Frame(MainFrame,style="rightFrame.TFrame")
		rightFrame.pack(side=RIGHT,expand=True,fill=BOTH, padx=20)

		#Display Question Frame
		s = Style()
		s.configure('rtf.TFrame',background="green",borderweight=25)
		rtf = Frame(rightFrame,height=f"{scrH*(1/3)}",width=f"{scrW*(4/5)}",style="rtf.TFrame")
		rtf.pack(side=TOP, padx=30,pady=15)

		text = "Which of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following Which of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following Which of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following Which of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following Which of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following Which of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following  is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory studyWhich of the following is an inert gas? and is also the number 19th on the chemical periodic table in chemical science and laboratory study"		
		text = list(text)
		p = False
		for i in range(1,len(text)):
			if(i%120 == 0):
				p = True
			if p == True and text[i] == " ":
				text[i] = "\n"
				p = False

		t = ""
		t = t.join(text)

		scroll2 = Scrollbar(rtf, orient='vertical')
		scroll2.pack(side=RIGHT,fill=Y)



		dispQ = Text(rtf)
		dispQ.insert('end',t)
		dispQ.configure(state="disabled",background="#FFF",foreground="#000",height="10",width=150, yscrollcommand=scroll2.set ,padx=20,pady=15)
		dispQ.pack(side=LEFT,expand=True,fill=BOTH)

		scroll2.configure(command=dispQ.yview)






		#________________________

		s = Style()
		s.configure('rbf.TFrame',background="black")
		rbf = Frame(rightFrame,height=f"{scrH*(2/3)}",width=f"{scrW*(4/5)}",style="rbf.TFrame")
		rbf.pack(side=BOTTOM)



		#Options Frame
		s = Style()
		s.configure('rblf.TFrame',background="green", foreground="#FFF")
		rblf = Frame(rbf,height=f"{scrH*(2/3)}",width=f"{scrW*(4/5)*(1/2)}",style="rblf.TFrame")
		rblf.pack(side=LEFT)
		opt = ["Oxygen", "Chlorine", "Argon", " Flourine"]
		x = IntVar()
		for i in range (len(opt)):
			rdb = Radiobutton(rblf,text=opt[i], variable=x, value=i)
			rdb.configure(padx=25, pady=20, bg= "green",font=('Impacts','10','bold'))
			rdb.place(x=0,y=(i*80))


		prev = Button(rblf, text="Prev")
		prev.place(x=25	, y = rblf.winfo_screenwidth()-1000)

		save_next = Button(rblf,text="Save & Next")
		save_next.place(x= 400, y=rblf.winfo_screenwidth()-1000)


		#_____________
   


		#Diagram Frame
		s = Style()
		s.configure('rbrf.TFrame',background="green")
		rbrf = Frame(rbf,height=f"{scrH*(2/3)}",width=f"{scrW*(4/5)*(1/2)}",style="rbrf.TFrame")
		rbrf.pack(side=LEFT)



		#_____________









