import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

def obtenerContactos():
    #SELECT * FROM CONTACTOS;
    response = supabase.table("Contactos").select("*").execute()
    return response.data

print(obtenerContactos())