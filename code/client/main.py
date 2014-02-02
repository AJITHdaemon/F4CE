import kivy
import subprocess
kivy.require('1.7.1')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class SayThis(BoxLayout):
	video_obj = ObjectProperty(None)
	def playvideo(self):
		self.video_obj.state='play'
		self.video_obj.volume=1
	def pausevideo(self):
		self.video_obj.state='pause'

class SayThisApp(App):
	def build(self):
		return SayThis()

if __name__=='__main__':
	SayThisApp().run()
