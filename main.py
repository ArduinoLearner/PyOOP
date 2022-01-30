import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
kivy.require("2.0.0")
from kivy.app import App


from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button



actualbase = 10
actualbase2= 10
msg = ""

# OURSIDE FUNCTIONS
def changebase(n, base=10, to=10):
    '''
    params:
      n     - number to convert
      base  - current base of number 'n'
      to    - desired base, must be <= 36
    '''
    # check that new base is <= 36
    if to > 36 or base > 36:
        raise ValueError('max base is 36')

    # convert to base 10
    n = int(str(n), base)
    positive = n >= 0

    # return if base 10 is desired
    if to == 10:
        return str(n)

    # convert to new base
    n = abs(n)
    num = []
    handle_digit = lambda n: str(n) if n < 10 else chr(n + 55)
    while n > 0:
        num.insert(0, handle_digit(n % to))
        n = n // to

    # return string value of n in new base
    return ''.join(num) if positive else '-' + ''.join(num)

# WORKING CLASSESS

class TexteBox(TextInput):
    def __init__(self, **kw):
        super(TexteBox,self).__init__(**kw)
        self.size_gint_x=.1
        self.size_hint_y = .16
        self.pos_hint={'top':1}
        
        self.font_size=20

class ListeBox(Spinner):
    def __init__(self, **kw):
        super(ListeBox,self).__init__(**kw)
        
        self.values = ("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16")
#       self.pos_hint={'top':1}
        self.size_hint_x=None
        self.size_hint_y = None
        self.width = 50
        self.height= 60
        
        self.font_size=30

class Spies(Button):
    def __init__(self, **kw):
        super(Spies,self).__init__(**kw)
        self.text = "T1"

class SCRN1(Screen):
    def __init__(self, **kw):
        super(SCRN1,self).__init__(**kw)

        

        self.add_widget(Label(text="Convertidor de bases y Sumas v1",font_size=40,pos_hint={'x':0,'y':.2}))
#
        # Main Layout
        self.grid1 = BoxLayout(spacing = 20, padding = 10,width=self.width,height=self.height)
        
        # Text entrance
        self.txt1= TextInput(pos_hint={'top': 1},hint_text = "Numero A convertir")
        self.txt1.size_hint_x = .5
        self.txt1.size_hint_y = .16
        

        # Spinner Widget
        self.DRDW = Spinner(text = "Base", values = ("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"),pos_hint={'top': 1})        
        self.DRDW.size_hint_x = .5
        self.DRDW.size_hint_y = .16
        #self.DRDW._on_dropdown_select = self.printerer

        # Text entrance2
        self.txt2= Label(pos_hint={'top': 1},text = "Salida de numero")
        self.txt2.size_hint_x = .5
        self.txt2.size_hint_y = .16


        # Spinner2 Widget
        self.DRDW2 = Spinner(text = "Base", values = ("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"),pos_hint={'top': 1})
        self.DRDW2.size_hint_x = .5
        self.DRDW2.size_hint_y = .16
        #self.DRDW2._on_dropdown_select = self.printerer2

        
        
        # Adding Widgets to grid1 layout
        self.grid1.add_widget(self.txt1)
        self.grid1.add_widget(self.DRDW)
        self.grid1.add_widget(self.txt2)
        self.grid1.add_widget(self.DRDW2)




        # Creating another Layout
        self.grid2 = BoxLayout()
              
        # Label1 for Base indicator 
        self.Lb1 = Label(pos_hint={'top': .9})        
        self.Lb1.size_hint_x = .5
        self.Lb1.size_hint_y = .16
        self.Lb1.text = "Aqui se mostrarán\nlos resultados"
        
        # Label2 for Base indicator 
        self.Lb2 = Button(pos_hint={'top': .9},on_press=self.printerer) #################
        self.Lb2.text = "Convertir" 
        self.Lb2.size_hint_x = .5
        self.Lb2.size_hint_y = .13
        

        
        # Adding widgets to layout
        self.grid2.add_widget(self.Lb1)
        self.grid2.add_widget(self.Lb2)


        # Another Layout
        self.grid3=BoxLayout(spacing = 20, padding = 10)
  
        # Text entrance3
        self.txt3= TextInput(pos_hint={'top': 1},hint_text = "Numero1")
        self.txt3.size_hint_x = .5
        self.txt3.size_hint_y = .16
        

        # Spinner3 Widget
        self.DRDW3 = Spinner(text = "10", values = ("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"),pos_hint={'top': 1})
        self.DRDW3.size_hint_x = .5
        self.DRDW3.size_hint_y = .16
        #self.DRDW3.background_color =[.3,.4,.3,1]

            #Spinner3.1 Widget
        self.op = Spinner(text = "OP",values = ("+","-","*","/"),pos_hint={'top': 1},size_hint_x=.5,size_hint_y=.16)
        
        # Text entrance4
        self.txt4= TextInput(pos_hint={'top': 1},hint_text = "Numero2")
        self.txt4.size_hint_x = .5
        self.txt4.size_hint_y = .16

        # Spinner4 Widget
        self.DRDW4 = Spinner(text = "10", values = ("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"),pos_hint={'top': 1})
        self.DRDW4.size_hint_x = .5
        self.DRDW4.size_hint_y = .16


        # ANOTHER LAYOUT GRID4
        self.grid4 = BoxLayout(spacing = 20, padding = 10)
        # Text entrance5
        self.txt5= TextInput(pos_hint={'top': .9},hint_text = "Resultado")
        self.txt5.size_hint_x = .5
        self.txt5.size_hint_y = .16

        # Spinner5 Widget
        self.DRDW5 = Spinner(text = "10", values = ("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"),pos_hint={'top': .9})
        self.DRDW5.size_hint_x = .5
        self.DRDW5.size_hint_y = .16

        # LABEL DE RESULTADO 
        self.resultado = Label(pos_hint={'top': 1},text="AQUI RESULTADO")
        self.leibol = BoxLayout(orientation='vertical',spacing=20,padding=20,pos_hint={'top': 1})

        self.grid4.add_widget(self.txt5)
        self.grid4.add_widget(self.DRDW5)
        self.leibol.add_widget(self.resultado)
        self.leibol.add_widget(Label(text = ""))
        self.leibol.add_widget(Label(text = ""))
        self.leibol.add_widget(Label(text = ""))
        self.grid4.add_widget(self.leibol)     
        
          
        
        # BUTTON ACTION FOR CALCULATION
        self.bn1 = Button(text = "Calcular",on_press=self.operation,size_hint=(.3,.16),pos_hint={'top': 1})
        
        # Adding widgets to Grid3
        self.grid3.add_widget(self.txt3)
        self.grid3.add_widget(self.DRDW3)
        self.grid3.add_widget(self.op)
        self.grid3.add_widget(self.txt4)
        self.grid3.add_widget(self.DRDW4) 
        self.grid3.add_widget(self.bn1)  
        
         

        # ANOTHRE1
        self.grid0 = GridLayout(cols=1)

        # Adding widgets to screen

        self.grid0.add_widget(self.grid1)
        self.grid0.add_widget(self.grid3)
        self.grid0.add_widget(self.grid4)


        
        # Add to main Layout
        self.add_widget(self.grid0)
        self.add_widget(self.grid2)
        
        

        

    # CLASS FUNCTIONS

    # SPINNER TEXT IS SPINNER TEXT SELECTED
    def printerer(self,instance,*args):

        try:
            global actualbase
            global actualbase2

            
            actualbase = int(self.DRDW.text)
            actualbase2 = int(self.DRDW2.text)

            num1 = changebase(str(self.txt1.text),int(self.DRDW.text),int(self.DRDW2.text))



            self.Lb1.text= "El numero " + self.txt1.text + "\nEn base " + self.DRDW.text + "\n \nEquivale a "+  str(num1) + "\nEn base " + self.DRDW2.text
            #self.txt1.text = changebase(self.txt1.text,actualbase,int(*args))

            #self.DRDW.text = str(actualbase)
            #print(*args)
            
            #self.Lb1.text = "El numero " + str(changebase(int(self.txt1.text),actualbase,10)) + "\nes igual a "+self.txt1.text + "\nen base " + str(actualbase)
            

        except Exception:
            global msg
            
            if self.txt1.text != "":
                msg= " La base actual con la que se está trabajando es " + str(actualbase) + " \nLo que significa que no podrás agregar valores \npor encima de este numero" + "\nEstabas trabajando con base " + str(actualbase) + " e intentaste agregar " + "'" + self.txt1.text+"'" + "\nEs decir que debes agregar valor menor a la base que trabajes"
                pup = Popup(title = "", content = Label(text = msg),size_hint = (.55,.5))
                pup.open()

            else:
                msg =  "No hay nada para convertir" + "\nDebes agregar algún valor"    
                pup = Popup(title = "", content = Label(text = msg),size_hint = (.3,.3))



        


    def operation(self,instante,*args):
        try:
            resultado = 0
            num1 = changebase(str(self.txt3.text),int(self.DRDW3.text),10) # convertir el numero1 de base DRDW3 a base  10
            print(num1)
            num2 =  changebase(str(self.txt4.text),int(self.DRDW4.text),10)
            print(num2)
            r = num1 + self.op.text + num2
            print(r)
            resultado = eval(r)
            print(resultado)


            self.txt5.text=changebase(resultado,10,int(self.DRDW5.text))
            self.resultado.text = "La operación \n" + str(r) + " es = " + str(changebase(resultado,10,int(self.DRDW3.text))) + "\n Que es equivalente a\n " + str(resultado) + " en base 10"
        
        except Exception:
            msg =  "Error\nVerifique que halla seleccionado una operación\nAsegurese que no halla dejado espacios blancos en numero 1 y 2\nQue no halla seleccionado un numero invalido para la base que se este trabajando\n  Ejemplo: Selecciona base 2 y escribe un 4"    
            pup = Popup(title = "", content = Label(text = msg),size_hint = (.8,.3))
            pup.open()


            





        


class APP(App):
    def build(self):
        
        return SCRN1()



APP().run()
