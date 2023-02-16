# Projeto-CONTRATADO-ResiliaSenac-

* O projeto consiste em cadastrar candidatos para difentes vagas e através de palavras chaves realizar uma busca no resumo pessoal do candidato. Caso essas palavras estejam dentro deste resumo pessoal, o candidato estará apto para próxima fase do processo seletivo.

## Tecnologias usadas:
#### Python 3.11 🐍


# Falando do código

+ De início temos um dicionário apenas para apoio do programador. logo após criamos um def para cadastrar e posteriormente buscar os candidatos apts para próxima atapa do processo seletivo.

* Uma estrutura de repetição foi criada para realizar o cadastro dos candidatos onde colocamos todos num dicionário e logo após realizamos uma nossa busca usando as palavras chaves como parâmetro para pegarmos apenas os candidatos aptos e os colocamos em um dicionário a parte.

* Toda esse processo leva em conta para qual vaga o candidato esta se inscrevendo. caso seja vaga1, irá ára os dicionários da respectiva vaga e assim funciona também o processo para vaga 2.

* Ao final temos duas mensagens mostrando ao usuário quantos candidatos tivemos ao todo para cada vaga e quantos estão aptos para prosseguir no processo seletivo.

* Importamos a biblioteca pandas para melhorar a visualização dos candidatos aprovados, caso tenha. condicionais são criadas para evitar bugs no código para caso não haja nenhum candidato apto para prosseguir no processo seletivo.

* Por fim os frames são exibidos de forma clara e objetiva para melhor entendimento do usuário.
