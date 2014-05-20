# -*- coding: utf-8 -*-

USERS = {'editor':'editor',
          'viewer':'viewer',
          'lacet':'lacet123',
          'guillem':'guille123'}
GROUPS = {'lacet':['group:editors']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
        

# Aquesta funció comprova el nostre usuari/contrasenya
# si cal fer-ho a una base de dades ho encapsularem en aquesta funció
def comprova_usuari(userid, passw):
    # de moment ho resolem amb un diccionari amb el id/pass dels usuaris
    if USERS.get(userid)==passw:
        return True
    return False
