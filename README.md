# Stable-CAD-Generator
Innovative CAD generator using Stable Diffusion

# Description
Uses the newly published Stable Diffusion model to generate CAD models/blueprints.

For image recognition/classification the model tensorflow is used.

For UI the module tkinter is used.

# Installation 
pip3 install -r requirements.txt

# Usage
python3 main.py

# Notes
You must have a good internet connection since an api is being called.

You must provide a CAD model or a blueprint otherwise it will generate incorrect results.

If it does not generate the desired results make sure the images are in RGB mode.(optional)

Use the example.png as a test image to generate sample output.

# Possible errors
If it gives an error during installation make sure your Python version is before 3.11 since
the new one is conflicting the packages.

Tested on Python 3.10/3.10.8.
If tensorflow throws an AVX instruction error that means that your CPU is not supported.
Please check if your CPU supports AVX https://10scopes.com/cpu-support-avx/.

If an error occurs while generating the image after the recognition, 
please check if you added your api key on line 16.

To get a new API key please visit https://beta.dreamstudio.ai/membership .

# Sources/Modules used
https://numpy.org/ (used for expanding the dimensions of the image)

https://www.tensorflow.org/ (image classification)

https://beta.dreamstudio.ai/ (the api that generates the new image, limited to about 124)

https://docs.python.org/3/library/tkinter.html (the library used for the UI)

https://pillow.readthedocs.io/ (used for displaying the images)
