# DOCUMENTAÇÃO
http://127.0.0.1:8000/api/docs/


0. (Signup) Rota de cadastro 
http://127.0.0.1:8000/api/cadastro/ - POST
body - {
    "email": "example@example.com",
    "password": "example123"
}
1. (Login) Rota para poder logar no sistema
http://127.0.0.1:8000/api/api-token-auth/ - POST
body - {
	    "email":"admin@admin.com",
	    "password":"admin"
    }

2. (Index) Rota para listagem dos Navers.
http://127.0.0.1:8000/api/ - GET

3. (Show) Rota para detalhar informações de um único naver através de seu identificador
http://127.0.0.1:8000/api/usuario/{id}/ - GET

4. (Store) Rota de Criação de Naver
http://127.0.0.1:8000/api/usuario/ - POST  
body - {
            "name": "",
            "birthdate": null,
            "admission_date": null,
            "job_role": "",
            "projetos": null
        }
5. (Update) Rota Para Atualização de Naver
http://127.0.0.1:8000/api/usuario/ - PUT/PATCH
body - {
            "name": "",
            "birthdate": null,
            "admission_date": null,
            "job_role": "",
            "projetos": null
        }
6. (Delete) Rota Para Deletar um Naver        
http://127.0.0.1:8000/api/usuario/{id}/ - DELETE

7. (Index) Rota para listagem dos Projetos
http://127.0.0.1:8000/api/projetos/ - GET

8. (Show) Rota para detalhar um projeto
http://127.0.0.1:8000/api/projetos/{id}/ - GET

9. (Store) Rota de Criação de Projeto
http://127.0.0.1:8000/api/projetos/ - POST
body -  {
            "name": "",
            "lista_usuarios": []
        }

10. (Update) Rota Para Atualização de Projeto
http://127.0.0.1:8000/api/projetos/ - PUT/PATCH
body -  {
            "name": ""
        }

11. (Delete) Rota Para Deletar um Projeto
http://127.0.0.1:8000/api/projetos/{id}/ - DELETE


# TESTE
python manage.py test