# Crea y activa el entorno
python -m venv venv
# Linux/Mac
source venv/bin/activate  
# Windows
venv\Scripts\activate     

# Instala Django dentro del entorno
pip install django

1. Se realiza la configuración inicial del proyecto:
3. Revisar la versión de django - py -m django --version

# Crea el proyecto con:
py -m django startproject 'Nombre del Proyecto'

# Para los estilos de App - (Opcional)
1. Se debe de crear dentro del la raíz del proyecto la carpeta (static)
2. Dentro de esta carpeta se aloja el archivo styles.css

# Para que Django tome los estilos
1. ir a la carpeta de settings y revisar que exista lo siguiente:
   
   ![image](https://github.com/user-attachments/assets/10050886-a984-4737-ad96-2e0c6a2cf796)

2. Para los archivos HTML se debe de realizar el siguiente proceso:
   
  ![image](https://github.com/user-attachments/assets/17a09942-e14b-44bf-bb8b-6d826f59776d)

3. Tener esta linea al comienzo de la etiqueta HTML!

# HTML: {% load static %} 
## RUTA CSS: link rel="stylesheet" href="{% static 'app/styles.css' %}"

# Muestra de la App Inicialmente

![image](https://github.com/user-attachments/assets/20da0399-fe7b-4a69-811a-065ec4e337a6)

# Muestra de la App con Estilos

![image](https://github.com/user-attachments/assets/0188d2f1-daa7-44ca-bf01-d97a608c6f91)

