from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
sound_1 = SoundLoader.load('gup1.wav')
sound_2 = SoundLoader.load('gup2.wav')
sound_3 = SoundLoader.load('gup3.wav')
sound_4 = SoundLoader.load('gup4.wav')

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        hl = BoxLayout()
        #txt = Label(text='Выбери экран')
        vl.add_widget(ScrButton(self, 'down', 'first', text='1'))
        vl.add_widget(ScrButton(self, 'left', 'second', text='2'))
        vl.add_widget(ScrButton(self, 'right', 'third', text='3'))
        vl.add_widget(ScrButton(self, 'up', 'fourth', text='4'))
        #hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        im = Image(source='giveup.jpg',size_hint=(None, None), size=('639sp', '360sp'))
        btn = Button(text='Never Gonna \nGive You Up', size_hint=(1, 1), pos_hint={'left': 0})
        btn_back = ScrButton(self, 'up', 'main', text='Назад', size_hint=(1, 1), pos_hint={'right': 1})
        vl.add_widget(im)
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)
        btn.on_press = self.press
    def press(self):
        sound_1.play()


class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        im = Image(source='upgive.jpg',size_hint=(None, None), size=('639sp', '360sp'))
        btn = Button(text='Never Gonna \nLet You down', size_hint=(1, 1), pos_hint={'left': 0})
        btn_back = ScrButton(self, 'right', 'main', text='Назад', size_hint=(1, 1), pos_hint={'right': 1})
        vl.add_widget(im)
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)
        btn.on_press = self.press
    def press(self):
        sound_2.play()


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        im = Image(source='pugive.jpg',size_hint=(None, None), size=('639sp', '360sp'))
        btn = Button(text='Never Gonna \nRun Around, and', size_hint=(1, 1), pos_hint={'left': 0})
        btn_back = ScrButton(self, 'left', 'main', text='Назад', size_hint=(1, 1), pos_hint={'right': 1})
        vl.add_widget(im)
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)
        btn.on_press = self.press
    def press(self):
        sound_3.play()


class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        im = Image(source='updunk.jpg',size_hint=(None, None), size=('639sp', '360sp'))
        btn = Button(text='Desert You', size_hint=(1, 1), pos_hint={'left': 0})
        btn_back = ScrButton(self, 'down', 'main', text='Назад', size_hint=(1, 1), pos_hint={'right': 1})
        vl.add_widget(im)
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)
        btn.on_press = self.press
    def press(self):
        sound_4.play()


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm


app = MyApp()
app.run()
