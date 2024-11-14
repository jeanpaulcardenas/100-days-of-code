class CoffeeMachine:
    MENU = {
        'espresso': {
            'ingredients': {
                'water': 50,
                'coffee': 18,
                'milk': 0
            },
            'cost': 1.5
        },

        'latte': {
            'ingredients': {
                'water': 200,
                'coffee': 24,
                'milk': 150
            },
            'cost': 2.5
        },

        'cappuccino': {
            'ingredients': {
                'water': 250,
                'coffee': 24,
                'milk': 100
            },
            'cost': 3.0
        }}
    COIN_VALUES = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }

    def __init__(self):
        self.resources = {
            'ingredients': {
                'water': 1000,
                'coffee': 500,
                'milk': 750,
            },
            'money': 0
        }

    def process_coins(self):
        print('Please insert coins')
        coins_inserted = {}
        for k in self.COIN_VALUES.keys():
            coins_inserted[k] = int(input(f'how many {k}?'))
        return sum([self.COIN_VALUES.get(k)*v for (k, v) in coins_inserted.items()])

    def transaction_successful(self, money_inserted: float, drink: str):
        cost = self.MENU[drink]['cost']
        if money_inserted >= cost:
            self.resources['money'] += cost
            print(f'here is your change {money_inserted - cost}')
            return True
        else:
            print('sorry, not enough money. money refunded')
            return False

    def check_resources(self):
        print(self.resources)

    def check_resources_sufficient(self, drink):
        for resource, amount in self.MENU[drink]['ingredients'].items():
            if amount > self.resources['ingredients'][resource]:
                print(f'Sorry there is not enough {resource}')
                return False
        return True

    def make_coffee(self, drink):

        self.resources['ingredients'] = {
            k: (v - self.MENU[drink]['ingredients'].get(k)) for (k, v) in self.resources['ingredients'].items()
        }
        print(f'Here is your {drink}. Enjoy!!!!')

    def start_machine(self):
        on = True
        while on:
            prompt = input('What would you like?').lower()
            if prompt == 'report':
                self.check_resources()

            elif prompt == 'off':
                on = False

            else:
                drink = prompt
                try:
                    if self.check_resources_sufficient(drink):
                        money_inserted = self.process_coins()
                        if self.transaction_successful(money_inserted, drink):
                            self.make_coffee(drink)

                except KeyError:
                    print('sry, please type in correctly. options are: espresso, latte, cappuccino')




machine = CoffeeMachine()
machine.start_machine()
