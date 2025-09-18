#Proyecto de Automatización con Selenium y Python

Este es un proyecto de automatización de pruebas para la web, construido con Python, Selenium y Pytest, utilizando una arquitectura BDD con el Patrón de Diseño Page Object Model (POM).

Guía de Instalación del Ambiente (macOS) ⚙️
Sigue estos pasos para configurar tu entorno de desarrollo local y ejecutar las pruebas.

1. Prerrequisitos
Asegúrate de tener instalado lo siguiente en tu sistema:

Homebrew (gestor de paquetes para macOS). Si no lo tienes, instálalo desde brew.sh.
Python 3.9+. Puedes verificar tu versión con python3 --version. Si necesitas instalarlo, usa brew install python3.
Visual Studio Code. Descárgalo desde la página oficial.

2. Clonar el Repositorio
Abre tu terminal y clona este repositorio en tu máquina local.

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA_DEL_PROYECTO>

3. Configurar el Entorno Virtual
Es una buena práctica aislar las dependencias del proyecto en un entorno virtual.

Crear el entorno virtual llamado 'venv'
python3 -m venv venv

Activar el entorno virtual
source venv/bin/activate
Nota: Verás (venv) al principio de la línea de tu terminal, lo que indica que el entorno está activo.

4. Instalar Dependencias
Instala todas las librerías necesarias que están definidas en el archivo requirements.txt.

'''pip install -r requirements.txt

5. Instalar Extensión en VS Code (Opcional pero recomendado)
Para una mejor experiencia de desarrollo, instala las siguientes extensiones desde el Marketplace de VS Code:

Python (de Microsoft)

Cucumber (Gherkin) Full Support (para resaltar la sintaxis de los archivos .feature)

Cómo Ejecutar las Pruebas ▶️
Con el entorno virtual activado, ejecuta el siguiente comando desde la raíz del proyecto para correr todas las pruebas y generar un reporte HTML.

Bash

pytest --html=reports/report.html
