def exchange_money(budget, exchange_rate):
    exchanged_value = budget / exchange_rate
    return exchanged_value
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """


def get_change(budget, exchanging_value):
    amountLeft = budget - exchanging_value
    return amountLeft
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    pass


def get_value_of_bills(denomination, number_of_bills):
    totalLeft = number_of_bills 
    return totalLeft * denomination
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    pass


def get_number_of_bills(budget, denomination):
    numberAfter = budget / denomination
    return int(numberAfter)


    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    pass


def get_leftover_of_bills(budget, denomination):
    leftover = budget % denomination
    return leftover
    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread /= 100
    exchange_rate *= 1 + spread
    currency = exchange_money(budget, exchange_rate)
    bills = get_number_of_bills(currency, denomination)
    newValue = bills * denomination
    return int(newValue)

    # - You need to calculate `spread` percent of `exchange_rate` using multiplication operator and add it to `exchange_rate` to get the exchanged currency.

    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    pass
