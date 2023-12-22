import os
import requests

def download_gif(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Get the path to the "Downloads" folder
        #you can replace with your location folder that you want to save thd Gif
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

        # Create the full path to save the GIF in the "Downloads" folder
        save_path = os.path.join(downloads_path, save_path)

        with open(save_path, 'wb') as gif_file:
            gif_file.write(response.content)

        print(f"GIF downloaded successfully and saved at: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading GIF: {e}")

# Example usage:
#put the gif link here
gif_url = 'https://media.giphy.com/media/UCTaYoiR7pD2okgFK1/giphy.gif'
#you can change name to your liking
save_filename = 'my_gif.gif'

download_gif(gif_url, save_filename)



