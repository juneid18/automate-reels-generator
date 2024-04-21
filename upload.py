import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QFrame
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class Upload(QWidget):
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

        self.setWindowTitle('Upload Form')
        self.setGeometry(300, 300, 600, 400)

        # Create a frame with a light gray background
        frame = QFrame(self)
        frame.setGeometry(100, 50, 400, 300)
        frame.setStyleSheet('background-color: #F0F0F0; border-radius: 10px;')

        # Create round button with CSS styling
        self.btn_upload = QPushButton('Add YouTube Channel', self)
        self.btn_upload.clicked.connect(self.Add_clicked)
        self.btn_upload.setStyleSheet(
            'text-align:center; background-color: #1ac6ff; cursor: pointer; color: white; z-index:1; border: none; border-radius: 200px; padding: 10px 20px; font-size: 16px;'
        )

        # Create header label
        header_label = QLabel('Upload On Youtube', frame)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 24px; font-weight: bold; color: black; margin-bottom: 20px;')

        # Create input fields with placeholder text
        self.txt_Title = QLineEdit(frame)
        self.txt_Title.setPlaceholderText('Title')
        self.txt_Title.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        self.txt_Description = QLineEdit(frame)
        self.txt_Description.setPlaceholderText('Description')
        self.txt_Description.setStyleSheet('font-size: 16px; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;')

        # Create round button with CSS styling
        self.btn_upload = QPushButton('Upload', frame)
        self.btn_upload.clicked.connect(self.Upload_clicked)
        self.btn_upload.setStyleSheet(
            'background-color: #CD201F; cursor: pointer; color: white; border: none; border-radius: 20px; padding: 10px 20px; font-size: 16px;'
        )

        # Set up layout for the frame
        layout = QVBoxLayout(frame)
        layout.addWidget(header_label)
        layout.addWidget(self.txt_Title)
        layout.addWidget(self.txt_Description)
        layout.addWidget(self.btn_upload)

        # Assign the layout to the frame
        frame.setLayout(layout)

    def Upload_clicked(self):
        Title = self.txt_Title.text()
        Description = self.txt_Description.text()
        vid_path = "final.mp4"

        if not (Title and Description):
            self.show_message('Error', 'Please fill in all fields.')
        else:
            try:
                from upload_video import upload_video_to_youtube
                upload_video_to_youtube(vid_path, Title, Description)
                self.show_message('Success', 'Upload successful.')
            except Exception as e:
                print(f"Error in Upload_clicked: {e}")

    def Add_clicked(self):
        print("Add_clicked method called")
        try:
            from addchannel import Channel
            self.addchannel = Channel()
            self.addchannel.show()
            self.close() 
        except Exception as e:
            print(f"Error in Add_clicked: {e}")


    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Upload()
    window.show()
    sys.exit(app.exec_())
