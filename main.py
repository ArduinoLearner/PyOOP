#Notes:
#   Creating widgets by Writing them as variables 
#   Add id's to widgets
#   Inaccessible widgets ( Widgets that were directly added to the layout with out typing "self")
#   Binding actions to Button
#   Access the widget properties in order to create conditions for button
#   Using isNumeric() method as a condition for my button
#   Pop up widget and customizing its properties

#   The biggest sized widget in a gridlayout will be the maxmimum widget size, that is to say, if you have a single Label with size_hint_y = .2
#   There's no way you can create a button with height <.2

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import kivy
kivy.require("2.0.0")

class MyLayout(BoxLayout):

    #initialize infine in comming keywords 
    def __init__(self,**kwargs):
    
        #call gridlayout
        super(MyLayout,self).__init__(**kwargs)
        
        self.orientation = 'vertical' # BoxLayout Orientation
        
        dis1 = GridLayout(cols= 3) # Layout's property
        self.add_widget(dis1) # Add widget layout

        dis1.add_widget(Label(text = "")) # Add an inaccessible widget(it becomes inaccessible when not writing the self. instance) inside the widget

        self.entradas = TextInput(multiline = True,size_hint=(.4,.2)) 
        self.ids['txtbx'] = self.entradas  #Adding id to widget by creating it as a variable, assign the id tag to variable
        dis1.add_widget(self.entradas)

        dis1.add_widget(Label(text="")) 

        dis1.add_widget(Label(text = "Gastos"))
        dis1.add_widget(Label(text = "Bolsa"))
        dis1.add_widget(Label(text = "Monedero"))

        self.gastos = TextInput(text = "50%",size_hint=(.4,.4))
        self.ids['gastos'] = self.gastos

        self.bolsa = TextInput(text = "35%",size_hint=(.4,.4))
        self.ids['bolsa'] = self.bolsa

        self.monedero = TextInput(text = "15%",size_hint=(.4,.4))
        self.ids['monedero'] = self.monedero

        dis1.add_widget(self.gastos)
        dis1.add_widget(self.bolsa)
        dis1.add_widget(self.monedero)

        dis1.add_widget(Label(text="",size_hint=(.4,.4)))
        init = Button(text = "Init",size_hint_y=.4)
        init.bind(on_press = self.press)
        dis1.add_widget(init)
        dis1.add_widget(Label(text="",size_hint=(.4,.4)))

        dis1.add_widget(Label(text=""))
        dis1.add_widget(Label(text=""))
        dis1.add_widget(Label(text=""))

        
       
    
    
    def press(self,instance):

        if(self.entradas.text == ""):
            pup = Popup(title = "", content = Label(text = "No has agregado una entrada"),size_hint = (.4,.2)) # Creating a pop up widget
            pup.open() #Opening the pop up

        elif ((self.entradas.text).isnumeric() == False): # USING THE ISNUMERIC METHOD
            pop = Popup(title = "", content = Label(text = "La entrada no es numerica"),size_hint=(.4,.2))
            pop.open()
        
        if (self.entradas.text != "" and (self.entradas.text).isnumeric() == True):
            entrada = int(self.entradas.text)
            gastos = (50 * entrada) / 100
            bolsita = (35*entrada)/100
            monedero = (15*entrada)/100

            self.gastos.text = str(gastos)
            self.bolsa.text = str(bolsita)
            self.monedero.text = str(monedero)




        

        
class MyApp(App):
    def build(self):
        return MyLayout()
    

MyApp().run()

