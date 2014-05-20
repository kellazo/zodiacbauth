# -*- coding: utf-8 -*-
from pyramid.config import Configurator
#importem llibreries auth i autoritzacio
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import groupfinder

### proves 
from .models import RootFactory
import os
here = os.path.dirname(os.path.abspath(__file__))
### proves


# Adaptat de:
# http://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/authorization.html
# i del github de egipcis

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
   
    
    ### # afegit del auth module
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    ### configurem 
    #config = Configurator(settings=settings)
    config = Configurator(settings=settings,root_factory='zodiacbauth.models.RootFactory')
    
    ### les posem a la funcions
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    
    config.include('pyramid_mako')
    #config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    ### crear views a rutes login i logout
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    
    ### ames a mes
    #el meu zodiac #formulari del zodiac
    # afegim la URL "/elmeu" a la que accedim amb "http://localhost:8080/elmeu"
    config.add_route( "elmeu", "/elmeu" ) # elmeu=view, /elmeu=URL
    
    #config.add_route( "guestbook", "/guestbook" ) # guestbook=view, /guestbook=URL
    
    
    config.scan()
    return config.make_wsgi_app()
