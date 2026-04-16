import boto3
import uuid
from datetime import datetime

REGION = "us-east-1"
TABLE_NAME = "devops-registros"

def insertar_registro(evento, detalle):
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    tabla = dynamodb.Table(TABLE_NAME)

    item = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "evento": evento,
        "detalle": detalle,
        "servidor": "EC2-devops-server",
        "estado": "OK"
    }

    tabla.put_item(Item=item)
    print(f"[OK] Registro insertado: {evento} - {item['timestamp']}")

def listar_registros():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    tabla = dynamodb.Table(TABLE_NAME)

    print("\n==========================================")
    print("  Registros en DynamoDB")
    print("==========================================")

    respuesta = tabla.scan()
    items = respuesta.get("Items", [])

    if items:
        for item in items:
            print(f"  [{item['timestamp']}] {item['evento']} — {item['detalle']}")
    else:
        print("  No hay registros aún.")
    print("")

if __name__ == "__main__":
    print("==========================================")
    print("  DynamoDB Manager - DevOps Project")
    print("==========================================\n")

    insertar_registro("despliegue", "Aplicacion Flask levantada con Docker")
    insertar_registro("backup", "Script de respaldo ejecutado correctamente")
    insertar_registro("monitoreo", "CloudWatch configurado y activo")
    insertar_registro("s3", "Archivos subidos al bucket S3")

    listar_registros()

    print("==========================================")
    print("  Finalizado correctamente")
    print("==========================================")