# Custom Stack - Testes

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

-   Python 3.x
-   pip (gerenciador de pacotes do Python)

------------------------------------------------------------------------

## 🚀 Passo a passo para rodar o projeto

### 1. Clonar ou baixar o repositório

``` bash
git clone https://github.com/eberssj/custom_stack
cd custom-stack
```

------------------------------------------------------------------------

### 2. Criar ambiente virtual

``` bash
python -m venv .venv
```

------------------------------------------------------------------------

### 3. Ativar o ambiente virtual

#### Windows:

``` bash
.venv\Scripts\activate
```

#### Linux/Mac:

``` bash
source .venv/bin/activate
```

------------------------------------------------------------------------

### 4. Instalar dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🧪 Rodando os testes

Para executar todos os testes:

``` bash
pytest
```

------------------------------------------------------------------------

## 📊 Rodando testes com cobertura

Para verificar a cobertura de testes:

``` bash
pytest --cov=src --cov-report=term-missing
```

Isso exibirá:

-   porcentagem de cobertura
-   linhas não testadas (se houver)

------------------------------------------------------------------------

## ✅ Resultado esperado

Todos os testes devem passar:

    9 passed

E a cobertura deve ser:

    100%

------------------------------------------------------------------------

## 📁 Estrutura do projeto

    custom-stack/
    ├── src/
    │   ├── custom_stack_class.py
    │   └── number_asc_order.py
    ├── test/
    │   ├── custom_stack_test.py
    │   └── test_number_asc_order.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 💡 Observações

-   O projeto utiliza **pytest** para testes
-   A cobertura é medida com **pytest-cov**
-   Nenhuma modificação foi feita na classe original `CustomStack`

------------------------------------------------------------------------

## 👨‍💻 Autor

Projeto acadêmico para estudo de testes unitários, cobertura e uso de
estruturas de dados em Python.
