<h1 align="center">House Sales</h1>

<h1 align="center">
  <img src="img/House_Sales.png " />
</h1>

<p align="center">Neste projeto foi criada uma problemática hipotética sobre a Previsão de Compras de Imóveis na região de King County, USA. </p>

<h1 align="center">Questão e Entendimento de Negócio</h1>

1.	Contexto da Problemática:

Realizou-se uma reunião mensal para discutir os fatores que impactam na compra e venda de imóveis nas proximidades de regiões lacustres, e após este primeiro momento, o CFO fez uma requisição de Relatório contendo informações sobre os imóveis de King County. A necessidade surgiu devido a intenção de entender qual o melhor período para vender ou comprar imóveis e quais características destes contribuem para isso. A segunda pauta da reunião foi a dificuldade de se analisar os dados obtidos de forma rápida e seletiva. Além disso, toda a visualização de informações sobre os imóveis só pode ser realizada pela rede local da empresa.

2.	Questionamento

- Como agilizar a tomada de decisões sobre compra e venda de imóveis?
- Como disponilibizar o acesso às informações de forma integrada e remota?


3.	Soluções

- Criação de visualização gráficos, tabelas e regiões dos imóveis demonstrados em mapa para consultoria online auxiliados por filtros interativos;
- Criação de Dashboard Online atualizado de forma remota e com acesso por meio da Internet;

<h1 align="center">Desenvolvimento do Projeto</h1>

O Dataset apresenta a Tabela "KC House Data", que contém informações sobre os imóveis: cômodos e suas respectivas quantidades, região por latitude e longitude, preço do imóvel, data de cadastro, período de construção e reforma, etc.

<p></p>

1.	Descrição dos Dados


Uma das primeiras partes do projeto é realizada no estudo do tipo de dados que temos disponíveis para o desenvolvimento do projeto. Nessa etapa são obtidos conhecimentos sobre o dataset: qual a quantidade de observações e atributos apresentados, quais os tipos de atributos, etc.


2.	Feature Engineering

Na etapa de Feature Engineering foram utilizadas transformações matemáticas das features para que fossem utilizadas ao máximo a maior quantidade de dados possíveis do dataset.

<h1 align="center">Questionário CFO</h1>

O Mapa Mental pode ser utilizado como um “guia” para observar quais são as variáveis mais importantes para a Análise Exploratória dos Dados e quais serão mais relevantes para a criação das hipóteses sobre o desenvolvimento e insights que serão apresentados. Dado que o projeto tem a finalidade de predição de clientes pagantes ou devedores, devemos selecionar as variáveis que serão agentes para tal objetivo e quais atributos destes são mais importantes para a validação das hipóteses.

<h1 align="center">
  <img src="img/Credit_Risk_Dataset.png" />
</h1>
<h1 align="center">Análise Exploratória de Dados</h1>

Após a filtragem de hipóteses serão realizadas as análises sobre as features e como estas agem sozinhas ou em combinação com outras features. O projeto teve oito hipóteses finais que foram validadas ou refutadas pelo estudo gráfico de cada uma delas (informações apresentadas no notebook Jupyter). 

<h1 align="center">Melhores Insights - Hipóteses</h1>

**H1.** Clientes com idades menores tendem a fazer mais empréstimos

Verdadeiro.

<p align="center">
  <img src="./img/h1.png">
</p>


**H4.** Clientes que tem como finalidade para o empréstimo reformas residenciais são maioria

Falso: Empréstimos para a Educação são maioria

<p align="center">
  <img src="./img/h4.png">
</p>


**H7.** Clientes com renda superior a 20000 tendem a pagar mais os empréstimos

Verdadeiro.

<p align="center">
  <img src="./img/h7.png">
</p>


<h1 align="center">Machine Learning Modelling</h1>

Para a escolha da técnica de Machine Learning que seria utilizada para o desenvolvimento dos modelos foram testados e coletados resultados de acurácia das seguintes técnicas:

o	Naive Bayes;

o	Decision Tree;

o	Random Forest;

o	KNN;

o	Regression Logistic;

o	SVM.

Os resultados das acurácias de cada técnica foram concentrados de forma tabulada e comparados.

<h1 align="center">
  <img src="img/modelos_acc.png" />
</h1>

<h1 align="center">Obtenção dos resultados de forma remota</h1>


A última parte do projeto foi o desenvolvimento de API e utilização de Heroku para disponibilizar dados em Cloud. 


<h1 align="center">Referências</h1>
https://www.kaggle.com/laotse/credit-risk-dataset    - Acesso em: 02/11/2021


https://www.bcgbrasil.com.br/Divulgacao-informacoes/Gestao-Risco/Paginas/Risco-de-Credito.aspx - Acesso em: 29/11/2021

