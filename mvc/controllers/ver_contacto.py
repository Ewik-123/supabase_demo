import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base ='template')

class VerContacto:
    def GET(self, id_contacto):

        model_contactos=ModelContactos()

        resultado = model_contactos.buscarContacto(id_contacto)
    
        contacto = resultado[0] if resultado and len(resultado) > 0 else []
        print(contacto)
        return render.ver_contacto(contacto) #type: ignore
    