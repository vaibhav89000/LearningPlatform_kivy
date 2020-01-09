from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from gtts import gTTS
from pygame import mixer
import pyttsx3

class SpeakerWindow(Screen):
    pass
    def btn_clk(self):
        # txt="यह स्पीकर है"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("speaker.mp3")
        mixer.init()
        mixer.music.load("speaker.mp3")
        mixer.music.play()

class KeyboardWindow(Screen):
    pass
    def btn_clk(self):
        # txt="यह कीबोर्ड है"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("keyboard.mp3")
        mixer.init()
        mixer.music.load("keyboard.mp3")
        mixer.music.play()

class MouseWindow(Screen):
    pass
    def btn_clk(self):
        # txt="यह माउस है"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("mouse.mp3")
        mixer.init()
        mixer.music.load("mouse.mp3")
        mixer.music.play()

class CpuWindow(Screen):
    pass
    def btn_clk(self):
        # txt="यह सीपीयू है"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("cpu.mp3")
        mixer.init()
        mixer.music.load("cpu.mp3")
        mixer.music.play()

class TestWindow(Screen):
    pass




class MainWindow(Screen):
    pass

class MonitorWindow(Screen):
    pass
    def btn_clk(self):
        # txt="यह मॉनिटर है"
        # obj = gTTS(text=txt, slow=False, lang='hi')
        # obj.save("monitor.mp3")
        mixer.init()
        mixer.music.load("monitor.mp3")
        mixer.music.play()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("second.kv")

class SecondApp(App):
    def build(self):
        return kv



if __name__ == "__main__":
    SecondApp().run()