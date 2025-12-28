from PIL import Image, ImageTk
import tkinter as tk


window = tk.Tk()
window.title("Image Swap Timer")

image1 = Image.open("C:/Users/patel/OneDrive/Desktop/wix images/catto_close.png").resize((300, 200))
image2 = Image.open("C:/Users/patel/OneDrive/Desktop/wix images/catto_open.png").resize((300, 200))

photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)

photos = [photo1, photo2]
current_image = 0

image_label = tk.Label(image=photos[current_image])
image_label.pack()


tk.Label(window, text="Enter time (seconds):").pack()

time_entry = tk.Entry(window)
time_entry.pack()

time_left = time_entry.get()

timer_label = tk.Label(window, text=f"Time: {time_left}", font=("century gothic", 20))
timer_label.pack()

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time: {time_left}")
        window.after(1000, update_timer)
        def swap_image():
            global current_image
            current_image = (current_image + 1) % 2
            image_label.config(image=photos[current_image])

        window.after(1000, swap_image)
    else:
        timer_label.config(text="Time's up!")

update_timer()

window.mainloop()
