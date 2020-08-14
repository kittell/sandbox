'''
Created on Jul 7, 2020

@author: kirk@kirkkittell.com
'''

class Bond:
    def __init__(self, par):
        self.par = par
        return
    
    def set_ytm(self, ytm):
        self.ytm = ytm
        return
    
    def set_rate(self, rate):
        self.rate = rate
        return
        
    def set_term(self, term):
        self.term = term
        return
    
    def set_comp_freq(self, m):
        self.m = m
    
    def calc_price(self):
        self.coupon = (self.rate / self.m) * self.par
        self.price = (self.coupon / self.ytm) * (1 - (1 / (1 + self.ytm)) ** self.term)
        self.price += self.par / (1 + self.ytm) ** self.term
        
        return self.price
    
#     def calc_ear(self):
#         self.ear = 
#         return self.ear


def p1():
    b = Bond(100)
    b.set_term(6)
    b.set_rate(0.05375)
    b.set_ytm(0.02)
    b.set_comp_freq(1)
    print(b.calc_price())
    print(b.coupon)
    return


class CashFlow:
    def __init__(self):
        return

    def add_projection(self):
        return
    