from flask.views import MethodView
from flask import request, render_template, redirect



class OlaController(MethodView):
    def get(self):
        return "Até aqui deu certo"