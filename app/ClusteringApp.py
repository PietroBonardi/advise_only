# Kivy Library Dependancies
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
#
# Local Dependancies
from structure import MyScreenManager, StartScreen, FirstClusteringAge
from structure import FirstClusteringProtectionNeed, FirstClusteringLongTermCareNeed, Results

# This is the general App class.
# It returns the general widget as defined
# from the kv file
class ClusteringApp(App):
    def build(self):
        self.root_widget = Builder.load_file("./structure.kv")
        return self.root_widget

def main():

    AGE = None
    PROTECTIONNEED = None
    LONGTERMCARENEED = None

    ClusteringApp().run()

if __name__ == "__main__":
    main()
