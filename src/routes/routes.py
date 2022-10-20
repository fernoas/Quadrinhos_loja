from src.controllers.errors import NotFoundController
from src.controllers.controller import *



routes = {

    "index_route":"/","indexcontroller":IndexController.as_view("index"),
    "delete_route":"/delete/product/<int:code>", "delete_controller": DeleteProdutoController
.as_view("delete"),
    "update_route":"/update/product/<int:code>", "update_controller": UpdateProdutoController
.as_view("update"),
    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),


}


DeleteProdutoController