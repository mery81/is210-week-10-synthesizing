#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 10 Synthesizing Tasks. """


def sum_orders(cus, ord):
    """Contain cunstomers dictionaries.

    Args:
        cus (dict): A dictionary of customers keyed by customer ID.
        ord (dict): A dictionary of orders keyed by order ID.
    """
    res = {}
    for key, value in cus.iteritems():
        order, total = getCustOrder(key, ord)
        temp = value
        temp.update({'orders': order, 'total': total})
        res[key] = temp
    return res


def getCustOrder(k, ord):
    """Contain cunstomers orders data

    Args:
        k (int): value of customer ID.
        ord (dict): A dictionary of orders keyed by order ID.
    """
    count = 0
    tot = 0
    for key, value in ord.iteritems():
        if value['customer_id'] == k:
            count = count+1
            tot = tot + value['total']
    return count, tot
