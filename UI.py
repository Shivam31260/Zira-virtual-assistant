import cv2
import imageio

def play_gif(gif_path):
    # Read the GIF file
    gif = imageio.get_reader(gif_path)

    # Create a window
    cv2.namedWindow("GIF", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("GIF", 600, 600)

    # Display the GIF frame by frame
    try:
        for frame in gif:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow("GIF", frame)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
    except RuntimeError:
        pass

    # Close the window
    cv2.destroyAllWindows()

# Path to the GIF file
gif_path = 'face.gif'

# Call the function to play the GIF
play_gif(gif_path)
