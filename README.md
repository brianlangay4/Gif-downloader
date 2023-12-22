# Gif-downloader

![my_new_gif](https://github.com/brianlangay4/Gif-downloader/assets/67788456/56362910-78db-43da-9efe-a7b114f7e2bf)


### Introduction

The `download_gif` script is a Python program designed to download GIF files from a given URL and save them to a specified location. It utilizes the `requests` library for making HTTP requests and the `os` library for file and path manipulation.

### Usage

To use the script, you need to provide a valid GIF URL and specify a filename for saving the downloaded GIF. The example usage section at the end of the script demonstrates how to invoke the `download_gif` function with a sample GIF URL and save filename.

### Functionality

1. **Download GIF Functionality:**
   - The `download_gif` function takes a GIF URL and a save path as its parameters.
   - It uses the `requests.get` method to fetch the GIF content from the specified URL.
   - The response status is checked for success using `response.raise_for_status()`.
   - The script then constructs the full path to save the GIF in the "Downloads" folder.
   - The GIF content is written to the specified file using a binary write mode ('wb').
   - A success message is printed if the download is completed successfully.

2. **Example Usage:**
   - A sample GIF URL and save filename are provided in the example usage section.
   - Users can replace the `gif_url` and `save_filename` variables with their desired values.
   - The script will download the GIF from the specified URL and save it with the given filename.

### Error Handling

- If an error occurs during the download process, the script catches `requests.exceptions.RequestException` and prints an error message.

### Recommendations

- Users are encouraged to replace the sample GIF URL and filename with their desired values.
- Ensure that the specified folder for saving the GIF is accessible and has write permissions.
- Consider adding additional error handling or logging based on specific use-case requirements.

### Example Usage

```python
# Example usage:
# Put the GIF link here
gif_url = 'https://media.giphy.com/media/UCTaYoiR7pD2okgFK1/giphy.gif'
# You can change the name to your liking
save_filename = 'my_gif.gif'

download_gif(gif_url, save_filename)
```

### Conclusion

The `download_gif` script provides a simple and modular way to download GIFs from the internet, allowing users to customize the URL and save location according to their needs.
i will advance it into mobile app in the coming future projects
--- 
