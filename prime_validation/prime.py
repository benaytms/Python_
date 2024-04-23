from math import sqrt

def check_prime(n: int) -> bool:
    if (n == 1):
        return False
    
    limit = int(sqrt(n)) + 1
    
    for i in range(2, limit):
        if (n % i == 0):
            return False
    return True

def main() -> None:
    num = int(input("Digite um valor: "))

    if num <= 0:
        print("Deve ser positivo não nulo")
    elif (check_prime(num)):
        print("É primo")
    else: 
        print("Não é primo")

main()