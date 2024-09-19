import csv
import os #MANEJO CARPETAS
import time #CAMBIAR NOMBRE ARCHIVO
from flask import Flask, jsonify, request, send_from_directory, send_file
from flask_cors import CORS

# pip install Flask
# pip install Flask-Cors

# VARIOS IP LISTA BLANCA
app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# CARPETA_IMG="img"
# CARPETA_SOUND="sound"
ARCHIVO_CSV="datos_aves.csv"

# Creación carpetas
# for carpeta in [CARPETA_IMG, CARPETA_SOUND]:
#     os.makedirs(carpeta, exist_ok=True)

# # RUTAS carpetas creadas
# app.config["CARPETA_IMG"]=CARPETA_IMG
# app.config["CARPETA_SOUND"]=CARPETA_SOUND


def leerCsv():
    aves={}

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo)

                    # for data_df, row in df.iterrows():
            for row in lector:
                id_ave=int(row["ID"])

                if id_ave not in aves:
                    aves[id_ave]= {
                        "id": id_ave,
                        "nombre": row["Nombre"], 
                        "tamano": float(row["Tamaño"]) if row["Tamaño"] else None, #TERNARIO OPERADOR IZQUIERDA TRUE DERECHA FALSE if por si no hay archivo y evitar romper la API
                        "color": row["Color"],
                        "caracteristica": row[ "Caracteristica"],
                        "comportamiento": row[ "Comportamiento"],
                        "fotos": row[ "Fotos"].split(", ") if row["Fotos"] else [], #TERNARIO OPERADOR IZQUIERDA TRUE DERECHA FALSE - if por si no hay archivo y evitar romper la API
                        "sonidos": row[ "Sonidos"].split(", ") if row["Sonidos"] else [], #TERNARIO OPERADOR IZQUIERDA TRUE DERECHA FALSE  if por si no hay archivo y evitar romper la API
                        "observaciones": [ ] 
                    }

                aves[id_ave]["observaciones"].append({
                    "fecha": row["Fecha"],
                    "lugar": row["Lugar"],
                    "avistamientos": float(row["Avistamientos"]) if row["Avistamientos"] else None
                    })
    return aves

# el FRONT siempre necesita una ruta
# 190.2.3.5.5500/aves

@app.route("/aves/", methods=["GET"]) 
def obtener_aves():
    aves= leerCsv()
    datosAves=list(aves.values())
    # CONVERTIR a JASON
    return jsonify(datosAves)

@app.errorhandler(500)
def errorInterno():
    return jsonify({"error": "Ocurrió un error interno del servidos" }), 500

@app.errorhandler(404)
def noEncontrado():
    return jsonify({"error": "Recurso no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)



























































