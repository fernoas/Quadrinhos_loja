from controllers.errors import NotFoundController
from src.controllers.controller import *
from src.controllers.errors import NotFoundController


routes = {

    "ola_route":"/","olacontroller":OlaController.as_view("ola"),
    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),


}