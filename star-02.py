'''Elabore um algoritmo para mostrar os números primos existentes em um
intervalo.
O usuário deverá fornecer os valores inicial (inicial > 0) e final (inicial <
final) e os números primos existentes no intervalo ([inicial, final]) devem
ser separados por um espaço em branco

Exemplo:
Entrada: 2 13
Saída: 2 3 5 7 11 13'''

intervalo = input('Digite os valores inicial e final '
                  'para descobrir os números primos existentes neste intervalo ')

intervalo_array = [int(i) for i in intervalo.split()]
print(intervalo_array)
num_one = int(intervalo_array[0])
num_two = int(intervalo_array[1])

for cada_numero in range(num_one, num_two):
    if cada_numero % 2 == 1 or cada_numero == 2:
        intervalo_array.append(int(cada_numero))

print('Entre {} e {}, são primos:'.format(num_one, num_two))

for each_primo in intervalo_array:
    print(each_primo)
