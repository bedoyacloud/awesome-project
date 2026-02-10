# Mentoria - Carlos

## Tareas para la próxima sesión

### 1. Mejorar el tipado actual
**Objetivo:** Entender qué está retornando cada función

* [ ] Investiga qué significa `dict[str, str]` en el tipo de retorno
* [ ] En `read_item`, ¿por qué usamos `int | str | None`? ¿Qué representa el `|`?

---

### 2. Configurar Git
**Objetivo:** Versionar tu código desde el inicio

* [ ] Inicializa un repositorio git en tu proyecto
* [ ] Crea un archivo `.gitignore` que ignore `__pycache__/` y `.venv/`, validar el git ignore de toptal.com
* [ ] Haz tu primer commit con el código actual revisando [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
* [ ] Crea un `README.md` explicando qué hace tu API
* [ ] Sube el proyecto a GitHub/GitLab

---

### 3. Crear almacenamiento en memoria 💾
**Objetivo:** Mantener datos mientras la app está corriendo

* [ ] Crea una lista global llamada `items_db` que almacene objetos tipo `Item`
* [ ] Agrega 3 items de ejemplo cuando la app inicie
* [ ] Modifica el endpoint GET `/items/{item_id}` para buscar en esta lista

**Pista:**

```python
# Almacenamiento en memoria
items_db: list[dict[str,str]] = []

# ¿Cómo buscas un item por su id en esta lista?
# Investiga: list comprehension, método filter(), o un loop simple
```

---

### 4. Implementar POST
**Objetivo:** Agregar nuevos items a la lista

* [ ] Crea un endpoint `POST /items` que reciba un `dict[str, str]` en el body
* [ ] El endpoint debe agregar el item a `items_db`
* [ ] Retorna el item creado con status code 201
* [ ] ¿Cómo evitas que se creen dos items con el mismo `id`?

**Pista:**
```python
from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED) # ¿Para qué sirve status_code acá?
def create_item(item: dict[str, str]) -> dict[str, str]:
    # ¿Cómo verificas si el id ya existe?
    # ¿Cómo agregas a la lista?
    pass # ¿Para qué es pass?
```

---

### 5. Implementar GET de todos los items
**Objetivo:** Listar todos los items almacenados

* [ ] Crea `GET /items` que retorne toda la lista
* [ ] El tipo de retorno debe ser `list[dict[str, str]]`
* [ ] Prueba con Swagger (http://localhost:8000/docs)

---

### 6. Implementar PUT
**Objetivo:** Reemplazar completamente un item existente

* [ ] Crea `PUT /items/{item_id}` que reciba un `dict[str, str]` completo
* [ ] Debe buscar el item por id y reemplazarlo
* [ ] Si no existe, retorna error 404
* [ ] Retorna el item actualizado

**Preguntas para reflexionar:**
* ¿Cuál es la diferencia entre POST y PUT?
* ¿Qué pasa si envías un PUT con un id diferente al de la URL?

**Pista:**
```python
from fastapi import HTTPException

# ¿Cómo encuentras el índice de un item en la lista?
# enumerate() puede ser tu amigo aquí
```

---

### 7. Implementar PATCH
**Objetivo:** Actualizar parcialmente un item

* [ ] Investiga: ¿Cuál es la diferencia entre PUT y PATCH?
* [ ] Crea `PATCH /items/{item_id}`
* [ ] Debe permitir actualizar solo algunos campos (ej: solo `quantity`)
* [ ] Los campos no enviados deben mantener su valor anterior

---

### 8. Implementar DELETE
**Objetivo:** Eliminar items de la lista

* [ ] Crea `DELETE /items/{item_id}`
* [ ] Debe eliminar el item de la lista
* [ ] Si no existe, retorna 404
* [ ] Retorna status 204 (No Content)

**Pista:**
```python
# ¿Cómo remueves un elemento de una lista en Python?
# Opciones: .remove(), .pop(), del, o crear una nueva lista sin ese elemento
```

---

### 9. Manejo de errores
**Objetivo:** Hacer la API más robusta

* [ ] En todos los endpoints que buscan por id, maneja el caso cuando no existe
* [ ] Retorna mensajes de error descriptivos
* [ ] Usa los status codes apropiados

**Pista:**
```python
raise HTTPException( # ¿Para qué es raise? ¿De donde importamos HTTPException?
    status_code=404,
    detail=f"Item with id {item_id} not found"
)
```

---

### 10. Testing manual
**Objetivo:** Verificar que todo funciona

* [ ] Usa Swagger UI o Postman para probar cada endpoint
* [ ] Crea un flujo completo: POST → GET → PUT → PATCH → DELETE
* [ ] Documenta en tu README cómo usar cada endpoint

---

## Bonus (si te sobra tiempo)

* [ ] Agrega validaciones: `quantity` debe ser mayor a 0
* [ ] Crea un endpoint `GET /items?name=xxx` para filtrar por nombre
* [ ] Agrega un campo `created_at` automático a cada item, es decir, no lo recibes en el body

---

**Recuerda:** No copies y pegues código. Si encuentras algo en internet que no entiendes, pregúntame en la próxima sesión o si es rápida la pregunta, por WP. El objetivo es que comprendas cada línea que escribes.

**Recursos recomendados:**
* Documentación oficial de FastAPI: https://fastapi.tiangolo.com
* Tipado en Python: https://docs.python.org/3/library/typing.html