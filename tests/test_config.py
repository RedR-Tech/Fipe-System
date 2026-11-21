from app.core.config import config

def imprimir(nome, ambiente, appDebug, url, timeout):
    print("Aplicação: ",nome)
    print("Ambiente: ",ambiente)
    print("Debug: ",appDebug)
    print("Tipo Debug: ",type(appDebug))
    print("API: ",url)
    print("Timeout: ",timeout)
    print("Tipo Timeout: ", type(timeout))

imprimir(config.APP_NAME, config.APP_ENV, config.APP_DEBUG, config.FIPE_API_URL, config.FIPE_API_TIMEOUT)