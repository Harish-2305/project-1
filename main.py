import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size=(500,600)
#Builder.load_file("calculator.kv")

class calculatewid(Widget):
    def clear(self):
        self.ids.input.text="0"
    def button_press(self,data):
        prior=self.ids.input.text
        if prior == "0" or prior == "ERROR":
            self.ids.input.text=""
            self.ids.input.text=data
        else:
            self.ids.input.text=f"{prior}{data}"
    def math_sign(self,sign):
        prior=self.ids.input.text
        self.ids.input.text=f"{prior}{sign}"
    def dot(self):
        prior=self.ids.input.text
        a=["+","-","/","%","*"]
        b=[]
        num=[]
        for i in prior:
            if i in a:
                b.append(i)
        if len(b)!=0:
            c=b[-1]
            num=prior.split(c)
            prior=self.ids.input.text
            if c in prior and "." not in num[-1]:
                self.ids.input.text=f"{prior}."
        if "." in prior:
            pass
        else:
            self.ids.input.text=f"{prior}."
    def remove(self):
        prior=self.ids.input.text
        prior=prior[:-1]
        self.ids.input.text=prior
    def neg(self):
        prior=self.ids.input.text
        if "-" in prior:
            self.ids.input.text=f"{prior.replace("-","")}"
        else:
            self.ids.input.text=f"-{prior}"
    def equal(self):
        prior=self.ids.input.text
        try:
            answer=eval(prior)
            self.ids.input.text=str(answer)
        except:
            self.ids.input.text="ERROR"
        
            

        

class calculateApp(App):
    def build(self):
        return calculatewid()

calculateApp().run()
