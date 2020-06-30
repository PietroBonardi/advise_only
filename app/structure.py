# Kivy Library Dependancies
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
#
# Scikit Learn Dependencies
from joblib import dump, load
#
#
# ### Definition of the screen classes ###
#
#
# This will be the root class
# It contains the information of all
# screens and the way to change from
# one to the other

class MyScreenManager(ScreenManager):
    pass

# First screen. Here one chooses between different
# clustering algorithms
class StartScreen(Screen):
    pass

#
# ### 1ST CLUSTERING ###
#
# Screen to insert Age
class FirstClusteringAge(Screen):
    # Text that interacts with the screen
    # must be defined as an object
    age_text_input = ObjectProperty()
    # This is just the variable that stores the
    # age value for this class
    age = NumericProperty(0)

    def save_age(self):
        self.age = int(self.age_text_input.text)
        global AGE
        AGE = self.age
        print("Age", AGE)
#
#
# Screen to insert Protection Need (see slides for meaning)
class FirstClusteringProtectionNeed(Screen):
    # See previous class
    protection_need_text_input = ObjectProperty()
    protection_need = NumericProperty(0)

    def save_protection_need(self):
        self.protection_need = float(self.protection_need_text_input.text)
        global PROTECTIONNEED
        PROTECTIONNEED = self.protection_need
        print("Procetion Need:", PROTECTIONNEED)
#
#
# Screen to insert Long Term Care Need (see slides for meaning)
class FirstClusteringLongTermCareNeed(Screen):
    # See Age class
    long_term_care_need_text_input = ObjectProperty()
    long_term_care_need = NumericProperty(0)

    def save_long_term_care_need(self):
        self.long_term_care_need = float(self.long_term_care_need_text_input.text)
        global LONGTERMCARENEED
        LONGTERMCARENEED = self.long_term_care_need
        print("Long Term Care Need", LONGTERMCARENEED)
#
#
# Screen to show the correct product for the clustering
#
# !!! At the moment, it just shows the cluster to which it
# belongs to, but a simple match to a pre-determined product
# can do !!!
#
class Results(Screen):
    # cluster_output = StringProperty('')
    output_text = StringProperty(rebind=True)
    def __init__(self, **kwargs):
        super(Results, self).__init__(**kwargs)
        self.output_text = "PRESS ME"

    def get_final_value(self):
        print(PROTECTIONNEED, LONGTERMCARENEED, AGE)
        # I load the trained clustering algorithm from here
        kMedieLoad = load("./k_medie_test.joblib")
        self.output_text = str(kMedieLoad.predict([[PROTECTIONNEED, LONGTERMCARENEED, AGE]]))
