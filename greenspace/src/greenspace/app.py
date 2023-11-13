"""
smart_gardening app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class greenspace(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN,alignment="center"))

        username_label = toga.Label(
            "Username",
            style=Pack(padding=(5,30,10,40))
        )
        self.username_input = toga.TextInput(style=Pack(flex=1))

        username_box = toga.Box(style=Pack(direction=ROW, padding=(0,75,10,30)))
        username_box.add(username_label)
        username_box.add(self.username_input)

        password_label = toga.Label(
            "Password",
            style=Pack(padding=(5,30,10,40))
        )
        self.password_input = toga.PasswordInput(style=Pack(flex=1))

        password_box = toga.Box(style=Pack(direction=ROW, padding=(0,75,10,30)))
        password_box.add(password_label)
        password_box.add(self.password_input)

        button = toga.Button(
            "Login",
            on_press=self.login,
            style=Pack(padding=(10,75,5,165))
        )

        logo = toga.Image(self.paths.app / "logo.png")
        view_logo = toga.ImageView(logo,style=Pack(alignment="center"))
        
        main_box.add(view_logo)
        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(button)

        self.main_window = toga.MainWindow()
        self.main_window.content = main_box
        self.main_window.show()
        

    def login(self,widget):
        main_box = toga.Box(style=Pack(direction=COLUMN,alignment="center"))
        duration_label = toga.Label(
            "Pump duration(sec)",
            style=Pack(padding=(5,30,0,0))
        )
        duration = toga.NumberInput(style=Pack(flex=1),min=1,max=999,step=1)
        
        duration_box = toga.Box(style=Pack(direction=ROW, padding=(100,30,10,40)))
        duration_box.add(duration_label)
        duration_box.add(duration)
        
        button = toga.Button(
            "Run pump",
            style=Pack(padding=(10,30,5,40))
        )

        main_box.add(duration_box)
        main_box.add(button)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return greenspace()
