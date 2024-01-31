from tkinter import *
from classes import*
from tet import*

#Iniciando o sistema
sistema = Sistema()

#criando uma categoria
cat = sistema.adicionar_categoria('GEOMETRIA')
id_categoria = cat.id

#criando as primeiras aulas
aula = sistema.adicionar_aula_ao_curso('https://www.youtube.com/watch?v=5e8Ua4RhhXg', 'Poligonos', id_categoria)
id_aula = aula.id

#adicionando as aulas na categoria criada
sistema.adicionar_aula_categoria(id_categoria, id_aula)

#Repetindo o processo para cadastrar outras aulas.
aula = sistema.adicionar_aula_ao_curso( 'https://www.youtube.com/watch?v=o-srrvPTo0Y', 'Angulos e Retas', id_categoria)
id_aula = aula.id
sistema.adicionar_aula_categoria(id_categoria, id_aula)


#criando um plano
plano = sistema.adicionar_plano('Adquira uma compreensão abrangente da geometria, desde seus princípios fundamentais até suas aplicações práticas e dimensões avançadas', 50, 'Desafios Geometricos')
id_plano = plano.id
#adicionando uma categoria a um plano
sistema.adicionar_categoria_plano(id_categoria, id_plano)

#criando outra categoria
cat = sistema.adicionar_categoria('EQUACOES')
id_categoria = cat.id

aula = sistema.adicionar_aula_ao_curso('https://www.youtube.com/watch?v=1VjauwyHV0o', 'Equação do Segundo Grau', id_categoria)
id_aula = aula.id
sistema.adicionar_aula_categoria(id_categoria, id_aula)


aula = sistema.adicionar_aula_ao_curso('https://www.youtube.com/watch?v=YTJPkVMdKho', 'Sistema de Equacoes', id_categoria)
id_aula = aula.id
sistema.adicionar_aula_categoria(id_categoria, id_aula)

#Criando o segundo plano
plano = sistema.adicionar_plano('Desbrave o universo dos sistemas de equações por meio de uma abordagem educacional meticulosa, explorando desde os fundamentos até aplicações práticas', 50, 'Desafios de Equacoes')
id_plano = plano.id
sistema.adicionar_categoria_plano(id_categoria, id_plano)


sistema.iniciar_interface()