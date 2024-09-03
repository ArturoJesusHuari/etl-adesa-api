from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO

app = FastAPI()

# Configurar las políticas de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Reemplaza esto con el origen de tu front-end
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

@app.get("/")
async def hello_world():
    return {"message": "Hello world!"}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents), skiprows=5)
        
        # Aquí se ejecuta el proceso ETL usando el DataFrame 'df'
        # Ejemplo de conexión y carga de datos a PostgreSQL
        # conn = psycopg2.connect(
        #     dbname="tu_base_de_datos",
        #     user="tu_usuario",
        #     password="tu_contraseña",
        #     host="localhost",
        #     port="5432"
        # )
        # cursor = conn.cursor()
        
        # # Aquí agregas tu lógica de carga de datos a PostgreSQL

        # conn.commit()
        # cursor.close()
        # conn.close()
        return {
            "filename": file.filename, 
            "message": "Archivo procesado y cargado con éxito",
            "info": str(type(df))
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))