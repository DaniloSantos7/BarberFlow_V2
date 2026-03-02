# Funções de Bcrypt (Priority Zero)

import bcrypt

def gerar_hash_senha(senha_plana: str) -> str:
    """Transforma a senha em um hash seguro usando Bcrypt."""
    # O sal (salt) adiciona aleatoriedade para evitar ataques de dicionário
    sal = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha_plana.encode('utf-8'), sal)
    return hash_senha.decode('utf-8')

def verificar_senha(senha_digitada: str, hash_do_banco: str) -> bool:
    """Verifica se a senha digitada corresponde ao hash salvo."""
    try:
        return bcrypt.checkpw(
            senha_digitada.encode('utf-8'), 
            hash_do_banco.encode('utf-8')
        )
    except Exception:
        return False