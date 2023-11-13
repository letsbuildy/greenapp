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

        button_box = toga.Box(style=Pack(direction=COLUMN,padding=(10,75,5,165)))
        login_button = toga.Button(
            "Login",
            on_press=self.dashboard
        )
        forget_pass_button = toga.Button(
            "Forget password",
            style=Pack(padding=(10,0,0,0)))
        button_box.add(login_button)
        button_box.add(forget_pass_button)

        logo = toga.Image(self.paths.app / "logo.png")
        view_logo = toga.ImageView(logo,style=Pack(alignment="center"))
        
        main_box.add(view_logo)
        main_box.add(username_box)
        main_box.add(password_box)
        main_box.add(button_box)

        self.main_window = toga.MainWindow()
        self.main_window.content = main_box
        self.main_window.show()
        

    def dashboard(self,widget):
        main_box = toga.Box(style=Pack(direction=COLUMN,alignment="center"))
        
        
        status_box = toga.Box(style=Pack(direction=COLUMN,padding=30))
        online_box=toga.Box(style=Pack(direction=ROW))
        online_label = toga.Label("device",style=Pack(padding=(10,10,0,0),alignment="bottom"))
        online_status = toga.Image(self.paths.app / "images/red.png")
        online_status_viewer = toga.ImageView(online_status,style=Pack(height=48,width=48,alignment="center"))
        online_box.add(online_label)
        online_box.add(online_status_viewer)
        status_box.add(online_box)

        pump_box=toga.Box(style=Pack(direction=ROW))
        pump_label = toga.Label("pump",style=Pack(padding=(10,10,0,0),alignment="bottom"))
        pump_status = toga.Image(self.paths.app / "images/watering.gif")
        pump_status_viewer = toga.ImageView(pump_status,style=Pack(height=48,width=48,alignment="center"))
        pump_box.add(pump_label)
        pump_box.add(pump_status_viewer)
        status_box.add(pump_box)

        tank_box=toga.Box(style=Pack(direction=ROW))
        tank_label = toga.Label("water",style=Pack(padding=(10,10,0,0),alignment="bottom"))
        tank_status = toga.Image(self.paths.app / "images/green.png")
        tank_status_viewer = toga.ImageView(tank_status,style=Pack(height=48,width=48,alignment="center"))
        tank_box.add(tank_label)
        tank_box.add(tank_status_viewer)
        status_box.add(tank_box)

        info_box = toga.Box(style=Pack(direction=COLUMN,padding=30))
        last_run_box= toga.Box(style=Pack(direction=ROW))
        last_run_label = toga.Label("Last run:",style=Pack(padding=10))
        last_run_info= toga.Label("yesterday",style=Pack(padding=10))
        last_run_box.add(last_run_label)
        last_run_box.add(last_run_info)
        info_box.add(last_run_box)

        auto_mode = toga.Switch("Auto irrigation",style= Pack(padding=10))
        info_box.add(auto_mode)

        sub_box = toga.Box(children=
                           [status_box,
                            toga.Divider(direction=1),
                            info_box],
                            style=Pack(direction=ROW,padding=30))
        
        main_box.add(sub_box)

        countdown_box = toga.Box( children= [
            toga.Label("Pump Countdown",style=Pack(padding=10,alignment="center")),
            toga.Divider(),
            toga.Label("50"+"sec",style=Pack(padding=10))
        ],style=Pack(direction=COLUMN, flex=1, padding=10,alignment="center"))
        main_box.add(countdown_box)
        

        pump_action_box=toga.Box(style=Pack(padding=10,direction=COLUMN))
        start_pump = toga.Button("Run pump",style=Pack(background_color="green",
                                                       color="white",
                                                          padding=5))
        stop_pump = toga.Button("Stop pump",style=Pack(background_color="red",
                                                       color="white",
                                                       padding=5))
        
        set_schedule = toga.Button("Set schedules",style=Pack(background_color="blue",
                                                       color="white",
                                                       padding=5))
        
        pump_action_box.add(start_pump)
        pump_action_box.add(stop_pump)
        pump_action_box.add(set_schedule)
        main_box.add(pump_action_box)

        

        self.main_window.content = main_box
        self.main_window.show()

    
def main():
    return greenspace()
