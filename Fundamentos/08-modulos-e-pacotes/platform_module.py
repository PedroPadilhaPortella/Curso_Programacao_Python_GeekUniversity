import platform

print(f"Plataforma: {platform.platform(aliased = False, terse = False)}")
print(f"Maquina: {platform.machine()}")
print(f"Processador: {platform.processor()}")
print(f"Sistema Operacional: {platform.system()}")
print(f"Versão: {platform.version()}")

print(f"Implementação do Python: {platform.python_implementation()}, versão {platform.python_version()}")