from fastapi import FastAPI, HTTPException
from uuid import UUID#, uuid4, bibliotecas não utilizadas podem ser removidas
from typing import List #, Union
# from pydantic import BaseModel
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("7e8be937-6130-4e8e-9c77-c5f832e4377d"), #uuid4() #após geração do id por esta função "uuid4()", apagou-se o código e colocou-se consta atualmente
        first_name="Ana",
        last_name="Maria",
        email="email@gmail.com",
        role=[Role.role_1]
    ),
    User(
        id=UUID("d5e5bb35-7333-4687-990f-da7e9c919b06"),
        first_name="Maria",
        last_name="Santos",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
    User(
        id=UUID("3959a2ec-4caf-43a4-9c33-d7806b36c5ff"),
        first_name="Camila",
        last_name="Silva",
        email="email@gmail.com",
        role=[Role.role_3]
    )
]

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/api/users") # listar usuários
async def get_users():
    return db;

@app.get("/api/users/{id}") # pesquisar usuários cadastrados
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users") # criar novo usuário detro da base
async def add_user(user: User):
    # o ** negrita
    '''
    Adicionar um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    '''
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id {id} não encontrado"
    )

# ATIVIDADE EXTRA HTTP PUT REQUESTS

# Exercício 1: ----------------------------------------------------------------------------------

@app.put("/api/users/{id}") # atualizar informações do usuário (UPDATE)
async def update_user(id: UUID):
    for user in db:
        if user.id == id:
            user.email = "email@yahoo.com"
            return user
        
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id {id} não encontrado"
    )


# ----------------------------------------------------------------------------------
# código do primeiro exemplo

'''class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, busca: Union[str, int] = None):
    return {"item_id": item_id, "busca": busca}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}'''