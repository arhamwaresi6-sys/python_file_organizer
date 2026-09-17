import os
import shutil
imageExt = [
    "jpg",
    "jpeg",
    "png",
    "gif",
    "webp",
    "bmp",
    "svg",
    "tiff",
    "tif",
    "heic",
    "heif",
    "avif",
    "ico",
    "psd",
    "raw",
]
paths = {
    "img": "C:/Downloads/Images",
    "cpp": "C:/Projects/c++",
    "c": "C:/Projects/c",
    "py": "C:/Projects/python",
    "js": "C:/Projects/javascript",
    "html": "C:/Projects/html",
    "css": "C:/Projects/css",
    "pdf": "C:/Downloads/Documents"
}
# path generator
def find_path(a):
    return paths[a]


def create_folder(item):
    extension = os.path.splitext(item)[1].lower().strip(".")
    path = f"C:/Projects/{extension}_file_organizer"
    os.makedirs(path,exist_ok=True)
    if not(os.path.exists(path + f"/{item}")):
     item = os.path.join("..",item)
     shutil.move(item,path)


def extension_check(item):
       extension = os.path.splitext(item)[1].lower().strip(".")
       if extension in imageExt:
          return find_path("img")
       elif extension == "cpp":
          return find_path("cpp")
       elif extension == "c":
          return find_path("c")
       elif extension == "py":
          return find_path("py")
       
items = os.listdir("..")

for item in items:
    if not(os.path.isfile("../"+item)):
        continue

    path = extension_check(item)
    if path != None:
      item = os.path.join("..",item)
      shutil.move(item,path)   
    else:
        create_folder(item)    
#modifyed