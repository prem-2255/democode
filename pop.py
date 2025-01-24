import tkinter as tk
from PIL import Image, ImageTk
import cv2

# Create the main window
root = tk.Tk()
root.title("Photo Pop-up")

# Create a frame to hold the images
frame = tk.Frame(root)
frame.pack()

# Load the images
images = []
for i in range(5):
    img = Image.open(f"image_{i+1}.jpg")
    img.thumbnail((200, 200))  # Resize the image
    img_tk = ImageTk.PhotoImage(img)
    images.append(img_tk)

# Create a label to display the images
label = tk.Label(frame, image=images[0])
label.pack()

# Create a button to cycle through the images
def cycle_images():
    current_index = images.index(label.cget("image"))
    next_index = (current_index + 1) % len(images)
    label.config(image=images[next_index])

button = tk.Button(frame, text="Next", command=cycle_images)
button.pack()

# Create a button to play a video
def play_video():
    video = cv2.VideoCapture("video.mp4")
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

video_button = tk.Button(frame, text="Play Video", command=play_video)
video_button.pack()

# Start the GUI event loop
root.mainloop()