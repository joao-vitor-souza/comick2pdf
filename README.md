## How to use it

`comick2pdf` is a tool to download PDF versions of your desired mangas from [comick.app](https://comick.app/home). Setting up this tool is pretty easy. Supposing that you have Python downloaded on your machine, open a terminal window and type:

```bash
pip install Pillow, requests
```

After that, [download](https://github.com/joao-vitor-souza/comick2pdf/archive/refs/heads/main.zip) or clone this repository with:

```bash
git clone https://github.com/joao-vitor-souza/comick2pdf
```

Open the file called `env_paths.py` and fill the 2 variables:

```python
# Where the files you're going to download from the WEB will be stored.
DOWNLOAD_PATH = ""
# Where the PDF file will be stored.
OUTPUT_PATH = ""


"""
Example:

DOWNLOAD_PATH = "/home/joao/Downloads/"
OUTPUT_PATH = "/home/joao/Mangas/"
"""
```

Now, still on your terminal, move to the folder where you just downloaded/cloned the repository. You can use `cd` command for that. Inside the folder, enter:

```bash
python comick2pdf.py https://comick.app/comic/your-desired-manga pdf_name
```

Replace `https://comick.app/comic/your-desired-manga` with the URL of the manga you want. You can also give a name to the PDF file by replacing `pdf_name`; if no name is passed, then a default name is used. After that, a window in your browser will be opened and it'll download the manga images; you must place them in the same path as in the `DOWNLOAD_PATH`. After that, the script will take care of unzipping the images, building the PDF, moving it to the `OUTPUT_PATH`, and cleaning temporary files.

## Example

Let's say you want a PDF version of [Chainsaw Man Chapter 1](https://comick.app/comic/chainsaw-man-digital-colored-comics/6pk0z-chapter-1-en). First, you'll need to define the paths, in my case, they are:

```python
DOWNLOAD_PATH = "/home/joao/Downloads/"
OUTPUT_PATH = "/home/joao/Mangas/"
```

Now, open your terminal in the repository folder and type:

```bash
python comick2pdf.py https://comick.app/comic/chainsaw-man-digital-colored-comics/6pk0z-chapter-1-en CSM-Chapter-1
```
![convertion](https://user-images.githubusercontent.com/90481938/213005542-ff28783f-6308-4896-a591-a3f36ed216d9.png)

You'll be prompted with a download tab asking where you want to download the images; in my case, I'm going to download them to `"/home/joao/Downloads/"`.

After some seconds the PDF will be created at `"/home/joao/Mangas/"`:

![pdf](https://user-images.githubusercontent.com/90481938/213005485-51991190-aeb6-4634-ac60-b6b32db1f8ba.png)
