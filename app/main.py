"""Main."""

from fastapi import FastAPI, File, UploadFile
from pathlib import Path

from fastapi.responses import FileResponse


app = FastAPI()


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/upload/")
# the File(...) expression below makes FastApi aware that a file is required to process the request
async def upload_image(file: UploadFile = File(...)):
    #Create path to store uploaded file and use the filename for processing
    filepath = UPLOAD_DIR / file.filename

    # Save the uploaded file
    with filepath.open("wb") as fp:
        fp.write(file.file.read())
    return {"filename": file.filename}

@app.get("/image/{filename}")
async def get_image(filename: str):
    filepath = UPLOAD_DIR / filename
    if not filepath.exists():
        return {"error": "File not found"}
    return FileResponse(filepath)

@app.get("/images/")
async def list_images():
    # Get all items from the folder
    all_items = UPLOAD_DIR.iterdir()

    #Filter files:
    file_names = []
    for item in all_items:
        if item.is_file():
            file_names.append(item)

    return {"files": file_names}
