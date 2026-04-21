from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui' # Necesaria para mensajes flash

@app.route("/")
def index():
    # Información ficticia de la empresa de servicios (ej. Arquitectura o Sistemas)
    servicios = [
        {"nombre": "Consultoría Técnica", "desc": "Asesoramiento especializado en proyectos."},
        {"nombre": "Diseño Estructural", "desc": "Planificación y ejecución de infraestructura."},
        {"nombre": "Desarrollo de Software", "desc": "Soluciones digitales a medida."}
    ]
    return render_template('index.html', servicios=servicios)

@app.route("/contacto", methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Captura de datos del formulario
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        
        # Aquí podrías guardar en base de datos o enviar un correo
        flash(f"Gracias {nombre}, hemos recibido tu mensaje con éxito.", "success")
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

if __name__ == "__main__":
    # Usar el puerto que asigne Render o el 5000 por defecto localmente
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)