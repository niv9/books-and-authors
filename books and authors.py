# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:33:25 2024

@author: MS Surface Laptop
"""


class Citizen:
    def __init__(self,name,price,author,published):
        self.name=name
        self.price=price
        self.author=author
        self.published=published
        
        
    def add_citizen(self):
        print("Name:"+self.name)
        print("price"+self.price)
        print("author:"+self.author)
        print("published:"+self.published)
        
citizen1 = Citizen("harry potter and the philosophers stone","1928","J.K.rowling","1997")
citizen1.add_citizen()


citizen2 = Citizen("diary of a wimpy kid","700","jeff kinney","2017")
citizen2.add_citizen()


        
        
        