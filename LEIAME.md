# Guia de Instalação e Configuração — Builder

Este documento contém o guia prático de comandos de terminal para instalação, compilação de assets frontend (Vue 3/Vite), migração e manutenção do aplicativo **Builder** no ecossistema **ERPZ**.

> ⚠️ **Importante**: Substitua `[sitename]` pelo nome do site onde deseja operar (ex: `dev.erpz.io`).

---

## 1. Instalação no Bench

Acesse a pasta do seu bench:

```bash
cd ~/bench
```

Baixe o aplicativo a partir do repositório:

```bash
bench get-app https://github.com/andradezdev/builder.git
```

Instale as dependências JavaScript do construtor:

```bash
cd ~/bench/apps/builder
yarn install
```

Compile os arquivos da interface frontend (Vue 3 / Vite):

```bash
yarn build
```

Volte para a pasta do bench e instale o aplicativo no site de destino:

```bash
cd ~/bench
bench --site [sitename] install-app builder
```

Execute a sincronização de tabelas e modelos de bloco:

```bash
bench --site [sitename] migrate
```

Compile os assets de integração e limpe o cache:

```bash
bench build --app builder
bench --site [sitename] clear-cache
```

---

## 2. Acesso e Uso no Desk

1. **Acesso pelo Desk:**
   - No painel inicial do ERPZ (`/desk`), clique no ícone **Builder**.
   - No Workspace do Builder, utilize o botão **Abrir Builder** para acessar a interface visual completa em tela cheia (`/builder`).

2. **Criação de Páginas:**
   - Na lista de **Páginas do Builder**, clique em **Nova Página**.
   - Defina a rota pública desejada (ex: `/sobre`, `/solucoes`, `/landing-page`).
   - Use o editor interativo para compor os blocos, ajustar tipografia e publicar.

---

## 3. Atualização do Aplicativo

Para sincronizar o aplicativo com as últimas modificações do repositório:

```bash
cd ~/bench/apps/builder
git pull origin develop
yarn install
yarn build
cd ~/bench
bench build --app builder
bench --site [sitename] migrate
bench --site [sitename] clear-cache
```

Se necessário, reinicie os processos de execução:

```bash
sudo supervisorctl restart all
```

---

## 4. Desinstalação

Para desinstalar o aplicativo de um site específico:

```bash
cd ~/bench
bench --site [sitename] uninstall-app builder
```

Para remover o aplicativo completamente do bench:

```bash
bench remove-app builder
```
