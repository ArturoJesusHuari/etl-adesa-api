from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello world!"}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))
        
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
            "info": str(df.info())
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))