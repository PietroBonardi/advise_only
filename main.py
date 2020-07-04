from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
import pandas as pd
from joblib import load
import hdbscan

RESULT_LABEL = None
hdb_cluster = load("./HDBSCAN_leaf.joblib")

with open("for_standardization.csv","r") as file:
    for_stand = pd.read_csv(file)



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
                    root.set_inheritanceindex()
                    root.get_result()
    
<InformationScreen>:
    results_output: update
    BoxLayout:
        Label:
            id: update
            text: update.text
            color: 0,0,0,1
            
        Button: 
            text: "Update"
            on_release: 
                root.upd()
        Button:
            text: 'Back to menu'
            background_normal: '/System/Library/Desktop Pictures/Solid Colors/Space Gray.png'
            
            on_press: 
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.4
                root.manager.current = 'menu' 
                root.clearlabel()
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
        self.age = (float(self.age_input.text)-for_stand['Age'][0])/for_stand['Age'][1]
        print(self.age)

    def set_incomeneed(self):
        self.incomeneed = (float(self.incomeneed_input.text)-for_stand['IncomeNeed'][0])/for_stand['IncomeNeed'][1]
        print(self.incomeneed)
    def set_riskpropension(self):
        self.riskpropension = (float(self.riskpropension_input.text)-for_stand['RiskPropension'][0])/for_stand['RiskPropension'][1]
        print(self.riskpropension)

    def set_protectionneed(self):
        self.protectionneed = (float(self.protectionneed_input.text)-for_stand['ProtectionNeed'][0])/for_stand['ProtectionNeed'][1]
        print(self.protectionneed)

    def set_inheritanceindex(self):
        self.inheritanceindex = (float(self.inheritanceindex_input.text)-for_stand['InheritanceIndex'][0])/for_stand['InheritanceIndex'][1]
        print(self.inheritanceindex)

    def get_result(self):
        points = [[self.age,self.incomeneed,self.riskpropension,self.protectionneed,self.inheritanceindex]]
        print("My Points: ",points)
        labels, streghts = hdbscan.approximate_predict(hdb_cluster,points)
        print("Predictions: ", labels[0])

        global RESULT_LABEL
        RESULT_LABEL = labels[0]


#MenuScreen
class InformationScreen(Screen):

    results_output = ObjectProperty(True)

    def upd(self):
        if RESULT_LABEL is not None:
            self.results_output.text = str(RESULT_LABEL)
        else:
            self.results_output.text = "Error"

    def clearlabel(self):
        self.results_output.text = "Results"
    


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
