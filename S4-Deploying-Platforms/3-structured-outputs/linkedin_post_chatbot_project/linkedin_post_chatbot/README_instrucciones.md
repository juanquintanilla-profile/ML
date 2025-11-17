Instrucciones del proyecto
--------------------------

1. Crear archivo .env con:
   OPENAI_API_KEY=tu_clave_aqui

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar:
   python main.py

4. El sistema pedirá una descripción del post de LinkedIn y generará:
   - título
   - contenido
   - hashtags
   - categoría

5. La respuesta se valida estrictamente con Pydantic mediante Structured Outputs.
