import os
import sys
from pathlib import Path

from PIL import Image

try:

    class C:
        b = "\033[94m"
        y = "\033[93m"
        g = "\033[92m"
        e = "\033[0m"

    try:
        path = Path(sys.argv[1])
        os.chdir(path)
    except IndexError:
        print(C.y + "No path was passed!" + C.e)
        sys.exit(1)
    except FileNotFoundError:
        print(C.y + "Invalid path!" + C.e)
        sys.exit(1)

    images = os.listdir(".")
    if "pdf" in images:
        images.remove("pdf")

    print(C.b + "\nConverting..." + C.e)

    images.sort(key=lambda x: int(x.split(".")[0]))
    cover = Image.open(images[0]).convert("RGB")
    image_list = [Image.open(image).convert("RGB") for image in images[1:]]

    if not os.path.exists(path / Path("pdf")):
        os.mkdir(path / Path("pdf"))

    cover.save(f"pdf/{path.parts[-1]}.pdf", save_all=True, append_images=image_list)
except KeyboardInterrupt:
    print(C.y + "\nInterruption Detected! Program Closed!" + C.e)
    sys.exit(0)
else:
    print(C.g + "\nConvertion Completed!")
    print(C.b + f"\nThe PDF is located in the pdf folder created at {C.e}{path}\n")
