[README.md](https://github.com/user-attachments/files/24425078/README.md)
# 📄 Telegram Bot – Monitor de Google Docs

Este projeto é um **bot do Telegram** que monitora automaticamente um **Google Docs** e envia uma **notificação no Telegram** sempre que o documento for alterado.

Ideal para acompanhar **escalas, cronogramas, documentos acadêmicos ou administrativos** sem precisar verificar manualmente.

---

## 🚀 Funcionalidades
- ✅ Monitora um Google Docs público (somente leitura)
- 🔄 Verificação automática a cada **1 hora**
- 🔔 Envia alerta no Telegram quando houver qualquer alteração
- 🕒 Informa data e hora da modificação detectada
- ☁️ Pronto para rodar gratuitamente no **Railway**
- 🔐 Uso de variáveis de ambiente (mais seguro)

---

## 🧠 Como funciona
1. O bot baixa o conteúdo do Google Docs em formato texto
2. Gera um **hash (SHA-256)** do conteúdo
3. Compara com a última versão salva
4. Se houver diferença → envia mensagem no Telegram

---

## 📦 Requisitos
- Python **3.10+**
- Conta no **Telegram**
- Conta no **GitHub**
- Conta gratuita no **Railway**

---

## 📁 Estrutura do projeto
```
telegram-docs-monitor/
├── bot_monitor_docs.py
├── requirements.txt
├── README.md
```

---

## ⚙️ Variáveis de ambiente
Configure estas variáveis no serviço de hospedagem (Railway):

| Variável | Descrição |
|--------|----------|
| `BOT_TOKEN` | Token do bot do Telegram |
| `CHAT_ID` | ID do chat que receberá as mensagens |
| `DOC_ID` | ID do Google Docs monitorado |

---

## 🛠️ Instalação local (opcional)
```bash
pip install -r requirements.txt
python bot_monitor_docs.py
```

---

## ☁️ Deploy gratuito no Railway (resumo)
1. Suba este repositório no GitHub
2. Crie um projeto em https://railway.app
3. Conecte o repositório
4. Configure as variáveis de ambiente
5. Use como comando de start:
```
python bot_monitor_docs.py
```

---

## 🧪 Teste
- Faça qualquer alteração no Google Docs
- Aguarde até **1 hora**
- Receba a notificação automaticamente no Telegram

---

## 🔒 Segurança
⚠️ **Nunca versionar o BOT_TOKEN no código**  
Use sempre variáveis de ambiente.

Se o token for exposto:
- Acesse **@BotFather**
- Use o comando `/revoke`

---

## 📌 Possíveis melhorias
- 📅 Gerar automaticamente arquivos `.ICS` (Google Agenda)
- 🧠 Detectar apenas mudanças relevantes
- 📊 Histórico de versões
- 📂 Monitorar múltiplos documentos

---

## 📜 Licença
Uso livre para fins pessoais e educacionais.
