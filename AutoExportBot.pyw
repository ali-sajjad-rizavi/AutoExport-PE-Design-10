from tkinter import *
from tkinter import messagebox
from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time

WAITING_TIME = 0.5

class Robot:
	def startExporting():
		try:
			downstep = 48
			for i in range(10):
				posX, posY = pyautogui.position()
				if posX < 100 and posY < 100:
					print('Stopped before working!')
					return
				#-----------------------------------------------------------------------------
				if downstep == 114 or downstep == 213 or downstep == 279 or downstep == 312:
					print('continue...')
					downstep += 33
					continue
				pyautogui.click(imagesearch('filebutton.png'))
				time.sleep(WAITING_TIME)
				pyautogui.click(imagesearch('exportoption.png'))
				time.sleep(WAITING_TIME)
				#---------------------------
				saveAsType_position = imagesearch('saveastypelabel.png')
				pyautogui.click(saveAsType_position + (803, 0))
				time.sleep(WAITING_TIME)
				pyautogui.click(saveAsType_position + (464, downstep))
				time.sleep(WAITING_TIME)
				pyautogui.click(imagesearch('savebutton.png'))
				time.sleep(WAITING_TIME)
				#
				errorIcon_position = imagesearch('erroricon.png')
				if errorIcon_position[0] != -1:
					pyautogui.click(errorIcon_position + (400, 160))
				#
				downstep += 33
		except:
			messagebox.showinfo('Imagesearch error!', 'Could not find a button.')



class BotWindow:
	def __init__(self):
		self.__root = Tk()
		self.__root.title("PE Design 10 - Export Bot")
		self.__root.geometry("300x150")
		self.__root.resizable(False, False)
		Button(self.__root, text='Start exporting', command=Robot.startExporting).grid(padx=100, pady=25, row=0)
		Label(self.__root, text='Note: Move the mouse to\nthe Top-Left corner to stop.').grid(row=1)

	def show(self):
		self.__root.mainloop()

#---------


def main():
	form = BotWindow()
	form.show()

if __name__ == '__main__':
	main()