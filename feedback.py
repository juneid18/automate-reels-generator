import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QDesktopWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from telegram import Bot

class FeedbackForm(QWidget):
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

        self.setWindowTitle('Feedback Form')
        self.setGeometry(300, 300, 600, 400)

        # Create a frame with a light gray background
        frame = QFrame(self)
        frame.setGeometry(0, 0, 400, 300)  # Set initial geometry
        self.center_frame(frame)  # Center the frame
        frame.setStyleSheet('background-color: #F0F0F0; border-radius: 10px;')

        # Create header label
        header_label = QLabel('Feedback Form', frame)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 24px; font-weight: bold; color: black; margin-bottom: 20px;')

        # Create input fields with placeholder text
        self.username_edit = QLineEdit(frame)
        self.username_edit.setPlaceholderText('Enter your Name')
        self.username_edit.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        self.feedback_edit = QLineEdit(frame)
        self.feedback_edit.setPlaceholderText('Enter your feedback')
        self.feedback_edit.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        # Create round button with CSS styling
        btn_send_feedback = QPushButton('Send Feedback', frame)
        btn_send_feedback.clicked.connect(self.send_feedback)
        btn_send_feedback.setStyleSheet(
            'background-color: black; color: white; border: none; border-radius: 20px; padding: 10px 20px; font-size: 16px;'
        )

        # Set up layout for the frame
        layout = QVBoxLayout(frame)
        layout.addWidget(header_label)
        layout.addWidget(self.username_edit)
        layout.addWidget(self.feedback_edit)
        layout.addWidget(btn_send_feedback)

    def send_feedback(self):
        username = self.username_edit.text()
        feedback_text = self.feedback_edit.text()

        # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
        bot_token = '6797131262:AAE8vTF4wnwiB5FYzXeF_pvrMxiNw-9rxoA'
        chat_id = '2134013900'  # Replace with your actual Telegram chat ID

        async def send_message():
            bot = Bot(token=bot_token)
            await bot.send_message(chat_id=chat_id, text=f"Feedback from {username}: {feedback_text}")

        asyncio.run(send_message())

        self.username_edit.clear()
        self.feedback_edit.clear()

    def center_frame(self, frame):
        # Center the frame in the screen
        screen_geo = QDesktopWidget().screenGeometry()
        frame.move((screen_geo.width() - frame.width()) // 2, (screen_geo.height() - frame.height()) // 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = FeedbackForm()
    form.show()
    sys.exit(app.exec_())
