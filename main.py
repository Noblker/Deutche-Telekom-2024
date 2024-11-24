import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
import json
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "Inser OPENAI_API_key" #really insert
model = ChatOpenAI(model="gpt-4o-mini")
# j_string = '{"meno": "Timon", "vek": 18, "rok": 2007, "muz": True}'
# data = json.loads(j_string)
data:dict[str, any] = {"name": "Timon", "age": 18, "birth": 755, "man": True}
def check(k:str, v:any)->bool:
    system_template = "Check if the value is possible in respektive kategory: {kategory}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    chain = prompt_template | model
    response = chain.invoke({"kategory": k, "text": v})
    print(response.content)
for k in data:
    check(k, data[k])