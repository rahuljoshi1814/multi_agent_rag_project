from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.agents.schema_agent import extract_schema_info
from app.agents.sql_generator_agent import generate_sql
from app.agents.retriever_agent import execute_query
from app.agents.synthesizer_agent import synthesize_answer
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Query(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
def ask(query: Query):
    question = query.question
    schema = extract_schema_info(question)
    sql_query = generate_sql(question, schema)
    result = execute_query(sql_query)
    answer = synthesize_answer(question, result)

    return {
        "answer": answer,
        "intermediate_steps": {
            "schema": schema,
            "sql_query": sql_query,
            "result": result
        }
    }
