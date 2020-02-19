# Watermark

Makespace asks members to add a notice "made@makespace" to pictures of things
they make. This directory makes that simple. Clone this repository with:

``` bash
cd <your directory>
git clone https://github.com/Makespace/Branding
```

The Python code runs on Python3 and requires OpenCV (Open Computer Vision) for
the overlay. Install it with:

```bash
python3 -m pip install opencv-python
```

Verify the installation with:

```ipython
>>> import cv2
>>> cv.__version__
'4.1.0'
```

and see [this
thread](https://stackoverflow.com/questions/44439443/python-how-to-pip-install-opencv2-with-specific-version-2-4-9)
for OpenCV installation details in Python.

Then you can add a watermark to pictures with:

``` bash
python3 add_watermark.py <path to your picture>
```

This will create another picture in the same directory with a suffix
`_makespace` and with the made@makespace logo in overlay.

Changes and pull requests welcome!

