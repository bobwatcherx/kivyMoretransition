from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

# AND IMPORRT TRANSITION
from kivy.garden.moretransitions import PixelTransition,RippleTransition,BlurTransition,RVBTransition



# LOAD KV
Builder.load_file("homescreen.kv")
Builder.load_file("secondscreen.kv")

class Homescreen(MDScreen):
	def RippleEffect(self):
		self.manager.transition = RippleTransition()
		self.manager.current = "second"
	def BlurEffect(self):
		self.manager.transition = BlurTransition()
		self.manager.current = "second"

	def RVBEffect(self):
		self.manager.transition = RVBTransition()
		self.manager.current = "second"
	def PixelEffect(self):
		self.manager.transition = PixelTransition()
		self.manager.current = "second"

class Secondscreen(MDScreen):
	def RippleEffect(self):
		self.manager.transition = RippleTransition()
		self.manager.current = "home"
	def BlurEffect(self):
		self.manager.transition = BlurTransition()
		self.manager.current = "home"

	def RVBEffect(self):
		self.manager.transition = RVBTransition()
		self.manager.current = "home"
	def PixelEffect(self):
		self.manager.transition = PixelTransition()
		self.manager.current = "home"



class MyApp(MDApp):
	def build(self):
		self.screen = ScreenManager()
		self.screen.add_widget(Homescreen(name="home"))
		self.screen.add_widget(Secondscreen(name="second"))
		return self.screen

if __name__ == "__main__":
	MyApp().run()
