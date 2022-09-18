def calculate_download(size, download_speed):
    time = (size / download_speed) * 60
    print(f"Download levará: {time} min")


calculate_download(200, 50)
calculate_download(500, 50)

calculate_download(200, 100)
calculate_download(500, 100)