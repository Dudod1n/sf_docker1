import requests

def download_favicon(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            favicon_url = url + "/favicon.ico"
            response = requests.get(favicon_url)
            with open("favicon.ico", "wb") as f:
                f.write(response.content)
            print("Favicon downloaded successfully")
        else:
            print("Failed to get website content")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    download_favicon("https://www.youtube.com/")