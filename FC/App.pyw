from customtkinter import CTk, CTkFont

from MainFrame import MainFrame


class App(CTk):
    def __init__(self) -> None:
        super().__init__()

        # Config
        title = "Formulas calculator"
        icon_path = __file__ + "/../res/calc.ico"
        geometry = "{}x{}".format(560, 380)
        resizable = (False, False)
        global_font = CTkFont("Roboto", 30)

        # Configure the window
        self.title(title)
        self.wm_iconbitmap(icon_path)
        self.geometry(geometry)
        self.resizable(*resizable)

        # Create elements
        self._main_frame = MainFrame(self, global_font)

        self._display_elements()

    def _display_elements(self) -> None:
        """
        Display all window elements.
        """
        self._main_frame.pack(pady=10)  # y-axis padding = 10px

    def run(self) -> None:
        """
        Run the application.
        """
        self.mainloop()


if __name__ == '__main__':
    App().run()
