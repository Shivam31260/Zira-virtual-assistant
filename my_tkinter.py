
# for mp4 to gif
# from moviepy.editor import VideoFileClip

# def convert_to_gif(input_file, output_file):
#     clip = VideoFileClip(input_file)
#     clip.write_gif(output_file)

# # Replace "C:\\Users\\DELL\\Desktop\\zira\\watermarked_preview.mp4" with the path to your input MP4 file
# # Replace "C:\\Users\\DELL\\Desktop\\zira\\face.gif" with the desired path for the output GIF file
# convert_to_gif("C:\\Users\\DELL\\Desktop\\zira\\watermarked_preview.mp4", "C:\\Users\\DELL\\Desktop\\zira\\face.gif")
import tkinter as tk
from PIL import Image, ImageTk
import threading
import queue

class VideoApp(tk.Tk):
    def __init__(self, gif_path):
        super().__init__()

        self.title("AI Assistant")
        self.geometry("800x600")

        # Load GIF file
        self.gif = Image.open(gif_path)
        self.gif_frames = self.get_frames(self.gif)

        # Create a label to display the GIF
        self.label = tk.Label(self)
        self.label.pack()

        # Queue to pass frames between threads
        self.queue = queue.Queue()

        # Start the worker thread
        self.worker_thread = threading.Thread(target=self.process_frames)
        self.worker_thread.daemon = True
        self.worker_thread.start()

        # Start the animation
        self.animate()

    def get_frames(self, gif):
        frames = []
        try:
            while True:
                frames.append(gif.copy())
                gif.seek(len(frames))  # Go to next frame
        except EOFError:
            pass
        return frames

    def process_frames(self):
        for frame in self.gif_frames:
            photo = ImageTk.PhotoImage(frame)
            self.queue.put(photo)
            import time
            time.sleep(0.1)  # Sleep to control the speed of the animation

    def animate(self):
        try:
            photo = self.queue.get_nowait()
            self.label.config(image=photo)
            self.label.image = photo
            self.after(100, self.animate)
        except queue.Empty:
            self.after(100, self.animate)

if __name__ == "__main__":
    # Replace "face.gif" with the path to your GIF file
    app = VideoApp("face.gif")
    app.mainloop()
