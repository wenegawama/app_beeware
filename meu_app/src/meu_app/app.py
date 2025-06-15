import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class MeuApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "Nome: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Diga Olá!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        button2 = toga.Button("Click me", on_press=self.my_callback)

        icon_button = toga.Button(icon=toga.Icon("resources/my_icon"), on_press=self.my_callback)

        current_date = toga.DateInput()

        textbox = toga.MultilineTextInput()
        textbox.value = "FELIZ DE APRENDER BEEWARE !"

        password = toga.PasswordInput()

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(button2)
        main_box.add(icon_button)
        main_box.add(current_date)
        main_box.add(textbox)
        main_box.add(password)




        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print(f"Hello, {self.name_input.value}")

    def my_callback(self, widget):
        # handle event
        pass



def main():
    return MeuApp()