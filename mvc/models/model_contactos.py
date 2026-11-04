import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL",""),
                os.environ.get("SUPABASE_KEY","")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        # SELECT * FROM contactos;
        response = self.supabase.table("Contactos").select("*").execute()
        return response.data

    def buscarContacto(self,id_contacto:int):
        response = self.supabase.table("Contactos").select("*").eq("id_contacto",id_contacto).execute()
        return response.data

    def insertarContacto(self,nombre,email,telefono):
        response = self.supabase.table("Contactos").insert({
            "nombre":nombre,
            "email":email,
            "telefono": telefono
        }).execute()
        return response.data

    def borrarContacto(self,id_contacto:int):
        response = self.supabase.table("Contactos").delete().eq("id_contacto", id_contacto).execute()
        return response.data

    def actualizarContacto(self,id_contacto,nombre,email,telefono):
        response = self.supabase.table("Contactos").update({
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }).eq("id_contacto", id_contacto).execute()
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(15))
    print(model_contactos.insertarContacto("Araceli", "ara@email.com", "67676767"))
    print(model_contactos.borrarContacto(11))
    print(model_contactos.actualizarContacto("1","Wicho","wicho@email.com", "90676767"))