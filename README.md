# Laboratorio4

## Juan David Becerra - 201911588 - Pruebas Postman y analisis
## Nicolas Chalee Guerrero - 201912737 - pipeline
## Juan Andrés Santiago - 201821950 - API

## Instrucciones

1. Ejecutar el siguiente comando en la terminal para instalar todas las librerias necesarias: pip3 install -r requirements.txt
2. Ejecutar el programa colocando el siguiente comando en la terminal: uvicorn main:app --reload 
3. Abrir la aplicacion Postman e importar la coleccion encontrada en la carpeta de "postman".
4. Se encuentran dos request: Predict y Rsquared. En cada uno se coloca en la parte del body las entradas Json de los datos. 
5. Enviar el request correspondiente. En el resultado del request de predict deberia aparecer el valor que se predijo de life expectancy y en Rsquared deberia aparecer el valor exacto del R^2 encontrado.
