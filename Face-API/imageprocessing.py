#crear el servicio de computer vision
az cognitiveservices account create \
--kind ComputerVision \
--name ComputerVisionService \
--sku S1 \
--resource-group xxxx \
--location [location]

#ver las keys
az cognitiveservices account keys list \
--name ComputerVisionService \
--resource-group xxxx

#almacernar la key1
key=$(az cognitiveservices account keys list \
--name ComputerVisionService \
--resource-group xxxx \
--query key1 -o tsv)

##IDENTIFICACION PUNTOS DE REFERENCIA EN IMAGEN
# uso de analyze

#CASO 1: foto montaña
#salida: JSON con categorias, description and details
curl "https://<region>.api.cognitive.microsoft.com/vision/v2.0/analyze?visualFeatures=Categories,Description&details=Landmarks" \
-H "Ocp-Apim-Subscription-Key: $key" \
-H "Content-Type: application/json" \
-d "{'url' : 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-process-images-with-the-computer-vision-service/master/images/mountains.jpg'}" \
| jq '.'

#CASO 2: contenido inapropiado. Familia posando
#salida: JSON con description + info si es contenido adecuado
```
"adult": {
    "isAdultContent": false,
    "isRacyContent": false,
    "adultScore": 0.0013711383799090981,
    "racyScore": 0.0046537225134670734
```
curl "https://<region>.api.cognitive.microsoft.com/vision/v2.0/analyze?visualFeatures=Adult,Description" \
-H "Ocp-Apim-Subscription-Key: $key" \
-H "Content-Type: application/json" \
-d "{'url' : 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-process-images-with-the-computer-vision-service/master/images/people.png'}" \
| jq '.'
    
    
#GENERACION DE MINIATURAS
curl "https://<region>.api.cognitive.microsoft.com/vision/v2.0/generateThumbnail?width=100&height=100&smartCropping=true" \
-H "Ocp-Apim-Subscription-Key: $key" \
-H "Content-Type: application/json" \
-d "{'url' : 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-process-images-with-the-computer-vision-service/master/images/dog.png'}" \
-o  thumbnail.jpg
    
#IDENTIFICACION DE TEXTO y EXTRACION DE TEXTO DE UNA IMAGEN
#hace uso de la "ocr" (reconocimiento optico de caracteres)
    
#salida: principales elementos de texto de la imagen
    
curl "https://<region>.api.cognitive.microsoft.com/vision/v2.0/ocr" \
-H "Ocp-Apim-Subscription-Key: $key" \
-H "Content-Type: application/json"  \
-d "{'url' : 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-process-images-with-the-computer-vision-service/master/images/ebook.png'}" \
 | jq '.'
    
    
# EXTRACION DE TEXTO MANUSCRITO
#usa recognizetext que detecta y extrae texto manuscrito de notas, cartas, ensayos, pizarras, formularios y otras fuentes. 
