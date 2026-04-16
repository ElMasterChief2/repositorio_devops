from flask import Flask, jsonify, render_template_string
import boto3
import os
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Project - Soluciones Tecnologicas del Futuro</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0f1117; color: #ffffff; margin: 0; padding: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { color: #00d4ff; border-bottom: 2px solid #00d4ff; padding-bottom: 10px; }
        .card { background: #1a1d2e; border: 1px solid #2a2d3e; border-radius: 8px; padding: 20px; margin: 20px 0; }
        .badge { background: #00d4ff; color: #000; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
        .status { color: #00ff88; font-weight: bold; }
        table { width: 100%; border-collapse: collapse; }
        td { padding: 8px 0; border-bottom: 1px solid #2a2d3e; }
        td:first-child { color: #888; width: 180px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Plataforma DevOps AWS</h1>
        <div class="card">
            <span class="badge">LIVE</span>
            <p class="status">Aplicación funcionando correctamente</p>
            <table>
                <tr><td>Empresa</td><td>Soluciones Tecnologicas del Futuro</td></tr>
                <tr><td>Proyecto</td><td>Plataforma automatizada de despliegue</td></tr>
                <tr><td>Tecnologias</td><td>Flask · Docker · AWS EC2 · S3 · CloudWatch</td></tr>
                <tr><td>Fecha/Hora</td><td>{{ fecha }}</td></tr>
                <tr><td>Servidor</td><td>Amazon EC2 · us-east-1</td></tr>
                <tr><td>Contenedor</td><td>Docker</td></tr>
            </table>
        </div>
        <div class="card">
            <h3>Endpoints disponibles</h3>
            <table>
                <tr><td>GET /</td><td>Esta pagina principal</td></tr>
                <tr><td>GET /health</td><td>Estado de la aplicacion (JSON)</td></tr>
                <tr><td>GET /info</td><td>Informacion del servidor (JSON)</td></tr>
            </table>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML, fecha=fecha)

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "service": "devops-app"
    })

@app.route("/info")
def info():
    return jsonify({
        "empresa": "Soluciones Tecnologicas del Futuro",
        "proyecto": "Plataforma DevOps AWS",
        "version": "1.0.0",
        "tecnologias": ["Flask", "Docker", "AWS EC2", "S3", "CloudWatch"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)