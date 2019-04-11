import pyodbc
from flask import Flask, render_template, request
app = Flask(__name__)



def conector(self):
    self.server = 'MAQUINA19-PC\SQLEXPRESS'
    self.database = 'student'
    self.cnxn = pyodbc.connect('DRIVER={{SQL Server}; Server='+server+';Database =' +self.database+';Trusted_Connection=yes;')  
    self.cursor = self.cnxn.cursor()
    self.cursor.execute(self.exeSQL) 
class Aluno():
    def __init__(self, nome, data, idade, genero, email, objetivo):
        self.nome = nome
        self.data = data
        self.idade = idade
        self.genero = genero
        self.email = email
        self.objetivo = objetivo
def InserirAluno(self):
    self.exeSQL = "INSERT INTO student (nome, data, idade, genero, email, objetivo) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.nome, self.data, self.idade, self.genero,self.email, self.objetivo)
    conexao(self)
    self.cursor.commit() 
    self.cursor.close()

@app.route('/')
def student ():
return render_template ('formulario.html')


@app.route ('/resultado',methods = ['POST', 'GET'])
def insert (POST):
   if request.method == 'POST':
      result = request.form
      nome = request.form ['NAME']
      data=request.form['DATA_DE_NASCIMENTO']
      idade = request.form['IDADE']
      objetivo =request.form['OBJETIVO']
      genero=request.form['GENERO']
      email = request.form ['EMAIL']
      aluno = Aluno( nome, data, idade, genero, email, objetivo)
      Aluno.InserirAluno
      

   
     row = cursor.fetchone()
     if row != None:
        return "Usuario existente na base"
     else:
         return "Usuario não existe"
     return render_template("resultado.html",result = result)


     

 if __name__ == '__main__':
     app.run (debug = True)
