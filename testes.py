import unittest;
import aluno as a;
import turma as t;

class turmaTest(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.alunos = [];
    
    self.alunos.append(a.Aluno('Fabio', 'Teixeira', 8));
    self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 11));
    self.alunos.append(a.Aluno('Melissa', 'Teixeira', -1));
    self.alunos.append(a.Aluno('Marcus', 'Soares', 5));
    
    self.turmaObject = t.Turma();
    self.turmaObject.cadastrarAlunos(self.alunos);
  
  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 
  
  def testMaior(self):      
    self.assertEqual(11, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota');

  def testMenor(self):    
    self.assertEqual(-1, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota');

  def testIntervalo(self):
    print('Testar se o intervalo de notas está correto.')
    if((self.turmaObject.menorNota.nota < 0) or (self.turmaObject.maiorNota.nota > 10)):
      print('Intervalo de notas incorreto! Favor cadastrar notas entre 0 e 10, inclusive!');
    else:
      print('Intervalo de notas correto!');

if __name__ == "__main__":
  unittest.main()
