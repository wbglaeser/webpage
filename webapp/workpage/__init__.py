##############################
### IMPORTS                ###
##############################
 
# EXTERNAL
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

# WITHIN PROJECT
from .models import DBSession, Base
from .security import groupfinder

##############################
### CODE                   ###
##############################

def main(global_config, **settings):

    # DATABASE CONFIGURATION
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    # GENERAL CONFIGURATIONS
    config = Configurator(settings=settings, root_factory='workpage.models.Root')
    config.include('pyramid_chameleon')

    # SECURITY CONFIGURATIONS
    authn_policy = AuthTktAuthenticationPolicy(
        settings['workpage.secret'], callback=groupfinder,
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    # VIEW CONFIGURATIONS
    config.add_route('start', '/')
    config.add_route('home', '/home')
    config.add_route('coming_shortly', '/coming_shortly')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('data_entry', '/data_entry')
    config.add_route('data_update', '/data_update')
    config.add_route('data', 'data.json')
    config.add_route('data_3', 'data_3.json')
    config.add_static_view(name='static', path='workpage:static')
    config.scan('.views')
    return config.make_wsgi_app()