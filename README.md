# **Documentação da API de Cursos**

## **Descrição**
Esta API gerencia informações relacionadas a cursos, formações e professores. Ela foi desenvolvida em Flask utilizando SQLAlchemy e banco de dados MySQL. A estrutura do projeto segue o padrão de camadas, com pastas dedicadas para modelos, serviços, schemas, views, e entidades. A API suporta operações CRUD completas e utiliza paginação nos endpoints.

---

## **Endpoints**

### **1. Cursos**
- **GET /cursos**: Retorna a lista de todos os cursos (com paginação).
- **POST /cursos**: Cadastra um novo curso.
- **GET /cursos/{id}**: Retorna detalhes de um curso específico.
- **PUT /cursos/{id}**: Atualiza as informações de um curso existente.
- **DELETE /cursos/{id}**: Remove um curso pelo ID.

### **2. Formações**
- **GET /formacoes**: Retorna a lista de todas as formações (com paginação).
- **POST /formacoes**: Cadastra uma nova formação.
- **GET /formacoes/{id}**: Retorna detalhes de uma formação específica.
- **PUT /formacoes/{id}**: Atualiza as informações de uma formação existente.
- **DELETE /formacoes/{id}**: Remove uma formação pelo ID.

### **3. Professores**
- **GET /professores**: Retorna a lista de todos os professores (com paginação).
- **POST /professores**: Cadastra um novo professor.
- **GET /professores/{id}**: Retorna detalhes de um professor específico.
- **PUT /professores/{id}**: Atualiza as informações de um professor existente.
- **DELETE /professores/{id}**: Remove um professor pelo ID.

---

## **Exemplo de Resposta**

### **GET /cursos**

**Requisição:**
```http
GET /cursos?page=1&per_page=2 HTTP/1.1
```
{
  "data": [
    {
      "id": 1,
      "nome": "Curso de Python",
      "descricao": "Aprenda Python do básico ao avançado",
      "formacao_id": 1
    },
    {
      "id": 2,
      "nome": "Curso de Java",
      "descricao": "Domine a linguagem Java e seus frameworks",
      "formacao_id": 2
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 2,
    "total": 10
  }
}

