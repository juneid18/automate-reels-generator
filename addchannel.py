import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QFrame

class FileCopyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()

        # Create a frame for visual separation
        frame = QFrame(self)
        frame.setFrameShape(QFrame.HLine)
        frame.setFrameShadow(QFrame.Sunken)
        layout.addWidget(frame)

        # Add a label to the layout
        label = QLabel('Upload client_secret.json File', self)
        label.setStyleSheet("font-size: 16px; font-weight: bold; color: black;")
        layout.addWidget(label, alignment=Qt.AlignCenter)

        # Create upload button
        upload_button = QPushButton('Upload File', self)
        upload_button.setStyleSheet("font-size: 14px; color: white; background-color: black; border-radius: 10px;")
        upload_button.clicked.connect(self.upload_file)
        upload_button.setFixedSize(200, 50)  # Set a larger size for the button
        layout.addWidget(upload_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        # Set up the application
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('File Copy App')

    def upload_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Text files (*.txt);;All Files (*)")

        # Get the path of the selected file
        file_path, _ = file_dialog.getOpenFileName(self, "Upload File", "", options=options)

        # Check if a file was selected
        if file_path:
            self.copy_file_contents(file_path)

    def copy_file_contents(self, source_file_path):
        try:
            # Read data from the source file
            with open(source_file_path, 'r') as source_file:
                data = source_file.read()

            if data:
                # Open 'env.txt' in write mode to clear its contents
                with open('env.txt', 'w') as clear_file:
                    clear_file.truncate()

                # Append data to the 'env.txt' file
                with open('env.txt', 'a') as target_file:
                    target_file.write(data)

            # No need to display a success message or handle empty file case

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileCopyApp()
    window.show()
    sys.exit(app.exec_())
