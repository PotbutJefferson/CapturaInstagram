import requests # conexão com página web
import json
import urllib3

# Definição de hashtag
hashtag = 'moda44'

url_base = 'https://www.instagram.com/explore/tags/' + hashtag + '/?__a=1&max_id='

http = urllib3.PoolManager()

has_next_page = True
end_cursor    = '' 
dados = None
while has_next_page: # Fazendo paginação
    
    # Estabelece conexão e extrai JSON
    print(url_base + end_cursor)

    dados = http.request('GET', url_base)
    dados = json.loads(dados.data.decode('utf-8'))
    
    # Captura todas as publicações da página
    publicacoes = dados['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    
    for publicacao in publicacoes:
    
        legenda   = publicacao['node']['edge_media_to_caption']['edges'][0]['node']['text']
        n_comm    = publicacao['node']['edge_media_to_comment']['count']
        n_like    = publicacao['node']['edge_liked_by']['count']
        shortcode = publicacao['node']['shortcode']
        timestamp = publicacao['node']['taken_at_timestamp']

        print(shortcode, '-', timestamp)
        print(legenda)
        print('Número de comentários:', n_comm, 'Número de likes:', n_like)

        print('\n==============================\n')
    
    # Verifica se existe próxima página
    has_next_page = dados['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    if has_next_page:
        end_cursor    = dados['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']