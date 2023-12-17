# Import necessary libraries
import tkinter as tk  # GUI library
from tkinter import messagebox  # For displaying message boxes
from pytube import YouTube  # Library to work with YouTube videos
import os  # Operating System module for file operations

# Function to open the main window of the application
def open_main_window():
    # Function to download the video from the provided URL
    def download_video():
        # Get the URL from the entry field
        url = url_entry.get()
        if url:
            try:
                # Create a YouTube object using the provided URL
                yt = YouTube(url)
                # Get the highest resolution stream available
                video = yt.streams.get_highest_resolution()
                # Download the video
                video.download()
                # Show a success message upon successful download
                messagebox.showinfo("Download Successful", "Video downloaded successfully!")
            except Exception as e:
                # Show an error message if there's an issue with downloading
                messagebox.showerror("Error", f"Error downloading video: {str(e)}")
        else:
            # Show an error message if no URL is entered
            messagebox.showerror("Error", "Please enter a YouTube URL.")

    # Function to clear the entry field
    def clear_entry():
        url_entry.delete(0, tk.END)

    # Create the main window
    main_window = tk.Tk()
    main_window.geometry("720x480")  # Set window size
    main_window.title("YouTube Downloader")  # Set window title

    # Get the directory path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define paths for images
    img1_path = os.path.join(script_dir, "concert.gif")
    img2_path = os.path.join(script_dir, "Risk.jpeg")

    # Check if image files exist and are supported
    if os.path.exists(img1_path) and os.path.exists(img2_path):
        # Load images if they exist
        img1 = tk.PhotoImage(file=img1_path)
        img2 = tk.PhotoImage(file=img2_path)

        # Create labels to display images
        label_img1 = tk.Label(main_window, image=img1)
        label_img1.pack()

        label_img2 = tk.Label(main_window, image=img2)
        label_img2.pack()
    else:
        print("Image files not found or unsupported format")

    # Function to open the download window
    def open_download_window():
        # Create a new window (Toplevel) for download
        download_window = tk.Toplevel(main_window)
        download_window.geometry("720x480")  # Set window size
        download_window.title("Download Window")  # Set window title

        # Label for entering YouTube URL
        label1 = tk.Label(download_window, text="Enter YouTube URL:")
        label1.pack()

        global url_entry  # Declare the entry field as global
        url_entry = tk.Entry(download_window, width=40)  # Entry field for URL
        url_entry.pack()

        # Button to initiate download
        download_btn = tk.Button(download_window, text="Download", command=download_video)
        download_btn.pack(pady=10)

        # Button to clear the entry field
        clear_btn = tk.Button(download_window, text="Clear", command=clear_entry)
        clear_btn.pack(pady=5)

    # Button to open the download window
    open_download_btn = tk.Button(main_window, text="Open Download Window", command=open_download_window)
    open_download_btn.pack(pady=20)

    # Function to exit the application
    def exit_app():
        main_window.destroy()

    # Button to exit the application
    exit_btn = tk.Button(main_window, text="Exit", command=exit_app)
    exit_btn.pack(pady=10)

    # Start the main event loop
    main_window.mainloop()

# Call the function to open the main window of the application
open_main_window()
