import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base ='template')

class ActualizarContacto:
    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        resultado = model_contactos.buscarContacto(id_contacto)
        contacto = resultado[0] if resultado and len(resultado) > 0 else []
        return render.actualizar_contacto(contacto)

    def POST(self, id_contacto):
        formulario = web.input()
        nombre = formulario["nombre"]
        email = formulario["email"]
        telefono = formulario["telefono"]

        model_contactos = ModelContactos()
        model_contactos.actualizarContacto(id_contacto, nombre, email, telefono)

        raise web.seeother('/contactos')