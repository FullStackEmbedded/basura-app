'''

Main for Full Stack Embedded Basura App
see documentation for whole project: https://goo.gl/AqpBBp
documentation for Basura App: https://goo.gl/TZijCa

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import subprocess


""" Call the reporter bash script """
class  Reporter(BoxLayout):

    """reporter bash script called when button is pressed"""
    def start_reporter(self):
        print("starting reporter bash script")
        subprocess.call("/home/happycarmi/FSE/basura/basura-app/reporter.sh")


class BasuraApp(App):
    def build(self):
        title = "Basura-App"

if __name__ == '__main__':
    BasuraApp().run()