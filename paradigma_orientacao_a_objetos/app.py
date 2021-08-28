# Abaixo exemplo de importação informando de onde importar e qual módulo
# e em seguida o import é qual função será importada dentro desse módulo,
# podendo importar ser importadas várias funções sendo separadas por vírgula
from pacote_media_escolar.media_escolar import media, bem_vindo

# Abaixo exemplo de importação padrão
# import pacote_media_escolar.media_escolar

media = media(8, 9, 7, 9)
bem_vindo()
print(media)
