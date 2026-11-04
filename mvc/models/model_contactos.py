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
    response = self.supabase.table("contactos").select("*").eq("id_contacto",id_contacto).execute()
    return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())