import sys
import cv2
import numpy as np
import textwrap
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QVBoxLayout,
    QPushButton, QLabel, QGridLayout, QFrame, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPixmap, QIcon, QPalette, QColor
from PyQt5.QtCore import QSize, Qt
import webbrowser
import selection
import concatinate_video
import marge_song
import videoplay
from login import LoginForm
from feedback import FeedbackForm
from upload import Upload


class ScriptGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Set a clean and professional color palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))  # White background
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))     # Black text
        palette.setColor(QPalette.Button, QColor(0, 0, 0))         # Black buttons
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))  # White button text
        palette.setColor(QPalette.Base, QColor(200, 200, 200))  # Light gray base color
        palette.setColor(QPalette.AlternateBase, QColor(220, 220, 220))  # Slightly darker alternate base color
        self.setPalette(palette)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Automate video Maker Application")
        self.setGeometry(100, 100, 500, 650)

        layout = QVBoxLayout(self)

        nav = QFrame(self)
        nav.setGeometry(0, 0, 1000, 50)
        nav.setStyleSheet('background-color: #001F3F; color:#CCCCCC;')

        nav_layout = QHBoxLayout(nav)

        # opeining data.txt file and rendring name
        with open('data.txt', 'r') as file:
            content = file.read()

        # Find the index of "Name:" in the file contents
        name_index = content.find("Name:")

        # Extract the name based on the known format
        if name_index != -1:
            name_line = content[name_index:]
            name_txt = name_line.split(':')[1].strip()

            # Display the name
            name = QLabel(f"Hello, {name_txt}", nav)
            name.setStyleSheet("font-size: 24px; color: white; margin-left: 10px;")
            nav_layout.addWidget(name)
        else:
            name = QLabel("Unknown", nav)
            name.setStyleSheet("font-size: 24px; color: white; margin-left: 10px;")
            nav_layout.addWidget(name)
            print("Name not found in the file.")

        contact = QPushButton("Contact us", nav)
        contact.clicked.connect(self.contact)
        contact.setStyleSheet("width: 50px; background-color: yellowgreen; color: white; padding: 10px; border: 2px solid white; border-radius: 5px; margin-left: 10px;")
        nav_layout.addWidget(contact)

        layout.addWidget(nav)

        feedback = QPushButton("FeedBack", nav)
        feedback.clicked.connect(self.feedback)
        feedback.setStyleSheet("width: 50px; background-color: blue; color: white; padding: 10px; border: 2px solid white; border-radius: 5px; margin-left: 10px;")
        nav_layout.addWidget(feedback)

        layout.addWidget(nav)

        logout_button = QPushButton("Logout", nav)
        logout_button.clicked.connect(self.log)
        logout_button.setStyleSheet("width: 50px; background-color: red; color: white; padding: 10px; border: 2px solid white; border-radius: 5px; margin-left: 10px;")
        nav_layout.addWidget(logout_button)
        logout_button.hide()


        login_button = QPushButton("LogIn", nav)
        login_button.clicked.connect(self.log)
        login_button.setStyleSheet("width: 50px; background-color: coral; color: white; padding: 10px; border: 2px solid white; border-radius: 5px; margin-left: 10px;")
        nav_layout.addWidget(login_button)
        login_button.hide()

        layout.addWidget(nav)
        file_path = "data.txt"
        try:
            with open(file_path,'r') as file :
                data = file.read()
                if data:
                    login_button.hide()
                    logout_button.show()
                else:
                    print("no data")
                    logout_button.hide()
                    login_button.show()
        except Exception as e:
            print(f"an error occupied : {e}")

        # Script input
        script_label = QLabel("Enter your video script:", self)
        script_label.setFont(QFont("Arial", 12, QFont.Bold))
        script_label.setStyleSheet("margin-top:20px;")
        layout.addWidget(script_label)

        self.script_text = QTextEdit(self)
        self.script_text.setFont(QFont("Arial", 10))
        self.script_text.setAcceptRichText(False)
        layout.addWidget(self.script_text)

        # Category selection
        self.selectedCategoryLabel = QLabel("Selected category", self)
        self.selectedCategoryLabel.setFont(QFont("Arial", 12))
        self.selectedCategoryLabel.setStyleSheet("font-weight:bold;")
        layout.addWidget(self.selectedCategoryLabel)


        categories = ["Nature", "Anime", "Galaxy", "Love", "Motivation", "Education"]
        images = ["Nature.jpg", "Anime.jpg", "Galaxy.jpg", "Love.jpg", "Motivation.jpg", "Education.jpg"]

        grid_layout = QGridLayout()

        for idx, category in enumerate(categories):
            button_container = QWidget(self)
            button_layout = QVBoxLayout(button_container)

            label = QPushButton(self)
            pixmap = QPixmap(images[idx]).scaled(QSize(100, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            label.setIcon(QIcon(pixmap))
            label.setIconSize(QSize(100, 100))
            label.setStyleSheet("border: none;")
            label.clicked.connect(lambda checked, category=category: self.category_button_clicked(category))

            

            category_label = QLabel(category, self)
            category_label.setAlignment(Qt.AlignCenter)
            category_label.setFont(QFont("Arial", 10))

            button_layout.addWidget(label)
            button_layout.addWidget(category_label)

            button_container.setLayout(button_layout)

            grid_layout.addWidget(button_container, idx // 2, idx % 2)

        layout.addLayout(grid_layout)

        # Submit button
        submit_button = QPushButton("Generate", self)
        submit_button.clicked.connect(self.submit_script)
        submit_button.setFont(QFont("Arial", 12, QFont.Bold))
        submit_button.setStyleSheet("background-color: black; color: white; padding: 10px; border: 2px solid white; border-radius: 5px;")
        layout.addWidget(submit_button)

        # Output text
        self.output_txt = QTextEdit(self)
        self.output_txt.setReadOnly(True)
        self.output_txt.setFont(QFont("Arial", 10))
        self.output_txt.setStyleSheet("background-color: white; color: black; border: 2px solid black; border-radius: 5px; padding: 10px;")
        layout.addWidget(self.output_txt)

       # Play Video button (initially hidden)
        self.play_button = QPushButton("Play Video", self)
        self.play_button.clicked.connect(self.playVid)
        self.play_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.play_button.setStyleSheet("width: 50px; background-color: coral; color: white; border: 2px solid black; border-radius: 5px; padding: 10px;")
        self.play_button.hide()

        # Upload Video button (initially hidden)
        self.upload_button = QPushButton("Upload Video", self)
        self.upload_button.clicked.connect(self.uploadVid)
        self.upload_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.upload_button.setStyleSheet("width: 50px; background-color: #CD201F; color: white; border: 2px solid black; border-radius: 5px; padding: 10px;")
        self.upload_button.hide()

        # Create a QHBoxLayout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.upload_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

    def category_button_clicked(self, category):
        print(f"Category button clicked: {category}")
        self.selectedCategory = category
        self.selectedCategoryLabel.setText(f"Selected category: {category}")

    def log(self):
        self.close()
        self.login_form = LoginForm()
        self.login_form.show()
        print("Logout") 

        

    def feedback(self):
        self.close()
        self.feedback = FeedbackForm()
        self.feedback.show()

    @staticmethod
    def contact():
        whatsapp_url = "https://api.whatsapp.com/send/?phone=9503170450&text&type=phone_number&app_absent=0"
        webbrowser.open(whatsapp_url)




    def submit_script(self):
        try:
            script_content = self.script_text.toPlainText()
            selected_category = self.selectedCategory 

            script = script_content.split(", ")

            num = len(script)

            print("Script Content:", script_content)
            print("Selected Category :", selected_category)

            self.output_txt.setPlainText(f"Script Content: {script_content}\n")
            self.output_txt.append(f"{selected_category}\n")
            self.output_txt.append("Output will be displayed here !!\n")
            self.output_txt.append("-" * 50 + "\n")

            selected, song_name = selection.select_video(num, selected_category)
            self.output_txt.append("-" * 50 + "\n")
            self.output_txt.append(f"The Videos Selected to be concatenated: {selected}\n")
            self.output_txt.append("-" * 50 + "\n")

            concatinate_video.concatinate(selected)

            video_path = 'concatinated_video.mp4'
            cap = cv2.VideoCapture(video_path)

            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            output_path = 'output_video.avi'
            out = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

            text_messages = script
            current_text_index = 0
            text_duration_seconds = 3
            frame_rate = 28
            text_duration_frames = int(text_duration_seconds * frame_rate)
            current_text_frame_counter = 0

            opacity_duration_frames = 15 * fps
            max_opacity = 255

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                text_frame = np.zeros_like(frame)

                wrapped_text = textwrap.fill(text_messages[current_text_index], width=30)
                wrapped_text_lines = wrapped_text.split('\n')
                text_x_position = int((frame.shape[1] - len(wrapped_text_lines[0]) * 15) / 2)
                text_y_position = int(frame.shape[0] / 2)

                if current_text_frame_counter < opacity_duration_frames:
                    opacity = int((current_text_frame_counter / opacity_duration_frames) * max_opacity)
                elif current_text_frame_counter >= text_duration_frames - opacity_duration_frames:
                    opacity = int(((text_duration_frames - current_text_frame_counter) / opacity_duration_frames) * max_opacity)
                else:
                    opacity = max_opacity

                text_color = (252, 252, 252, opacity)
                for line in wrapped_text_lines:
                    cv2.putText(text_frame, line, (text_x_position, text_y_position), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
                    text_y_position += 40

                frame_with_text = cv2.addWeighted(frame, 1, text_frame, 1, 0)

                out.write(frame_with_text)

                current_text_frame_counter += 1

                if current_text_frame_counter >= text_duration_frames:
                    current_text_index += 1
                    current_text_frame_counter = 0

                if current_text_index >= len(text_messages):
                    break

            cap.release()
            out.release()

            self.output_txt.append("-" * 50 + "\n")
            self.output_txt.append(f"Video processing complete. The output video is saved as: {output_path}\n")
            self.output_txt.append("-" * 50 + "\n")

            marge_song.marge(song_name)
            self.output_txt.append(f"The Final Video Is Generated: {output_path}\n")

            self.play_button.show()
            self.upload_button.show()
            layout = self.layout()
            layout.addWidget(self.play_button)
            layout.addWidget(self.upload_button)

        except Exception as e:
            print(f"Error: {e}")

    def playVid(self):
        print("Playing Video")
        self.output_txt.append("Playing The Video In Chrome Tab ")
        self.output_txt.append("Wait More 5 Sec...! ")
        videoplay.play_video_in_browser()

    def uploadVid(self):
        print ("upload")
        self.close()
        self.upload = Upload()
        self.upload.show()

def main():
    app = QApplication(sys.argv)
    window = ScriptGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
