"""
5. Створити механізм обробки ситуацій, коли користувач намагається завершити операцію,
для якої у нього недостатньо коштів на рахунку.
Вимоги:
Створити клас InsufficientFundsException, наступний від виключеного базового класу.
Додайте наступні властивості:
required_amount: грошова сума, необхідна для виконання операції.
current_balance: поточний баланс рахунку.
Опціонально:
currency: валюта рахунку.
transaction_type: тип транзакції (наприклад, "withdrawal", "purchase").
Використання:
При спробі завершити операцію, перевірити достатню кількість коштів на рахунку. Якщо коштів недостатньо,
створіть екземпляр InsufficientFundsException з іншими значеннями властивостей і викиньте його.
Опрацювати виключення, щоб повідомити користувача про брак коштів і припинити виконання операції.
"""
currency_list = ['USD', 'EUR', 'UAH']
transaction_type_list = ["withdrawal", "purchase"]


class InsufficientFundsException(Exception):
    def __init__(self, required_amount, current_balance, msg="Insufficient funds to complete the transaction"):
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'Your balance is {self.current_balance} -> {self.msg} ({self.required_amount})'


def check_transaction(required_amount, current_balance, currency, transaction_type):
    if required_amount > current_balance:
        raise InsufficientFundsException(required_amount, current_balance)
    else:
        print(f"Transaction {transaction_type} {required_amount} {currency} successes!")

try:
    check_transaction(156, 1534, currency_list[2], transaction_type_list[1])
    # check_transaction(156345, 1534, currency_list[2], transaction_type_list[1])
except InsufficientFundsException as ex:
    print(f'{ex.__class__}: {ex}')



