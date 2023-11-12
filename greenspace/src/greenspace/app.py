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
            on_press=self.say_hello,
            style=Pack(padding=(10,75,5,165))
        )

        logo = toga.Image(self.paths.app / "logo.png")
        view_logo = toga.ImageView(logo,style=Pack(alignment="center"))
        
        main_box.add(view_logo)
        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print(f"Username, {self.username_input.value}")
        print(f"Password, {self.password_input.value}")


def main():
    return greenspace()
