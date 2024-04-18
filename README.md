# apigateway_be_MisionTIC2022
Microservico ApiGateway (Backend) para el proyecto de ejemplo GESTIÓN ACADÉMICA.
> Usado en los programas Misión TIC 2022 y Programación Avanzada-Uniremington 2024.

[Aquí](resources/Modelo.md) puede encontrar el __modelo general del sistema__.
## API GATEWAY
Por definición un api Gateway es _“es el gestor de tráfico que interactúa con los datos o el servicio backend real y aplica políticas, autenticación y control de acceso general para las llamadas de una API para proteger datos valiosos.”_. Este concepto posee una gran variedad de ventajas asociadas con temas tales como la escalabilidad de las aplicaciones, análisis,  supervisión y monitoreo de los servicios que ofrecen la plataforma, además la integración y llamados a múltiples microservicios ante una misma solicitud por parte del cliente.

#### Referencias
- [Tibco](https://www.tibco.com/glossary/what-is-an-api-gateway)
- [Nginx](https://www.nginx.com/learn/api-gateway/)
- [Red Hat](https://www.redhat.com/es/topics/api/what-does-an-api-gateway-do)
---
---
## Tecnologías
- Python
- [Flask Framework](https://flask.palletsprojects.com)


### Uso
1. Clone el repositorio e ingrese en el directorio del proyecto
```
git clone https://github.com/wilmar-arcila/apigateway_be_MisionTIC2022.git
cd apigateway_be_MisionTIC2022
```
2. Cree el [entorno virtual de python](https://docs.python.org/es/3/library/venv.html)
```
python -m venv .venv
```
__Nota__: Este paso solo es necesario la _primera vez que se quiera ejecutar el proyecto_. Una vez creado el entorno virtual este permanecerá hasta que explicitamente se elimine.
3. Active el entorno virtual

Linux
```
source .venv/bin/activate
```
Windows
```
# In cmd.exe
.venv\Scripts\activate.bat
# In PowerShell
.venv\Scripts\Activate.ps1
```
4. Instale las dependencias del proyecto
```
pip install -r requirements.txt
```
5. Configure las URL para los microservicios en el archivo [config.json](config.json)
6. Ejecute el servidor
```
python main.py
```
__Nota__: Cuando haya terminado de trabajar con el servidor, recuerde desactivar el entorno virtual
```
deactivate
```
---
## ToDo
- [ ] Exponer la arquitectura de referencia
- [ ] Documentar la API