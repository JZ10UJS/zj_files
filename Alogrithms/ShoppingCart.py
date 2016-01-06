#!usr/bin/python
# coding:utf-8

class ShoppingCart(object):
    """购物车"""
    items_in_cart = {}
    
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def display_cart(self):
        print '\nI got'
        print '*' * 10
        for item in self.items_in_cart:
            print '%d %d dollar %s' % (self.items_in_cart[item][1],
                                       self.items_in_cart[item][0],
                                       item)
        print '*' * 10,'\n'

    def add_item(self, product, price, number):
        """增加商品到购物车
        购物车以字典{product:[price,number]}形式存储"""
        if product not in self.items_in_cart:
            self.items_in_cart[product] = [price, number]    
        else:
            self.items_in_cart[product][1] += number 
        print '%d %s added' % (number, product)

    def remove_item(self, product, number):
        """移除商品"""
        if number > self.items_in_cart[product][1]:
            print 'I even don\'t have that much'
        else:
            if product in self.items_in_cart:
                self.items_in_cart[product][1] -= number 
                print '%d %s romoved' % (number, product)
                if self.items_in_cart[product][1] == 0:
                    del self.items_in_cart[product]
            else:
                print '%s is not in the cart' % product
                
    def total_money(self):
        """购物车总价格"""
        sumall = 0
        for item in self.items_in_cart:
            sumall += self.items_in_cart[item][0] * self.items_in_cart[item][1]
        return sumall
if __name__ == '__main__':    
    zj = ShoppingCart('ZHANGJIE')
    print zj.items_in_cart
    zj.add_item('Iphone',99,2)
    zj.add_item('Nokia',29,1)
    zj.add_item('Samsung',49,1)
    zj.display_cart()
    zj.add_item('Iphone',99,1)
    zj.display_cart()
    zj.remove_item('Iphone',2)
    zj.remove_item('Samsung',1)
    zj.remove_item('Nokia',2)
    print 'Now I have',zj.items_in_cart
    print 'Total money', zj.total_money()
