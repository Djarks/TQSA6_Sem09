class Turma:
  def __init__(self):
    self.turma = [];
    self.menorNota = None;
    self.maiorNota = None;

  def cadastrarAlunos(self, alunos):    
    for i in alunos:
      self.turma.append(i);
      if((self.menorNota == None) or (self.menorNota.nota > i.nota)):
        self.menorNota = i;
      elif((self.maiorNota == None) or (self.maiorNota.nota < i.nota)):
        self.maiorNota = i;

  def vrfIntervalo(self, alunos):
    for i in alunos:
      if ((i.nota < 0) or (i.nota > 10)):
        print('Nota de ' + i.nome + ' ' + i.sobrenome + ' incorreta. Favor cadastrar notas no intervalo entre 0 e 10, inclusive!');
      #else:
      #  print('Todos os alunos com notas cadastradas dentro do intervalo esperado!');

  def mostrarAlunos(self):  
    print('Quantidade de alunos:', len(self.turma));
    for x in self.turma:      
      print(x.mostrarAluno());
