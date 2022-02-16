import os

def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("main.py")

    createFolder('Images')
    createFolder('Docs')
    createFolder('Audios')
    createFolder('Videos')
    createFolder('Others')

    imgExts = [".png", ".jpg", ".jpeg", ".jfif", ".svg", ".webp", ".gif"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", ".doc", ".pdf", ".htm", ".html", ".ppt", ".pptx", ".xls", ".xlsx"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    audioExts = [".aac", ".mp3", ".wav", ".wma"]
    audios = [file for file in files if os.path.splitext(file)[1].lower() in audioExts]


    videoExts = [".mpeg-1", ".mpeg-2", ".mpeg-4", ".avi", ".mov", ".mkv", ".mp4"]
    videos = [file for file in files if os.path.splitext(file)[1].lower() in videoExts]


    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in audioExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in videoExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Audios", audios)
    move("Videos", videos)
    move("Others", others)