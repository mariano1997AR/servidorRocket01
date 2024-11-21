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
     # Leer el dato enviado desde el cliente
    data = request.json  # Flask espera un JSON
    mensaje = data.get('accion', '')  # Obtener el valor del campo "accion"

    if mensaje == 'crear':
        # Crear el documento PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.cell(200, 10, txt="Este es tu documento generado.", ln=True, align='C')

        # Guardar el PDF temporalmente
        file_path = 'documento.pdf'
        pdf.output(file_path)

        # Enviar el archivo como respuesta
        response = send_file(file_path, as_attachment=True)

        # Agregar eliminación del archivo tras enviar la respuesta
        @response.call_on_close
        def remove_file():
            if os.path.exists(file_path):
                os.remove(file_path)

        return response
    elif mensaje.lower() == 'saludar'.lower():
        # Responder con el mensaje recibido 
        respuestaSaludar = "Hola rocket te saluda"
        print(respuestaSaludar)
        return jsonify({"mensaje": f" {respuestaSaludar}"}), 200
    


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

    
    