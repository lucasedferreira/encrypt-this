# encrypt-this

Você deve implementar uma função chamada encryptThis(message) que criptografa uma mensagem de texto seguindo as regras especificadas abaixo:

A mensagem é uma string contendo palavras separadas por espaços.

Cada palavra na mensagem deve ser criptografada da seguinte maneira:

O primeiro caractere da palavra deve ser convertido para o seu código ASCII.

O segundo caractere da palavra deve ser trocado com o último caractere.

A função deve retornar a mensagem criptografada, mantendo a mesma estrutura de palavras separadas por espaços.

Aqui está um exemplo de como a função deve funcionar:

\>>> encryptThis("Hello") <br>
'72olle' <br>
\>>> encryptThis("good") <br>
'103doo' <br>
\>>> encryptThis("hello world") <br>
'104olle 119drlo' <br>
 

Você também deve criar pelo menos 4 testes unitários para garantir que a função está funcionando corretamente em diferentes casos.

Lembre-se de seguir as boas práticas de programação, fornecer comentários apropriados e garantir que sua função seja eficiente.

Instruções para Testes Unitários:

Você deve criar testes unitários para verificar se a função encryptThis está funcionando corretamente. Certifique-se de cobrir diferentes cenários, incluindo palavras de diferentes comprimentos e mensagens com várias palavras. Certifique-se de incluir comentários explicando o propósito de cada teste.

Exemplo de teste unitário:

```python
def test_encryptThis():

    assert encryptThis("Hello") == '72olle'  # Teste para palavra de cinco letra
```

Por favor, desenvolva a função e os testes unitários com base nas instruções fornecidas
