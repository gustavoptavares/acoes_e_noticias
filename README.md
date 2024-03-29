# Dashboard de ações e notícias

## Descrição Geral

O objetivo é criar um dashboard com cotações e notícias, utilizando a linguagem python e o framework dash + plotly, que mostra gráficos candlestick com as cotações dos últimos 3 anos das ações CEAB3, WEGE3 e PETR4 e exibe as três notícias mais atualizadas do Brazil Journal. 

O arquivo "app.py" é o script Dash, o diretório "assets" tem o arquivo CSS "style.css" com os estilos. Ao iniciar o aplicativo na IDE, o Dash automaticamente irá detectar os arquivos dentro do diretório assets e irá aplicá-los ao seu aplicativo.

## Tecnologias

Abaixo serão listadas todas as tecnologias de linguagens, bibliotecas e frameworks utilizados para desenvolvimento do dashboard.

• Python.

• Dash + plotly.

• Yfinance.

• Requests.

• BeautifulSoup.

• HTML.

• CSS.

## Etapas de Desenvolvimento

As etapas do desenvolvimento do dashboard foram as seguintes:

• Criar uma interface de usuário com Dash que combine o layout e os elementos de interface do usuário (dropdown para seleção de ações e exibição de notícias) em uma única aplicação Dash.

• Integrar a busca de dados de cotações com yfinance para buscar dados de cotações dos últimos 3 anos com base na seleção do usuário no dropdown.

• Gerar gráficos candlestick com Plotly das ações selecionadas.

• Realizar web scraping para notícias que integre a funcionalidade de scraping para buscar as três últimas notícias do site Brazil Journal relacionadas à ação selecionada.

• Unificar tudo em um layout Dash que combine todos esses elementos em um layout Dash coeso.


## Resultados

• Segue abaixo a imagem, que mostra o dashboard com o gráfico de candle, e as notícias listadas da ação CEAB3 - C&A Modas.


![Minha Imagem](https://github.com/gustavoptavares/acoes_e_noticias/blob/main/CEAB3.jpg)

• Segue abaixo a imagem, que mostra o dashboard com o gráfico de candle, e as notícias listadas da ação WEGE3 - WEG S.A.


![Minha Imagem](https://github.com/gustavoptavares/acoes_e_noticias/blob/main/WEGE3.jpg)


• Segue abaixo a imagem, que mostra o dashboard com o gráfico de candle, e as notícias listadas da ação PETR4 - Petrobras.


![Minha Imagem](https://github.com/gustavoptavares/acoes_e_noticias/blob/main/PETR4.jpg)
