# 📌 Backend - Blog con FastAPI

Este proyecto es el **backend** de una aplicación tipo blog construido con **FastAPI** y **SQLAlchemy**. Permite gestionar usuarios, posts y comentarios con autenticación basada en JWT.

---

## 🚀 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (opcional, pero recomendado)
- Una base de datos (por defecto **SQLite**, aunque puedes usar **PostgreSQL** o **MySQL** modificando la configuración en `app/core/database.py`)

---

## 📂 Instalación

1.  Clona el repositorio:

   ```bash
   git clone https://github.com/Zawent/FastApi-Prueba
   cd FastApi-Prueba
   ```

2.  Crea y activa un entorno virtual:

   ```
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```

3.  Instala las dependencias:

   ```
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuración

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

env
# Configuración de la base de datos
DATABASE_URL=sqlite:///./blog.db
SECRET_KEY=tu_clave_secreta_super_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

▶️ Ejecución
Para correr el servidor de desarrollo:
uvicorn app.main:app --reload

El backend estará disponible en:
👉 http://127.0.0.1:8000

📚 Documentación automática
FastAPI genera la documentación de la API automáticamente:
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc


🧪 Probar la API
Puedes probar los endpoints usando:
Swagger UI integrado en FastAPI


📝 Notas
Por defecto la base de datos es SQLite (blog.db en la raíz del proyecto).
Si cambias a PostgreSQL o MySQL, recuerda actualizar la variable DATABASE_URL en .env.
Ejecuta las migraciones con Alembic si agregas modelos nuevos.

📌 Autor
Desarrollado con ❤️ usando FastAPI y SQLAlchemy - Uriel Vargas
