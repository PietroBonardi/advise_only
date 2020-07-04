from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

Builder.load_string("""
<CustomLabel@Label>
    color: 0,0,0,.75
    font_size: 45
    markup: True
    text_size: self.size
    halign: 'center'
    
    
    
<MenuScreen>:
    age_input: age
    incomeneed_input: incomeneed
    riskpropension_input: riskpropension
    protectionneed_input: protectionneed
    longtermcareneed_input: longtermcareneed
    inheritanceindex_input: inheritanceindex
    
    BoxLayout:
        orientation : "vertical"
        spacing: 10
        padding: 10
        
        Label:
            text: '[color=6666CC][b]A[/b]dvise[/color][color=CCCCCC][b]Only[/b][/color]'
            color: (0,0,0,0.5)
            font_size: 150
            markup: True
        
        GridLayout:
            cols : 2
            rows : 7
            
            CustomLabel: 
                text: "[b]Age:[/b]"
                
               
                
            TextInput:
                id: age
                font_size: 50
                multiline: False
                background_color: (1,1,1,0.3)            
            
            CustomLabel: 
                text: "[b]Income Need:[/b]"
            
            TextInput:
                id: incomeneed
                font_size: 50
                multiline: False
                background_color: (1,1,1,0.3)
            CustomLabel: 
                text: "[b]Risk Propension:[/b]"
            
            TextInput:
                id: riskpropension
                font_size: 50
                multiline: False
                background_color: (1,1,1,0.3)
                
            CustomLabel: 
                text: "[b]Protection Need:[/b]"
            
            TextInput:
                id: protectionneed
                font_size: 50
                multiline: False
                background_color: (1,1,1,0.3)
                
            CustomLabel: 
                text: "[b]Long Term Care Need:[/b]"
            
            TextInput: 
                id: longtermcareneed
                font_size: 50
                multiline: False
                background_color: (1,1,1,0.3)
            CustomLabel: 
                text: "[b]Inheritance Index:[/b]"
            
            TextInput: 
                id: inheritanceindex
                font_size: 50
                multiline: False
                background_color: (1,1,1,0.3)
                                   
        FloatLayout:   
            Button:
                text: 'Submit'
                background_normal: '/System/Library/Desktop Pictures/Solid Colors/Space Gray.png'
                border: (20,20,20,20)
                 
                font_size: 50
                size_hint : .25, .25 
                pos: 1000, 50
                on_release: 
                    root.manager.transition.duration = 0.4
                    root.manager.transition.direction = "left"
                    root.manager.current = 'information'
                    root.set_age()
                    root.set_incomeneed()
                    root.set_riskpropension()
                    root.set_protectionneed()
                    root.set_longtermcareneed()
                    root.set_inheritanceindex()
    
                                  

<InformationScreen>:
    BoxLayout:
        Label:
            text: 'Da capire quali prodotti'
            color: 0,0,0,1
        Button:
            text: 'Back to menu'
            background_normal: '/System/Library/Desktop Pictures/Solid Colors/Space Gray.png'
            
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.4
                root.manager.current = 'menu'
""")

# Declare both screens

class MenuScreen(Screen):
    age_input = ObjectProperty(True)
    incomeneed_input = ObjectProperty(True)
    riskpropension_input = ObjectProperty(True)
    protectionneed_input = ObjectProperty(True)
    longtermcareneed_input = ObjectProperty(True)
    inheritanceindex_input = ObjectProperty(True)

    age =''
    incomeneed = ''
    riskpropension = ''
    longtermcareneed = ''
    protectionneed = ''
    inheritanceindex = ''



    def set_age(self):
        age = int(self.age_input.text)
        print(age)

    def set_incomeneed(self):
        incomeneed = int(self.incomeneed_input.text)
        print(incomeneed)
    def set_riskpropension(self):
        riskpropension = int(self.riskpropension_input.text)
        print(riskpropension)

    def set_protectionneed(self):
        protectionneed = int(self.protectionneed_input.text)
        print(protectionneed)

    def set_longtermcareneed(self):
        longtermcareneed=int(self.longtermcareneed_input.text)
        print(longtermcareneed)
    def set_inheritanceindex(self):
        inheritanceindex = int(self.inheritanceindex_input.text)
        print(inheritanceindex)


class InformationScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(InformationScreen(name='information'))


class TestApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return sm


if __name__ == '__main__':
    TestApp().run()