from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse


router = APIRouter(
    prefix='/file',
    tags=['file']
)

# to upload files with .txt or docs file type
@router.post('/')
async def get_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return { 'lines': lines }

# to upload files that has a .jpeg, .png file types
@router.post('/uploadfile')
async def get_upload_file(uploadfile: UploadFile = File(...)):
    path = f"files/{uploadfile.filename}" # stores uploaded files in a static folder named files
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(uploadfile.file,buffer)
    return {
        'filename': path,
        'type' : uploadfile.content_type
    }

# to retrieve and download an image via an endpoint
@router.get('/download/{name}', response_class=FileResponse)
async def get_file(name: str):
    path = f"files/{name}"
    return path