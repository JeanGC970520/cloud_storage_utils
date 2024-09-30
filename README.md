# Utilidades para Cloud Storage

Pequeño programa para subir un archivo a Cloud Storage, identificar si existe y renombrarlo si es asi.

## Ejemplo

```python
from utils import push_to_cloud_storage

push_to_cloud_storage(
     bucket_name="proy-vsp-sandbox-sae-comercial-modelos-rl",
     file_path="C:\\Users\\jeanp\\OneDrive\\Imágenes\\Capturas de pantalla\\test_procesamiento_video_ava.png"
)
```