from datetime import datetime
import requests
import os


# link = https://pixe.la/v1/users/waronms/graphs/graph1.html
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("TOKEN_PIXELA")
GRAPH_ID = os.getenv("GRAPH_ID")


# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Reading Graph",
#     "unit": "Pages",
#     "type": "int",
#     "color": "sora",
# }

# Cria o usuário.
# response = requests.post(url=pixela_endpoint, json=user_params)

# Cria o gráfico.
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


header = {
    "X-USER-TOKEN": TOKEN
}


user_input = input("Olá, o que você gostaria de fazer?:\n"
                   "1 - Adicionar quantas páginas você leu hoje.\n"
                   "2 - Editar quantas páginas você leu em certa data.\n"
                   "3 - Deletar um dia do seu gráfico.\n"
                   "Por favor, digite 1, 2 ou 3.\n")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


# Adiciona uma nova entrada no gráfico.
if user_input == "1":
    today = datetime.now()
    pages_to_add = input("Quantas páginas você leu hoje?\n")
    post_pixel = {
        "date": today.strftime("%Y%m%d"),
        "quantity": pages_to_add,
    }
    post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
    response = requests.post(url=post_pixel_endpoint, json=post_pixel, headers=header)
    if response:
        print("Pronto!")
    else:
        print("Desculpe, algo deu errado.")


# Edita uma entrada no gráfico.
elif user_input == "2":
    day_to_update = input("Por favor, digite a data que gostaria de atualizar no formato dia/mês/ano.\n")
    day_to_update_f = "".join(day_to_update.split("/")[::-1])
    quantity_to_update = input("Quantas páginas você leu nesse dia?\n")
    update_pixel = {
        "quantity": quantity_to_update
    }
    update_pixel_endpoint = f"{post_pixel_endpoint}/{day_to_update_f}"
    response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=header)
    if response:
        print("Atualizado!")
    else:
        print("Desculpe, algo deu errado.")


# Deleta uma entrada no gráfico.
elif user_input == "3":
    day_to_delete = input("Por favor, digite a data para deletar no formato dia/mês/ano.\n")
    day_to_delete_f = "".join(day_to_delete.split("/")[::-1])
    delete_pixel = f"{post_pixel_endpoint}/{day_to_delete_f}"
    response = requests.delete(url=delete_pixel, headers=header)
    print(response.text)
    if response:
        print("Deletado!")
    else:
        print("Essa data não consta no seu gráfico.")


else:
    print("Não há essa opção.")
