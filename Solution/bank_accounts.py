bank = dict()

def deposit(name_and_sum, sign=1):
    name, summ = name_and_sum.split()
    bank[name] = bank.get(name, 0) + int(summ) * sign

def withdraw(name_and_sum):
    deposit(name_and_sum, sign=-1)

def balance(name):
    print(bank.get(name, 'ERROR'))

def transfer(name_and_sum):
    withdraw(' '.join(name_and_sum.split()[::2]))
    deposit(' '.join(name_and_sum.split()[1:]))

def income(prs):
    for name, summ in bank.items():
        bank[name] = int(summ * (1 + int(prs) / 100 * (summ > 0)))

commands = dict(DEPOSIT=deposit, WITHDRAW=withdraw, BALANCE=balance,
                TRANSFER=transfer, INCOME=income)

with open('input.txt', encoding='utf8') as inf:
    for line in inf:
        command, name_and_sum = line.strip().split(' ', 1)
        action = commands.get(command)
        action(name_and_sum)
