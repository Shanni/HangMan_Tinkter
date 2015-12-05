import Tkinter
import random

def drawMan(c,i):
	x=150
	y=150
	head=20
	body=50
	hand_x,hand_y=30,40
	offset=5
	coord = x-head, y-head, x+head, y+head
	if i>=1:
		oval = c.create_oval(coord)
	if i>=2:
		poly = c.create_line(x-head,y+head,x+head,y+head,x+head,x+head+body\
		,x-head,y+head+body,x-head,y+head)
	if i>=3:
		left_head = c.create_line(x-head,y+head+offset,x-head-hand_x,y+head-hand_y)
	if i>=4:
		right_head = c.create_line(x+head,y+head+offset,x+head+hand_x,y+head-hand_y)
	if i>=5:
		left_leg = c.create_line(x-head+offset,y+head+body,x-head-hand_x,y+head+body+hand_y)
	if i>=6:
		right_leg = c.create_line(x+head-offset,y+head+body,x+head+hand_x,y+head+body+hand_y)

def drawAlphabet(c, guessed):
	x0=50
	y=300
	x=100
	offset=0
	c.create_text(x0,y, font=("Purisa", 14), text="Letters:   ")
	for letter in text:
		if letter in guessed:
			c.create_text(100+offset,y, font=("Purisa",14), text=letter, fill="red")
		else:
			c.create_text(100+offset,y, font=("Purisa",14), text=letter, fill="green")
		offset+=14

def drawGuess(c):
	x=300
	y=200
	offset=0
	text=""
	for letter in answer:
		if letter in guessed:
			c.create_text(x+offset,y, font=("Purisa",14), text=letter)
			c.create_text(x+offset,y+3, font=("Purisa",14), text="_")
		else:
			if letter!=" ":
				c.create_text(x+offset,y+3, font=("Purisa",14), text="_")
		offset+=14

def updateGuess(currentGuess):
	guessed.add(currentGuess)
	if currentGuess not in answer:
		global wrongGuess
		wrongGuess+=1

def winGame(c):
	c.create_text(200,50, font=("Purisa",18), text="Congratulations!", fill="green")

def lossGame(c):
	msg="You lost! The answer was: \n"+answer
	c.create_text(200,50,font=("Purisa",18), text=msg, fill="red")

def guessLetter(top1):
	row1=Tkinter.Frame(top1)
	label=Tkinter.Label(row1, width=30, text="Guess a letter")
	row2=Tkinter.Frame(top1)
	global entry
	entry=Tkinter.Entry(row2)
	row1.pack(side="top",padx=5,pady=5)
	label.pack()
	row2.pack(padx=20,pady=20)
	entry.pack()

def callback():
	if entry.get()=="":
		return
	currentGuess=entry.get()[0]
	if ord(currentGuess)>=97 and ord(currentGuess)<=122:
		currentGuess=chr(ord(currentGuess)-32) # lower letter to upper letter
	#print currentGuess
	updateGuess(currentGuess)

	c.delete("all")
	drawMan(c,wrongGuess)
	drawAlphabet(c,guessed)
	drawGuess(c)
	c.pack(side="top")

	entry.delete(0,"end")
	global wrongGuess
	if wrongGuess>=6:
		top1.quit()
		lossGame(c)
		c.pack()
	
	elif (set(answer)&guessed)==set(answer)-set([" "]):
		top1.quit()
		winGame(c)
		c.pack()

	# print set(answer)
	# print guessed

def init():
	global text # A-Z
	global guessed
	guessed=set()
	text=[] 
	for i in xrange(26):
		text.append(chr(65+i))

	#generate the answer
	global answer
	answers=["ALAN TURING", "DONALD KNUTH", "ADA LOVELACE", "GRACE HOPPER",\
	"GORDON MOORE"]
	random.seed(1)
	answer=answers[int(random.random()*5)]

# if __name__=='__main__':
# small window for guessing
top1=Tkinter.Tk()
top=Tkinter.Tk()
top1.title("Guessing Computer Scientist")
top.title("Hangman Game!(Guessing Computer Scientist")

wrongGuess=0
currentGuess=''

init()
c=Tkinter.Canvas(top, bg="white", height=400, width=500)

drawMan(c,wrongGuess)
drawAlphabet(c,guessed)
drawGuess(c)
c.pack(side="top")

guessLetter(top1)
b1=Tkinter.Button(top1,text="Enter", width=10, command=callback)
b1.pack(side="left", padx=10, pady=10)
b2=Tkinter.Button(top1,text="Cancel", width=10)
b2.pack(side="right", padx=10, pady=10)

top.mainloop()
top1.mainloop()