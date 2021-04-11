def data_to_string(data):
    try:
        meses = ['janeiro, fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        mes = meses[int(data['mes']) - 2]
        return f"{data['dia']} de {mes} de {data['ano']}"
    except:
        return "Essa data está em fomato inválido!"

def get_date():
    try:
        data = dict()

        str_data = input("Qual a data atual (dd/mm/yyyy)? ")
        arr_data = str_data.split('/')
        data['dia'] = arr_data[0]
        data['mes'] = arr_data[1]
        data['ano'] = arr_data[2]

        print(data_to_string(data))
    except:
        print("Essa data está em fomato inválido!")



get_date()