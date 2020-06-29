from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from joblib import dump, load

import time
import random

AGE = None
PROTECTIONNEED = None
LONGTERMCARENEED = None

kMedieLoad = load("../test_notebooks/k_medie_test.joblib")

class StartScreen(Screen):
    pass

class FirstClusteringAge(Screen):
    age_text_input = ObjectProperty()
    age = NumericProperty(0)

    def save_age(self):
        self.age = int(self.age_text_input.text)
        AGE = self.age
        print("Age", AGE)

class FirstClusteringProtectionNeed(Screen):
    protection_need_text_input = ObjectProperty()
    protection_need = NumericProperty(0)

    def save_protection_need(self):
        self.protection_need = float(self.protection_need_text_input.text)
        PROTECTIONNEED = self.protection_need
        print("Procetion Need:", PROTECTIONNEED)

class FirstClusteringLongTermCareNeed(Screen):
    long_term_care_need_text_input = ObjectProperty()
    long_term_care_need = NumericProperty(0)

    def save_long_term_care_need(self):
        self.long_term_care_need = (self.long_term_care_need_text_input.text)
        LONGTERMCARENEED = self.long_term_care_need
        print("Long Term Care Need", LONGTERMCARENEED)

class Results(Screen):
    # cluster_output = StringProperty('')
    output_text = StringProperty(rebind=True)
    def __init__(self, **kwargs):
        super(Results, self).__init__(**kwargs)
        self.output_text = "PRESS ME"

    def get_final_value(self):
        self.output_text = str(kMedieLoad.predict([[0.23, 0.78, 34]]))


class MyScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    StartScreen:
    FirstClusteringAge:
    FirstClusteringProtectionNeed:
    FirstClusteringLongTermCareNeed:
    Results:
<StartScreen>:
    name: 'start_screen'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Choose a Clustering Algorithm'
            font_size: 30
        BoxLayout:
            Button:
                text: 'Clustering Age~IncomeNeed~Sex'
                font_size: 30
                on_release: app.root.current = 'first_clustering_age'
        BoxLayout:
            Button:
                text: 'Clustering ProtectionNeed~IncomeNeed'
                font_size: 30
                on_release: app.root.current = 'second'

<FirstClusteringAge>:
    name: 'first_clustering_age'
    age_text_input: age_input
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Clustering Age~IncomeNeed~Sex'
            font_size: 30
        Label:
            text: 'Please insert your AGE'
            font_size: 30
        BoxLayout:
            TextInput:
                id: age_input
                font_size: 40
            Button:
                text: 'save'
                font_size: 30
                on_release: root.save_age()
            Button:
                text: 'NEXT'
                font_size: 30
                on_release: app.root.current = 'first_clustering_protection_need'
<FirstClusteringProtectionNeed>:
    name: 'first_clustering_protection_need'
    protection_need_text_input: protection_need_input
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Clustering Age~IncomeNeed~Sex'
            font_size: 30
        Label:
            text: 'Please insert your PROTECTION NEED'
            font_size: 30
        BoxLayout:
            TextInput:
                id: protection_need_input
                font_size: 40
            Button:
                text: 'save'
                font_size: 30
                on_release: root.save_protection_need()
            Button:
                text: 'NEXT'
                font_size: 30
                on_release: app.root.current = 'first_clustering_long_term_care_need'
<FirstClusteringLongTermCareNeed>:
    name: 'first_clustering_long_term_care_need'
    long_term_care_need_text_input: long_term_care_need_input
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Clustering Age~IncomeNeed~Sex'
            font_size: 30
        Label:
            text: 'Please insert your LONG TERM CARE NEED'
            font_size: 30
        BoxLayout:
            TextInput:
                id: long_term_care_need_input
                font_size: 40
            Button:
                text: 'save'
                font_size: 30
                on_release: root.save_long_term_care_need()
            Button:
                text: 'RESULTS'
                font_size: 30
                on_release: app.root.current = 'results'
<Results>:
    name: 'results'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Clustering Age~IncomeNeed~Sex'
            font_size: 30
        Label:
            text: 'According to the information given, your product should be'
            font_size: 30
        Button:
            id: output_text
            on_release: root.get_final_value()
            text: root.output_text
            font_size: 100
''')



class ScreenManagerApp(App):
    def build(self):
        return root_widget


ScreenManagerApp().run()
