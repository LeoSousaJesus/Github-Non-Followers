# GitHub Non-Followers Checker

## **Este é um programa em Python que verifica quais usuários do GitHub você segue, mas que não seguem você de volta. Ele utiliza a API do GitHub para obter as listas de seguidores e usuários que você segue, e então compara essas listas para identificar os usuários que não te seguem de volta. Caso queira deixar de seguir quem não te segue de volta basta executar o arquivo .py e verificar os nomes gerados na lista.**

## Funcionalidades
- Obtém a lista de usuários que você segue no GitHub.

- Obtém a lista de usuários que seguem você no GitHub.

- Compara as duas listas e identifica os usuários que você segue, mas que não seguem você de volta.

## Pré-requisitos

- Python 3.x instalado.

- Um token de acesso pessoal do GitHub com as permissões `read:user` e `read:follow`.

# **Como Usar**

## **Gerar um Token de Acesso Pessoal:**

- Vá para as configurações do seu perfil no GitHub.

- Navegue até "Developer settings" > "Personal access tokens". Você pode gerar um token em [GitHub Developer Settings](https://github.com/settings/tokens)

- Gere um novo token com as permissões `read:user` e `read:follow`.

## **Instalar Dependências:**

- O programa utiliza a biblioteca `requests`, para instalá-la use o pip:

**`pip install requests`**

## **Configurar o Script:**

- Abra o arquivo `github_non_followers.py` e substitua `'seu_token_aqui'` pelo seu token de acesso pessoal.

- Substitua `'seu_username_github'` pelo seu nome de usuário do GitHub.

## **Limitações**

- A API do GitHub tem um limite de requisições por hora. Se você tiver muitos seguidores ou estiver seguindo muitas pessoas, pode ser necessário lidar com a paginação ou usar um token com uma taxa de limite mais alta.

- **Importante:** mantenha seu token de acesso pessoal seguro e não o compartilhe publicamente.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## **Para executar o Script:**

- Salve o código em um arquivo Python, por exemplo, `github_non_followers.py`.

- Execute o script usando o comando:

```Python
python github_non_followers.py