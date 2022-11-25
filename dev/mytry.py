# def my_dec(fun):
# 	def my_inner(x=1):
# 		x = 4
# 		return fun(x) 
# 	return my_inner


# @my_dec
# def my_mul(x):
# 	return x+x+x


# print(my_mul())
# /////////////////////////////////////////////
# def my_upper(fun):
# 	def my_inner():
# 		result = fun()
# 		print(result.capitalize())
# 		return result

# 	return my_inner

# @my_upper
# def my_name():
# 	return 'jayraj'

# @my_upper
# def my_last_name():
# 	return 'thakkar'


# my_name()
# my_last_name()
#////////////////////////////////////////////

# def my_recursion(a):
# 	if(a>0):
# 		my_data = a + my_recursion(a-1)
		
# 		print(my_data)

# 	else:
# 		my_data = 0	
# 	return my_data

# x = int(input("enter a number:--"))
# my_recursion(x)



# Greatest common number 

# def my_gcd(a,b):
# 	a,b = b%a,a
# 	if a == 0 :
# 		return b
# 	else:
# 		return my_gcd(a,b)



# print(my_gcd(10,74))

## Hasattr

# class my_data():
# 	name = 'jay'
# 	def my_name(self,what):
# 		name1=what
# 		 #(self.name,what)
# 		 # print(name)

# x = my_data()

# print(hasattr(x,'name'))
# print(hasattr(x,'my_name'))
# print(hasattr(x,'false'))

# # GEtattr


# print(getattr(x,'my_name.name1')('Hello'))
# # print(getattr(x,'name'))

import datetime

a = datetime.datetime.now()
print(a.strftime('%a'))
print(a.strftime('%A'))
print(a.strftime('%b'))
print(a.strftime('%B'))
print(a.strftime('%c'))
print(a.strftime('%C'))
print(a.strftime('%d'))
print(a.strftime('%D'))
print(a.strftime('%e'))
print(a.strftime('%f'))
print(a.strftime('%F'))
print(a.strftime('%G'))
print(a.strftime('%h'))
print(a.strftime('%H'))
print(a.strftime('%I'))
/print(a.strftime(''))













