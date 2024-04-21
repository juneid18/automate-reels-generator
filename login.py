import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QFrame
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class LoginForm(QWidget):
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

        self.setWindowTitle('Login Form')
        self.setGeometry(300, 300, 600, 400)

        # Create a frame with a light gray background
        frame = QFrame(self)
        frame.setGeometry(100, 50, 400, 300)
        frame.setStyleSheet('background-color: #F0F0F0; border-radius: 10px;')

        # Create header label
        header_label = QLabel('Login', frame)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 24px; font-weight: bold; color: black; margin-bottom: 20px;')

        # Create input fields with placeholder text
        self.txt_username = QLineEdit(frame)
        self.txt_username.setPlaceholderText('Username')
        self.txt_username.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        self.txt_password = QLineEdit(frame)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setPlaceholderText('Password')
        self.txt_password.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        # Create round button with CSS styling
        self.btn_login = QPushButton('Login', frame)
        self.btn_login.clicked.connect(self.login_clicked)
        self.btn_login.setStyleSheet(
            'background-color: black; color: white; border: none; border-radius: 20px; padding: 10px 20px; font-size: 16px;'
        )

        self.btn_regi = QPushButton('Dont have an account Register Here ...', frame)
        self.btn_regi.clicked.connect(self.regi_clicked)
        self.btn_regi.setStyleSheet(
            'background-color: white; color: black; border: none; padding: 10px 20px; font-size: 12px;'
        )

        # Set up layout for the frame
        layout = QVBoxLayout(frame)
        layout.addWidget(header_label)
        layout.addWidget(self.txt_username)
        layout.addWidget(self.txt_password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_regi)

    def login_clicked(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        if not (username and password):
            self.show_message('Error', 'Please fill in all fields.')
        else:
            if self.check_credentials(username, password):
                self.show_message('Success', 'Login successful.')
                self.open_script_generator()

            else:
                self.show_message('Error', 'Invalid username or password.')

    def regi_clicked(self):
        from register import RegisterForm
        self.close()
        self.register_form = RegisterForm()
        self.register_form.show()
        print("Register")

    def open_script_generator(self):
        from main import ScriptGenerator
        self.script_generator = ScriptGenerator()
        self.script_generator.show()

        self.close()

    def check_credentials(self, entered_username, entered_password):
        # Check if entered credentials match those stored in a file
        with open('data.txt', 'r') as file:
            for line in file:
                if line.startswith('Username:') and entered_username in line:
                    next_line = next(file, None)
                    if next_line.startswith('Password:') and entered_password in next_line:
                        return True
        return False  

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec_())
