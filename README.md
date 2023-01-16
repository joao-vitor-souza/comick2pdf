## How to use it

`comick2pdf` is a Python script that converts images downloaded from [comick.app](https://comick.app/home) into a PDF version of your desired manga. Supposing that you have Python downloaded on your machine, you'll need to install `Pillow` package before running this tool, to do this just open a terminal window and type:

```bash
pip install Pillow
```

After that, [download](https://github.com/joao-vitor-souza/comick2pdf/archive/refs/heads/main.zip) the script or clone this repository with:

```bash
git clone https://github.com/joao-vitor-souza/comick2pdf
```

Still on your terminal, move to the folder where you just downloaded/cloned the script. You can use `cd` command for that. Now, inside the folder, enter:

```bash
python comick2pdf.py path/to/images
```

Replace `path/to/images` with the path where the manga images are located; and there you go, a manga in PDF has been created inside the folder `pdf`.

## Example

Let's say you want a PDF version of [Chainsaw Man Chapter 1](https://comick.app/comic/chainsaw-man-digital-colored-comics?lang=en). First, download the manga images by clicking in the button inside the red circle:

![download](https://user-images.githubusercontent.com/90481938/212583211-3ae7b4c3-59ef-459d-ba77-885cb1d671c6.png)

I downloaded the images and unziped them to `/home/joao/Downloads/chainsaw-man-digital-colored-comics-1/`. Now, in the terminal, open the directory of the folder where the script is located and run:

![convertion](https://user-images.githubusercontent.com/90481938/212584302-70317f13-c02f-4196-9c01-b3566f6eb1cf.png)

That's it! If I go where the images are, there'll be a folder called `pdf`:

![pdf-folder](https://user-images.githubusercontent.com/90481938/212585081-dae1c2ea-a128-4ac1-98fe-1314c7f76872.png)

And inside it, it's the PDF of the manga itself:

![pdf](https://user-images.githubusercontent.com/90481938/212585278-84ae5993-bcef-40d4-b751-13628adf30a5.png)

Now, you can delete the images if you want to, they won't be useful anymore.
