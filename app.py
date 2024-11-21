from flask import Flask, jsonify, request,send_file
from flask_cors import CORS
from fpdf import FPDF
import os

app = Flask(__name__)
CORS(app) # Esta habilita CORS para todas las rutas

#Ruta GET para recibir datos

# Ruta POST para recibir datos desde React y enviar una respuesta
@app.route('/api/submitdata',methods=['POST'])
def submit_data():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"message":"No data received"}),400
        print("Datos recibidos", data)
        
        nombre = data.get('nombre')
        email = data.get('email')
        
        print(f"Nombre:{nombre} Email: {email}")
        
        return jsonify({"message":"Datos procesados correctamente","data":data}),200
    
    except Exception as e:
        return jsonify({"error":str(e)}),500
  
    



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 5000 como fallback local
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
    
    