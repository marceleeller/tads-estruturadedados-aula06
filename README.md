# Inversão de String com Pilha

Este projeto implementa a inversão de strings utilizando a estrutura de dados **pilha**. A pilha é utilizada para armazenar os caracteres da string e, ao desempilhar, obtemos a string invertida.

## Como funciona?
O programa:
1. Aceita uma string como entrada.
2. Insere cada caractere da string em uma pilha.
3. Utiliza o método `pop()` para remover e reconstruir a string na ordem inversa.

## Testes Realizados
Foram testadas diversas entradas para validar a solução:
✅ Palavras comuns (ex.: `"Python"`)
✅ Números (ex.: `"12345"`)
✅ Caracteres especiais (ex.: `"!@# $%&*"`)
✅ Frases com espaços (ex.: `"A casa é azul"`)
✅ Strings aleatórias (ex.: `"Stack"`)

Os testes demonstraram que a solução funciona corretamente para diferentes tipos de entradas.

## Conclusão
A implementação com pilha facilitou a inversão da string, pois permite que os caracteres sejam armazenados e removidos na ordem correta sem manipulações complexas. Essa abordagem é eficiente e ilustrativa do funcionamento da estrutura **LIFO (Last In, First Out)**.
