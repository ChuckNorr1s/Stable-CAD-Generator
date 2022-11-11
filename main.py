import tkinter as tk
from tkinter import filedialog, Text,PhotoImage
from PIL import ImageTk, Image
import numpy as np
import tensorflow as tf
import io
import warnings
import os
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# NB: host url is not prepended with \"https\" nor does it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# To get your API key, visit https://beta.dreamstudio.ai/membership
os.environ['STABILITY_KEY'] = 'sk-HJZLscUmnhEwdaMUWjteNnvGmxaHgIkA4WGg9UQm6NIFPpRI'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], 
    verbose=True
)

root = tk.Tk()
root.title("Stable CAD Generator")
root.geometry('600x600')
root.resizable(False, False)

frame = tk.Frame(root, bg="#07060f")
frame.pack(expand=True, fill="both")

def check_widget():
   try:
    if(label):
        label.destroy()
   except:
    return

def check_widget1():
   try:
    if(label1):
        label1.destroy()
   except:
    return

def open():
    check_widget()
    global file
    file = filedialog.askopenfilename(initialdir="/",title="Select the image.",filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"),("jpeg files", "*.jpeg")))
    img = ImageTk.PhotoImage(Image.open(file).resize((224,224)))
    photo = PhotoImage(...)
    global label
    label = tk.Label(frame,image=img)
    label.image = img
    label.place(x=30, y=150)

"""
def generate():
    check_widget1()
    img = ImageTk.PhotoImage(Image.open(file).resize((224,224)))
    photo = PhotoImage(...)
    global label1
    #recognize(file)
    label1 = tk.Label(frame,image=img)
    label1.image = img
    label1.place(x=350, y=150)

"""

def generate():
    check_widget1()

    dog = file
   # img = ImageTk.PhotoImage(Image.open(file).resize((224,224)))
    img1 = tf.keras.preprocessing.image.load_img(dog,target_size=(224,224))

    mobile = tf.keras.applications.MobileNetV2()

    resize = tf.keras.preprocessing.image.img_to_array(img1)

    final = np.expand_dims(resize, axis = 0)

    final = tf.keras.applications.mobilenet.preprocess_input(final)

    predict = mobile.predict(final)

    results = tf.keras.applications.imagenet_utils.decode_predictions(predict)

    res = "CAD of " + results[0][0][1]
    answers = stability_api.generate(
    prompt=res,
    seed=34562, # if provided, specifying a random seed makes results deterministic
    steps=50, # defaults to 50 if not specified
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(artifact.binary)).resize((224,224)))
    
                photo = PhotoImage(...)
                global label1
                label1 = tk.Label(frame,image=img)
                label1.image = img
                label1.place(x=350, y=150)


openImg = tk.Button(frame, text="New Image",activebackground="red",activeforeground="#90EE90",highlightbackground="#101820",highlightthickness=2.5,border=4,font=1,padx=10,pady=10,foreground="#FEE715",command=open,bg="#101820")

openImg.place(x=80, y=50)

updateImg = tk.Button(frame, text=" Generate ",activebackground="red",activeforeground="#90EE90",highlightbackground="#101820",highlightthickness=2.5,border=4,font=1,padx=10,pady=10,foreground="#FEE715",command=generate,bg="#101820")

updateImg.place(x=390, y=50)

root.mainloop()