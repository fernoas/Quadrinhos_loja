from flask.views import MethodView


class NotFoundController(MethodView):
    
    def get(self):
        return f"Pagina não encontrada"

        