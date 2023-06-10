from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import Button

from merge import login_window
from tkinter import*
from PIL import Image,ImageTk
class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Welcome",helign="center")
        
      
        
if __name__ == "__main__":
    app = MainApp()
    app.run()
    