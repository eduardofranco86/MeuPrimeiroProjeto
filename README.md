# MeuPrimeiroProjeto
# CTRL+ALT+T

# Remove o projeto antigo
 rm -rf MeuPrimeiroProjeto

# Atualiza o projeto 
git clone https://github.com/eduardofranco86/MeuPrimeiroProjeto.git

# Muda de diretório
cd MeuPrimeiroProjeto

# Abre o code do projeto atual
code . 


## Se o git não estiver instalado
conda install git 

## Rejeitar todas as alterações do seu repositório e a atualizar para a última versão
git fetch origin
## Depois 
git reset --hard origin/main
