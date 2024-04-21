import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QFrame
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from login import LoginForm

class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set up black and white color palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))  # White background
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))     # Black text
        palette.setColor(QPalette.Button, QColor(0, 0, 0))         # Black buttons
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))  # White button text
        self.setPalette(palette)

        self.setWindowTitle('Registration Form')
        self.setGeometry(300, 300, 600, 500)

        # Create a frame with a light gray background
        frame = QFrame(self)
        frame.setGeometry(120, 10, 400, 450)
        frame.setStyleSheet('background-color: #F0F0F0; border-radius: 10px; box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;')

        # Create header label
        header_label = QLabel('Registration', frame)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 24px; font-weight: bold; color: black; margin-bottom: 20px;')

        # Create input fields with placeholder text
        self.txt_name = QLineEdit(frame)
        self.txt_name.setPlaceholderText('Name')
        self.txt_name.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        self.txt_username = QLineEdit(frame)
        self.txt_username.setPlaceholderText('Username')
        self.txt_username.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        self.txt_password = QLineEdit(frame)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setPlaceholderText('Password')
        self.txt_password.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        self.txt_confirm_password = QLineEdit(frame)
        self.txt_confirm_password.setEchoMode(QLineEdit.Password)
        self.txt_confirm_password.setPlaceholderText('Confirm Password')
        self.txt_confirm_password.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 20px; color: black;')

        # Create round button with CSS styling
        self.btn_register = QPushButton('Register', frame)
        self.btn_register.clicked.connect(self.register_clicked)
        self.btn_register.setStyleSheet(
            'background-color: black; color: white; border: none; border-radius: 20px; padding: 10px 20px; font-size: 16px;'
        )

        self.btn_login = QPushButton('Have an account login ..', frame)
        self.btn_login.clicked.connect(self.login_click)
        self.btn_login.setStyleSheet(
            'background-color: white; color: black; border: none; padding: 10px 20px; font-size: 12px;'
        )

        # Set up layout for the frame
        layout = QVBoxLayout(frame)
        layout.addWidget(header_label)
        layout.addWidget(self.txt_name)
        layout.addWidget(self.txt_username)
        layout.addWidget(self.txt_password)
        layout.addWidget(self.txt_confirm_password)
        layout.addWidget(self.btn_register)
        layout.addWidget(self.btn_login)

    def register_clicked(self):
        name = self.txt_name.text()
        username = self.txt_username.text()
        password = self.txt_password.text()
        confirm_password = self.txt_confirm_password.text()

        if not (username and password and confirm_password):
            self.show_message('Error', 'Please fill in all fields.')
        elif password != confirm_password:
            self.show_message('Error', 'Passwords do not match.')
        else:
            with open('data.txt','w') as file:
                file.write(f"Username: {username}\n")
                file.write(f"Password: {password}\n")
                file.write(f"Name: {name}\n")
            self.show_message('Success', 'Registration successful.')
            self.close()
            self.login_form = LoginForm()
            self.login_form.show()
    def login_click(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
        print("login page ")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    register_form = RegisterForm()
    register_form.show()
    sys.exit(app.exec_())

