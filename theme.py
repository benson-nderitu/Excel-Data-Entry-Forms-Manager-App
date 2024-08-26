# code to implement in the App

# from theme import toggle_theme
#         self.theme_button.clicked.connect(toggle_theme)  # Connect theme_button to toggle_theme function


from PyQt5 import QtWidgets

toggle_flag = False  # Flag to toggle between two styles

def toggle_theme():
    global toggle_flag
    main_window = QtWidgets.QApplication.instance().activeWindow()  # Get the active window (MainWindow in this case)

    if toggle_flag:
        new_stylesheet = """
            background-color: rgb(255, 255, 255);
            alternate-background-color: rgb(0, 0, 0);
        """
    else:
        new_stylesheet = """
            background-color: rgb(0, 0, 0);
            alternate-background-color: rgb(255, 255, 255);
        """

    main_window.setStyleSheet(new_stylesheet)  # Set new style sheet
    toggle_flag = not toggle_flag  # Toggle the flag for next click