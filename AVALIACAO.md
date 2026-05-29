# Avaliação de Recuperação – Desenvolvimento de Algoritmos com Python

## Informações Gerais

**Data:** 29/05/2026

**Tempo:** 2 horas

---

# Sistema de Gerenciamento de Turma

Uma escola deseja desenvolver um sistema simples para registrar as notas dos alunos de uma turma.

Seu objetivo é desenvolver um programa em Python que permita cadastrar alunos, armazenar suas notas e gerar informações sobre o desempenho da turma.

Durante o desenvolvimento, utilize os conceitos estudados na Unidade Curricular:

* Lógica de programação;
* Variáveis e constantes;
* Entrada e saída de dados;
* Operadores aritméticos e relacionais;
* Estruturas condicionais;
* Estruturas de repetição;
* Funções;
* Listas;

---

# Requisitos do Sistema

## 1. Cadastro dos alunos

O sistema deverá solicitar o cadastro de **5 alunos**.

Para cada aluno deverão ser informados:

* Nome;
* Nota 1;
* Nota 2;
* Nota 3.

As informações deverão ser armazenadas em uma estrutura de dados adequada.

---

## 2. Função para cálculo da média

Crie uma função chamada:

```python
calcular_media()
```

A função deverá retornar a média do aluno.

---

## 3. Função para verificar situação

Crie uma função chamada:

```python
verificar_situacao()
```

A função deverá retornar:

| Média                                    | Situação    |
| ---------------------------------------- | ----------- |
| Média maior ou igual a 60                | Aprovado    |
| Média maior ou igual a 40 e menor que 60 | Recuperação |
| Média menor que 40                       | Reprovado   |

---

## 4. Exibição dos resultados

Após o cadastro dos alunos, exiba uma tabela contendo:

```text
Nome                Média          Situação
------------------------------------------------
João                75.0           Aprovado
Maria               52.0           Recuperação
Pedro               30.0           Reprovado
```

---

## 5. Estatísticas da turma

Ao final do programa exiba:

### Quantidade de alunos:

* Aprovados;
* Em Recuperação;
* Reprovados.

### Maior média da turma

Exemplo:

```text
Maior média da turma: 92.5
```

### Menor média da turma

Exemplo:

```text
Menor média da turma: 38.0
```

### Média geral da turma

Exemplo:

```text
Média geral da turma: 67.4
```

---

## 6. Pesquisa de aluno

Após exibir os resultados, solicite ao usuário o nome de um aluno.

O sistema deverá pesquisar o aluno cadastrado e exibir:

```text
Aluno encontrado!

Nome: João
Média: 75.0
Situação: Aprovado
```

Caso o aluno não exista:

```text
Aluno não encontrado.
```

---

## 7. Utilização obrigatória de funções

O programa deve possuir obrigatoriamente as seguintes funções:

```python
calcular_media()
verificar_situacao()
pesquisar_aluno()
```

Outras funções podem ser criadas livremente.

---

# Critérios de Avaliação

| Critério                                  |
| ----------------------------------------- |
| Organização e legibilidade do código      |
| Uso correto de variáveis e operadores     |
| Uso correto de funções                    |
| Uso correto de estruturas condicionais    |
| Uso correto de estruturas de repetição    |
| Manipulação de listas ou listas aninhadas |
| Cálculo correto das estatísticas          |
| Pesquisa de aluno                         |
| **Total**                                 |

---

# Desafio

Transforme o programa em um sistema com menu:

```text
1 - Cadastrar alunos
2 - Listar alunos
3 - Pesquisar aluno
4 - Exibir estatísticas
5 - Sair
```

Utilize uma estrutura de repetição para manter o sistema em execução até que o usuário escolha a opção **Sair**.

---

# Entrega

1. Desenvolva o programa em Python.
2. Salve o arquivo em **seurepositório/respostas/seunome** com o nome:

```text
avaliacao_final.py
```

3. Realize commit das alterações.
4. Abra um Pull Request para entrega da atividade.

Boa avaliação!
