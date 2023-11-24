"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Neste script mostramos como "ter controle" da resposta
a uma consulta em formato JSON.
"""
# Substitua sua chave de API OpenAI:
import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']


from openai import OpenAI
client = OpenAI()

"""
Observações:
============
* O modo JSON não garantirá que a saída corresponda a qualquer esquema específico, apenas que seja válida e analisada sem erros.

* Com o novo modo JSON, um desafio é o fato de que a saída JSON do modelo varia consideravelmente com cada consulta do 
  modelo devido ao fato de que um esquema não pode ser definido.

* Uma forma de criar consistência em termos de esquemas JSON é fazer uso do parâmetro 'seed', como você verá no exemplo de código abaixo.
  Para uma entrada bastante semelhante, se o parâmetro 'seed' for passado, o mesmo esquema JSON será repetido.

* Você deve sempre instruir o modelo a produzir JSON por meio de alguma mensagem na conversa, por exemplo, por meio da mensagem do 
  sistema. Definir apenas o sinalizador de formato de resposta não é suficiente.
"""

response = client.chat.completions.create(model="gpt-3.5-turbo-1106",
                                          response_format={ "type": "json_object" }, # O sinalizador JSON precisa ser definido
                                          messages=[
                                            {"role": "system", "content": "Você é um assistente útil projetado para gerar JSON."},
                                            {"role": "user", "content": "Quantas medalhas olímpicas Usain Bolt tem e de quais jogos?"}
                                                   ],
                                          temperature=0,
                                          max_tokens=250,
                                          top_p=1,
                                          frequency_penalty=0,
                                          presence_penalty=0,
                                          seed=1001
                                        )


print(response.choices[0].message.content)
print("🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗")
print (response)
