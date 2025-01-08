# ✉️ Automação de Email Gmail

## 📋 Sobre o Projeto

Script de automação em Python para envio de emails em massa através do Gmail. O projeto permite enviar emails automaticamente para múltiplos destinatários a partir de uma lista predefinida.

## 🚀 Funcionalidades

- Envio automatizado de emails
- Suporte para múltiplos destinatários
- Leitura automática de lista de emails
- Integração com Gmail

## 🛠️ Pré-requisitos

- Python 3.x
- Conta Gmail
- Configuração de "Acesso a app menos seguro" ativada na conta Google
- Arquivo de texto com lista de emails

## ⚙️ Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/betolara1/Automacao-de-Email-Gmail.git
   cd Automacao-de-Email-Gmail


2. Crie um arquivo `email.txt` com a lista de destinatários:

```plaintext
abc@abc.com
dce@dcr.com
par@par.com
```



## 📝 Como Usar

1. Prepare o arquivo `email.txt`:

1. Cada email deve estar em uma linha separada
2. Não deixe linhas em branco
3. Formato: um email por linha



2. Execute o script:
```shellscript
python main.py
```


## 📁 Estrutura do Projeto

```plaintext
Automacao-de-Email-Gmail/
├── main.py        # Script principal de automação
├── email.txt      # Lista de destinatários
└── README.md      # Documentação
```

## ⚠️ Observações Importantes

1. O nome do arquivo de emails deve ser **exatamente** "email.txt"
2. Se precisar mudar o nome do arquivo, atualize também no script
3. Certifique-se de que sua conta Google permite acesso a apps menos seguros
4. Mantenha suas credenciais seguras e não as compartilhe


## 🔒 Segurança

- Não compartilhe suas credenciais do Gmail
- Use uma conta secundária para testes
- Considere usar variáveis de ambiente para credenciais
- Evite compartilhar o arquivo email.txt com dados sensíveis


## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

- GitHub: [@betolara1](https://github.com/betolara1)


## 📧 Exemplo de Formato do email.txt

```plaintext
abc@abc.com
dce@dcr.com
par@par.com
```

## ❗ Troubleshooting

1. Se o script apresentar erro, verifique:

1. Se o arquivo email.txt existe no diretório
2. Se o nome do arquivo está correto
3. Se o formato dos emails está correto
4. Se suas credenciais do Gmail estão corretas



2. Em caso de erro de autenticação:

1. Verifique suas configurações de segurança do Google
2. Certifique-se que o acesso a apps menos seguros está ativado
3. Tente usar uma autenticação de dois fatores com senha de app



---

⭐️ Se este projeto te ajudou, considere dar uma estrela no GitHub!
