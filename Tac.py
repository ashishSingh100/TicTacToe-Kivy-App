from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import (ListProperty, NumericProperty)
from kivy.uix.modalview import ModalView
class GridEntry(Button):
	coords = ListProperty([0, 0])

class TicTacToeGrid(GridLayout):
	status=ListProperty([0,0,0,0,0,0,0,0,0])
	current_player=NumericProperty(1)
	def __init__(self,*args,**kwargs):
   		super(TicTacToeGrid,self).__init__(*args,**kwargs)
   		for row in range(3):
   			for column in range(3):
   				grid_entry=GridEntry(coords=(row,column))
   				grid_entry.bind(on_release=self.button_pressed)
				self.add_widget(grid_entry)
	def button_pressed(self,button):
		player={1:'O',-1:'X'}
		colors={1:(1,0,0,1),-1:(0,1,0,1)}
		row,column=button.coords
		status_index=3*row+column
		already_played=self.status[status_index]

		if not already_played:
			self.status[status_index]=self.current_player
			button.text={1:'O',-1:'X'}[self.current_player]
			button.background_color=colors[self.current_player]
			self.current_player*=-1
   		print('{} button clicked !'.format(button.coords))

   	def on_status(self,instance,new_value):
   		status=new_value
   		a=sum(status[0:3])
   		b=sum(status[3:6])
   		c=sum(status[6:9])
   		d=sum(status[0::3])
   		e=sum(status[1::3])
   		f=sum(status[2::3])
   		g=sum(status[::4])
   		h=sum(status[2:-2:2])
   		sums=[a,b,c,d,e,f,g,h]
   		if 3 in sums:
   			winner='O WIN'
   		elif -3 in sums:
   			winner='X'
   		elif 0 not in self.status:
   			winner='draw'
   		if winner:
   			popup = ModalView(size_hint=(0.75, 0.5))
			victory_label = Label(text=winner, font_size=50)
			popup.add_widget(victory_label)
			popup.bind(on_dismiss=self.reset)
			popup.open()
			popup.dismiss()

   	def reset(self, *args):
   		self.status = [0 for _ in range(9)]
   		for child in self.children:
   			child.text = ''
   			child.background_color = (1, 1, 1, 1)
   		self.current_player = 1

class TicTacToeApp(App):
	def build(self):
		return TicTacToeGrid()

if __name__=="__main__":
	TicTacToeApp().run()