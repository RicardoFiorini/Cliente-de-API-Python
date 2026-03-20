# Cliente de API Python
Este projeto é um exemplo prático de como construir um **cliente de API** robusto utilizando a linguagem Python. O foco principal é a integração com serviços de terceiros para buscar, tratar e exibir dados dinâmicos.[1]
## Funcionalidades

- Realização de requisições HTTP para APIs REST.
- Tratamento e processamento de dados em formato JSON.
- Consulta de condições climáticas em tempo real através do *weather_app.py*.
[1]
## Tecnologias Utilizadas
| Ferramenta | Finalidade |
| --- | --- |
| Python 3 | Linguagem de programação principal |
| Requests | Biblioteca para chamadas HTTP |
| JSON | Formato de intercâmbio de dados |[1]
## Exemplo de Execução
Para testar a aplicação de clima, execute o arquivo principal:
```bash

python weather_app.py

```
## Status do Projeto
- [x] Estrutura base de requisições
- [x] Integração com API de Clima
- [ ] Implementação de cache para evitar múltiplas requisições
- [ ] Criação de interface via terminal mais visual
> [!TIP]
> Importante: Certifique-se de ter uma chave de API válida configurada nas variáveis de ambiente ou diretamente no código para que as consultas funcionem corretamente!
