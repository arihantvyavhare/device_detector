
# %%
from fastai.vision.all import *
import gradio as gr








# %%
learn = load_learner('export.pkl')

# %%
categories = ('desktop pc','laptop','mobile phone')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %%
image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label()
examples = ['dell 20.jpg', 'dell inspiron.jpg', 'desktop pc on table.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)

# %%
## end -
