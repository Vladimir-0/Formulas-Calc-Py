from customtkinter import CTk, CTkFont, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkRadioButton, CTkTextbox, IntVar
from decimal import Decimal

from Utils import perform_operation


class MainFrame(CTkFrame):
    def __init__(self, master: CTk, elements_font: CTkFont = None) -> None:
        super().__init__(master, fg_color="transparent")

        # Config
        self.checked = IntVar()
        self.checked.set(0)

        # Create elements
        self._info_label = CTkLabel(self, text="Enter 2 numbers and select a formula", font=elements_font)

        self._input_frame = CTkFrame(self, fg_color="transparent")  # Invisible element for grouping
        self._a_entry = CTkEntry(self._input_frame, placeholder_text="0", width=205, font=elements_font)
        self._b_entry = CTkEntry(self._input_frame, placeholder_text="0", width=205, font=elements_font)
        self._ok_button = CTkButton(
            self._input_frame, text="OK", command=self._ok_button_click, width=205, font=elements_font)

        self._grope_box = CTkFrame(self._input_frame, fg_color="transparent")
        self._radio_button_1 = CTkRadioButton(
            self._grope_box, text="5 * x + 10 / y", variable=self.checked, value=0, font=elements_font)
        self._radio_button_2 = CTkRadioButton(
            self._grope_box, text="3 * x^2 + y + 3", variable=self.checked, value=1, font=elements_font)
        self._radio_button_3 = CTkRadioButton(
            self._grope_box, text="(x + 10 * y) / 3", variable=self.checked, value=2, font=elements_font)

        self._result_textbox = CTkTextbox(self, width=535, font=elements_font, state='disabled')  # readonly

        self._bind_elements()
        self._display_elements()

    def _bind_elements(self) -> None:
        """
        Bind the keyboard keys to the elements.
        """
        self._a_entry.bind("<Return>", lambda event=None: self._b_entry.focus())
        self._b_entry.bind("<Return>", lambda event=None: self._ok_button_click())
        # <Return> is Enter on the keyboard
        # lambda generates a function with an event variable as input to avoid an error

    def _display_elements(self) -> None:
        """
        Display all frame elements.
        """
        self._info_label.pack()

        self._input_frame.pack(pady=10)
        self._a_entry.grid(sticky="W", column=0, row=0)
        self._b_entry.grid(sticky="W", column=0, row=1)
        self._ok_button.grid(sticky="W", column=0, row=2)

        self._grope_box.grid(sticky="E", column=1, row=0, rowspan=3, padx=20)
        self._radio_button_1.grid(sticky="W", column=0, row=0, padx=5, pady=5)
        self._radio_button_2.grid(sticky="W", column=0, row=1, padx=5, pady=5)
        self._radio_button_3.grid(sticky="W", column=0, row=2, padx=5, pady=5)

        self._result_textbox.pack()

    def _ok_button_click(self) -> None:
        """
        Put calculation results into the entry.
        """
        inp_a = self._a_entry.get()  # get first text
        inp_b = self._b_entry.get()  # get second text
        inp_operation = self.checked.get()  # get formula number
        result = perform_operation(Decimal(inp_a), Decimal(inp_b), inp_operation)  # Calculate result

        self._result_textbox.configure(state="normal")
        self._result_textbox.delete(1.0, "end")  # delete all characters
        # enters the calculation result
        self._result_textbox.insert(1.0, result)
        self._result_textbox.configure(state="disabled")
