from flask.views import MethodView
from flask import request, render_template, redirect
from pymysql import MySQLError
from src.db import mysql



class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM produto")
            data = cur.fetchall
        return render_template('public/index.html', data=data)


    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        #category = request.form['category']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO produto(code,name,stock,value) VALUES(%s,%s,%s,%s)",(code,name,stock,value))
            cur.connection.commit()
            return redirect('/')



class DeleteProdutoController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM produto WHERE code = %s",(code))
            cur.connection.commit()
            return redirect('/')
        return "deletado com sucesso"


class UpdateProdutoController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            pass
        return "deletado com sucesso"

        