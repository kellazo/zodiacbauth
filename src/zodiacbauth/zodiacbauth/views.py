# -*- coding: utf-8 -*-
import random
import datetime

from pyramid.view import view_config

#llibreria exception
from pyramid.httpexceptions import HTTPFound

### per afegir el login i logout views
from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid, ###aquest ultim es del egipcis
    )

from .security import USERS,comprova_usuari ##aquest comprova ususari es del egipcis

@view_config(route_name='home', renderer='templates/mytemplate.mako')
def my_view(request):
    #array dimatges
    imatges = ['1_aries.jpg','2_tauro.jpg','3_geminis.jpg','4_cancer.jpg','5_leo.jpg','6_virgo.jpg','7_libra.jpg','8_escorpi.jpg','9_sagitari.jpg','10_capricorn.jpg','11_aquari.jpg','12_piscis.jpg']
    #clau imatges valor variable imatges i va sense cometes pk no vui pasar un string sino  una variable al return
    return {'project': 'zodiacbauth', 'page':"home",'imatges':imatges, 'logged_in':authenticated_userid(request) }

# view afegir
@view_config(route_name='elmeu', renderer='templates/elmeu.mako',
             permission='edit')
def elmeu_view(request):
    
    if request.method=="POST":
        
        frases=["Demà tindràs un día agradable, no cometis cap error i seràs recompensat.","Demà pot ser que et toqui la loteria...pensa-hi.","Pot ser que en algun moment del dia, algú et saludi, torna-li el saludo efusivament i seràs recompensat.","Vigila amb els actes que comets, perjudicaran a terceres persones... ","Vés al metge, crec que ja es hora de que facis alguna revisió de tan en tan. ","Si menges fruits secs sovints, poc esforç mental hauràs de fer en els examens ",]
        num=random.randint(0,5)#num aleatori amb random per a que escolleixi frase
        imatges = ['10_capricorn.jpg','11_aquari.jpg','12_piscis.jpg','1_aries.jpg','2_tauro.jpg','3_geminis.jpg','4_cancer.jpg','5_leo.jpg','6_virgo.jpg','7_libra.jpg','8_escorpi.jpg','9_sagitari.jpg']
        dia=request.POST.get("dia")
        mes=request.POST.get('mes')
        nom=request.POST.get('nom')
        ano=request.POST.get('any')
        mesos = ['Gener','Febrer','Març','Abril','Maig','Juny','Juliol','Agost','Setembre','Octubre','Novembre','Desembre']
        frase=frases[num].decode('utf-8')# decode per a que accepti els accents
        lletres_mes=mesos[int(mes)]
        num_mes=int(mes)+1
        signes = ['Capricorn','Aquari','Peixos', 'Àries','Taure', 'Bessons', 'Càncer', 'Lleó', 'Verge', 'Balança', 'Escorpí', 'Sagitari']
        dies_finals_signes = [20,19,20,20,21,21,22,22,22,22,22,21]
        
        dia=int(dia)
        mes=int(mes)
       # extret de : http://geekytheory.com/calcula-tu-zodiaco-con-python/
        if dia > dies_finals_signes[int(mes)]:
            mes=mes+1
        if mes==12:
            mes=0
        
        imatge_signe=imatges[int(mes)].decode('utf-8')
        signe=signes[int(mes)].decode('utf-8')
        
       
        #if request.POST.get('opcio')== "si": 
        #creem instancia fortuna
         #   fortuna = Fortuna(signe=signe,frase=frase)
        #and then ho posem a la DB
          #  fortuna.put()

        return {"dia":dia,"mes":mes,"nom":nom,"ano":ano,"lletres_mes":lletres_mes,"frase":frase,"num_mes":num_mes,"signe":signe,"imatge_signe":imatge_signe,'project':'zodiac' }
            
    
    return {'project':'zodiacbauth','logged_in':authenticated_userid(request)}
#view veure
#@view_config(route_name='view_page', renderer='templates/view.pt',
#             permission='view')


### view de login i logout
# aquest decorator és per establir la ruta per /login
@view_config(route_name='login', renderer='templates/login.mako')
# aquest altre ens redirigirà aquí quan algú intenti entrar en una web que no té permís
@forbidden_view_config(renderer='templates/login.mako')
def login(request):
    login_url = request.route_url('login')
    # detectem des de quina URL ve el visitant
    referrer = request.url
    # retornem l'usuari a la home page si ha vingut directe al login
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    user = authenticated_userid(request)
    if user:
        lloc = came_from.split("/")
        message = "Ets %s, i com a tal no pots entrar a %s" % (user,lloc[len(lloc)-1])
    else:
        message = "Identifica't per descobrir el teu futur a través del teu zodiac"
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if USERS.get(login) == password:
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        user = authenticated_userid(request), # afegim usuari autenticat si l'hi ha
        )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('home'),
                     headers = headers)

#@view_config(route_name='guestbook', renderer='templates/guestbook.mako',
#             permission='edit')
#def guestbook_view(request):
#    fortuna = Fortuna.all() # equival a una query select * from fortuna
    
    
#    return {'project':'zodiac','fortuna':fortuna}  
