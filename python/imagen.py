import openai
from openai.api_resources import * # noqa
from openai.api_resources.completion import Completion
from openai.api_resources.abstract.engine_api_resource  import EngineAPIResource 
from openai.api_resources.abstract.api_resource  import APIResource
from openai import api_requestor, error,util,six
from openai import error, http_client, version, util, six
from openai import error, util, six
from openai.six.moves.urllib.parse import parse_sql
from urllib.parse import urlparse, urlencode, quote_plus, unquote_plus






openai.api_key = key

modelo = 'gpt-3.6-turbo'

promt = "Capital de Perú"

mensajes = [

    {'role':'system', 'content':'dame una respuesta de 4 líneas'},
    {'role':'user', 'content':promt}

]

respuesta = openai.ChatCompletion.create(
    model = modelo,
    messages = mensajes,
    temperatura = 0.8,
    max_tokens = 1000
)

print(respuesta)