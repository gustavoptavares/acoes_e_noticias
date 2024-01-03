import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objs as go
import yfinance as yf
import requests
from bs4 import BeautifulSoup

# URLs específicos para cada ação
urls = {
    "PETR4": "https://braziljournal.com/?s=petrobras",
    "CEAB3": "https://braziljournal.com/?s=C%26A",
    "WEGE3": "https://braziljournal.com/?s=WEG"
}

# Função para obter dados de cotação e criar gráfico candlestick
def create_candlestick(ticker):
    stock_data = yf.Ticker(f"{ticker}.SA").history(period='3y')
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                open=stock_data['Open'], high=stock_data['High'],
                low=stock_data['Low'], close=stock_data['Close'],
                increasing_line_color='green', decreasing_line_color='red')])
    fig.update_layout(
        title=f"{ticker} - Gráfico Candle Referente as Cotações dos Últimos 3 Anos",
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        paper_bgcolor='rgba(0, 0, 0, 1)',
        plot_bgcolor='rgba(0, 0, 0, 1)',
        font=dict(color='white')
    )
    return fig

# Função para fazer o scraping das notícias
def get_news_from_brazil_journal(ticker):
    url = urls.get(ticker, "")
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', limit=3)
        news_data = []
        for article in articles:
            title = article.find('h2').get_text().strip()
            link = article.find('a', href=True)['href']
            news_data.append((title, link))
        return news_data
    else:
        return [("Notícia não encontrada ou erro na página", "#")]

# Inicializar o aplicativo Dash
app = Dash(__name__)

# Aqui é onde você incluiria o CSS externo em um cenário real
# app.css.append_css({"external_url": "https://your-cdn.com/your-css-file.css"})

# Definir o layout do aplicativo
app.layout = html.Div([
    html.H1("Dashboard de Ações e Notícias", style={'textAlign': 'center', 'color': 'white'}),
    dcc.Dropdown(
        id='stock-selector',
        options=[
            {'label': 'CEAB3 - C&A Modas', 'value': 'CEAB3'},
            {'label': 'WEGE3 - WEG S.A.', 'value': 'WEGE3'},
            {'label': 'PETR4 - Petrobras', 'value': 'PETR4'}
        ],
        placeholder="Selecione uma ação",
        style={'width': '50%', 'margin': '0 auto 20px', 'color': 'white'}
    ),
    html.Div([
        dcc.Graph(id='candlestick-graph', style={'flex': '1'}),
        html.Div([
            html.H2("Notícias", style={'textAlign': 'center', 'color': 'white'}),
            html.Div(id='news-content', style={
                'overflowY': 'scroll', 'height': '500px', 'border': '1px solid #333',
                'padding': '20px', 'margin': '10px', 'borderRadius': '5px',
                'backgroundColor': 'black', 'color': 'white'
            })
        ], style={'flex': '1', 'minWidth': '300px'}),
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'backgroundColor': 'black', 'color': 'white'}),
], style={'backgroundColor': 'black', 'color': 'white', 'height': '100vh', 'padding': '20px'})

# Callback para atualizar o gráfico candlestick e as notícias
@app.callback(
    [Output('candlestick-graph', 'figure'), Output('news-content', 'children')],
    [Input('stock-selector', 'value')]
)
def update_content(value):
    if value:
        fig = create_candlestick(value)
        news_data = get_news_from_brazil_journal(value)
        news_links = [html.A(href=link, target="_blank", children=title, style={'display': 'block', 'marginBottom': '10px', 'color': 'white'}) for title, link in news_data]
        return fig, news_links
    else:
        return {}, []

# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)