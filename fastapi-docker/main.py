# %%
from model import model_pipeline
from fastapi import FastAPI, UploadFile
from PIL import Image
import io

app = FastAPI()


# %%
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()

    # image = Image(io.BytesIO(content))
    image = Image.open(image.file)

    result = model_pipeline(text, image)
    return {"Result": result}
