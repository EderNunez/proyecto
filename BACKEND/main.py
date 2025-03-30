from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import mysql.connector
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="worshby-db"
)


class UsuarioRegistro(BaseModel):
    Usuario: str
    Correo: str
    Contraseña: str
    ConfirmarContraseña: str


class VideoCreate(BaseModel):
    Título: str
    Enlace: str
    Fecha_Publicacion: datetime
    x_user_id: int


class DonacionCreate(BaseModel):
    Nombre: str
    Apellido: str
    Tipo_Donacion: str
    Correo: str
    Teléfono: str
    Monto: float
    TipoDocumento: str
    Documento: str
    MetodoPago: str
    Fecha: datetime
    x_user_id: int


class PeticionCreate(BaseModel):
    Texto_Peticion: str
    x_user_id: int


class UsuarioLogin(BaseModel):
    Usuario: str
    Contraseña: str


class Miembro(BaseModel):
    Nombre: str
    Apellido: str
    Telefono: str
    Barrio: str
    Direccion: str
    Cargo: str
    Bautizado: bool
    Fecha: datetime
    Culto: str


class Iglesia(BaseModel):
    id: int
    Nombre: str
    Direccion: str
    Telefono: str


class Usuario(BaseModel):
    Usuario: str
    Correo: str
    Contraseña: str
    Rol: str


# ------------------- Funciones de ayuda -------------------


@app.options("/{full_path:path}")
async def preflight_handler(full_path: str, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


@app.post("/auth/login")
def login(usuario: UsuarioLogin):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT * FROM Usuarios WHERE Usuario = %s AND Contraseña = %s",
                (usuario.Usuario, usuario.Contraseña),
            )
            result = cursor.fetchone()

            if not result:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Credenciales inválidas",
                )

            return {"mensaje": "Login exitoso", "usuario": result}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.post("/auth/registro")
def registro_usuario(usuario: UsuarioRegistro):
    try:
        if usuario.Contraseña != usuario.ConfirmarContraseña:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Las contraseñas no coinciden",
            )

        with mydb.cursor() as cursor:
            sql = """
                INSERT INTO Usuarios 
                (Usuario, Correo, Contraseña, Rol)
                VALUES (%s, %s, %s, 'Usuario')
            """
            val = (usuario.Usuario, usuario.Correo, usuario.Contraseña)
            cursor.execute(sql, val)
            mydb.commit()
            return {"mensaje": "Usuario registrado exitosamente"}
    except mysql.connector.IntegrityError:
        raise HTTPException(status_code=400, detail="Usuario o correo ya existen")
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/videos")
def obtener_videos():
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Videos")
            return {"resultado": jsonable_encoder(cursor.fetchall())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/videos/{id}")
def obtener_video(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Videos Where ID_Video = %s", (id,))
            return {"resultado": jsonable_encoder(cursor.fetchone())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.post("/videos")
def crear_video(video: VideoCreate):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            sql = """
                INSERT INTO Videos 
                (Título, Enlace, Fecha_Publicacion, ID_Usuario)
                VALUES (%s, %s, %s, %s)
            """
            val = (video.Título, video.Enlace, video.Fecha_Publicacion, video.x_user_id)
            cursor.execute(sql, val)
            mydb.commit()
            return {"mensaje": "Video creado exitosamente"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.put("/videos/{id}")
def cambiar_video(videoCreate: VideoCreate, id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute(
                "UPDATE Videos SET Título = %s, Enlace = %s, Fecha_Publicacion = %s WHERE ID_Video = %s",
                (
                    videoCreate.Título,
                    videoCreate.Enlace,
                    videoCreate.Fecha_Publicacion,
                    id,
                ),
            )
            mydb.commit()
            return {"resultado": "Video actualizado exitosamente"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.delete("/videos/{id}")
def borrar_video(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM Videos WHERE ID_Video = %s", (id,))
            mydb.commit()
            return {"mensaje": "Se a borrado el video con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/donaciones")
def obtener_donaciones():
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Donaciones")
            return {"resultado": jsonable_encoder(cursor.fetchall())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/donaciones/{id}")
def obtener_donacion(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Donaciones WHERE ID_Donacion = %s", (id,))
            return {"resultado": jsonable_encoder(cursor.fetchone())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.post("/donaciones")
def crear_donacion(donacion: DonacionCreate):
    try:
        with mydb.cursor(dictionary=True) as cursor:

            sql = """
                INSERT INTO Donaciones 
                (ID_Usuario, Nombre, Apellido, Tipo_Donacion, Correo, Teléfono,
                 Monto, TipoDocumento, Documento, MetodoPago, Fecha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            val = (
                donacion.x_user_id,
                donacion.Nombre,
                donacion.Apellido,
                donacion.Tipo_Donacion,
                donacion.Correo,
                donacion.Teléfono,
                donacion.Monto,
                donacion.TipoDocumento,
                donacion.Documento,
                donacion.MetodoPago,
                donacion.Fecha,
            )
            cursor.execute(sql, val)
            mydb.commit()
        return {"mensaje": "Donación registrada exitosamente"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.put("/donaciones/{id}")
def cambiar_donacion(donacionCreate: DonacionCreate, id: int):
    try:
        with mydb.cursor() as cursor:
            cursor.execute(
                "UPDATE donaciones SET Nombre = %s, Apellido = %s, Tipo_Donacion = %s, Correo = %s, Teléfono = %s, Monto = %s, TipoDocumento = %s, Documento = %s, MetodoPago = %s, Fecha = %s WHERE ID_Donacion = %s",
                (
                    donacionCreate.Nombre,
                    donacionCreate.Apellido,
                    donacionCreate.Tipo_Donacion,
                    donacionCreate.Correo,
                    donacionCreate.Teléfono,
                    donacionCreate.Monto,
                    donacionCreate.TipoDocumento,
                    donacionCreate.Documento,
                    donacionCreate.MetodoPago,
                    donacionCreate.Fecha,
                    id,
                ),
            )
            mydb.commit()
            return {"mensaje": "Se a cambiado la donacion con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.delete("/donaciones/{id}")
def borrar_donaciones(id: int):
    try:
        with mydb.cursor() as cursor:
            cursor.execute(
                "DELETE FROM donaciones WHERE ID_Donacion = %s",
                (id,),
            )
            mydb.commit()
            return {"mensaje": "Se a borrado la donacion con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/peticiones")
def obtener_peticiones():
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Peticiones")
            return {"resultado": jsonable_encoder(cursor.fetchall())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/peticiones/{id}")
def obtener_peticion(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM Peticiones WHERE ID_Peticion = %s", (id,))
            return {"resultado": jsonable_encoder(cursor.fetchone())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.post("/peticiones")
def crear_peticion(peticion: PeticionCreate):
    try:
        with mydb.cursor() as cursor:
            sql = "INSERT INTO Peticiones (Texto_Peticion, ID_Usuario) VALUES (%s, %s)"
            cursor.execute(sql, (peticion.Texto_Peticion, peticion.x_user_id))
            mydb.commit()
            return {"mensaje": "Petición enviada exitosamente"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.put("/peticiones/{id}")
def cambiar_peticion(peticionCreate: PeticionCreate, id: int):
    try:
        with mydb.cursor() as cursor:
            cursor.execute(
                "UPDATE peticiones SET Texto_Peticion = %s, Fecha = %s WHERE ID_Peticion = %s",
                (
                    peticionCreate.Texto_Peticion,
                    datetime.now(),
                    id,
                ),
            )
            mydb.commit()
            return {"mensaje": "Se a cambiado la peticion con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.delete("/peticiones/{id}")
def borrar_peticion(id: int):
    try:
        with mydb.cursor() as cursor:
            cursor.execute(
                "DELETE FROM peticiones WHERE ID_Peticion = %s",
                (id,),
            )
            mydb.commit()
            return {"mensaje": "Se a borrado la peticion con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/miembros")
def obtener_miembros():
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT * FROM miembros",
            )
            return {"data": jsonable_encoder(cursor.fetchall())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/miembros/{id}")
def obtener_miembro(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM miembros WHERE ID_Miembro = %s", (id,))
            return {"resultado": jsonable_encoder(cursor.fetchone())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.post("/miembros")
def agregar_miembro(miembro: Miembro):
    try:
        with mydb.cursor() as cursor:
            sql = """
                INSERT INTO miembros 
                (Nombre, Apellido, Teléfono, Barrio, Dirección, Cargo, Bautizado, Fecha, Culto)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(
                sql,
                (
                    miembro.Nombre,
                    miembro.Apellido,
                    miembro.Telefono,
                    miembro.Barrio,
                    miembro.Direccion,
                    miembro.Cargo,
                    miembro.Bautizado,
                    miembro.Fecha,
                    miembro.Culto,
                ),
            )
            mydb.commit()
            return {"mensaje": "Miembro agregado exitosamente"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.put("/miembros/{id}")
def cambiar_miembros(miembro: Miembro, id: int):
    try:
        with mydb.cursor() as cursor:
            cursor.execute(
                "UPDATE miembros SET Nombre = %s, Apellido = %s, Teléfono = %s, Barrio = %s, Dirección = %s, Cargo = %s, Bautizado = %s, Fecha = %s, Culto = %s Where ID_Miembro = %s",
                (
                    miembro.Nombre,
                    miembro.Apellido,
                    miembro.Telefono,
                    miembro.Barrio,
                    miembro.Direccion,
                    miembro.Cargo,
                    miembro.Bautizado,
                    miembro.Fecha,
                    miembro.Culto,
                    id,
                ),
            )
            mydb.commit()
            return {"mensaje": "Se a cambiado el miembro con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.delete("/miembros/{id}")
def borrar_miembro(id: int):
    try:
        with mydb.cursor() as cursor:
            cursor.execute(
                "DELETE FROM miembros WHERE ID_Miembro = %s",
                (id,),
            )
            mydb.commit()
            return {"mensaje": "Se a borrado el miembro con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/usuarios")
def obtener_usuarios():
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM usuarios")
            return {"resultado": jsonable_encoder(cursor.fetchall())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE ID_Usuario = %s", (id,))
            return {"resultado": jsonable_encoder(cursor.fetchone())}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.post("/usuarios")
def agregar_usuario(usuario: Usuario):
    try:
        with mydb.cursor() as cursor:
            sql = """
                INSERT INTO usuarios 
                (Usuario, Correo, Contraseña, Rol)
                VALUES (%s, %s, %s, %s)
                """
            cursor.execute(
                sql,
                (usuario.Usuario, usuario.Correo, usuario.Contraseña, usuario.Rol),
            )
            mydb.commit()
            return {"mensaje": "Usuario agregado exitosamente"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.put("/usuarios/{id}")
def cambiar_usuario(usuario: Usuario, id: int):
    try:
        with mydb.cursor() as cursor:
            sql = "UPDATE usuarios SET Usuario = %s, Correo = %s, Contraseña = %s, Rol = %s WHERE ID_Usuario = %s"
            cursor.execute(
                sql,
                (
                    usuario.Usuario,
                    usuario.Correo,
                    usuario.Contraseña,
                    usuario.Rol,
                    id,
                ),
            )
            mydb.commit()
            return {"mensaje": "Se a cambiado el usuario con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@app.delete("/usuarios/{id}")
def borrar_usuario(id: int):
    try:
        with mydb.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM usuarios WHERE ID_Usuario = %s", (id,))
            mydb.commit()
            return {"mensaje": "Se a borrado el usuario con exito"}
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))
