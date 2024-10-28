def greet(*args):
  for names in args:
    print (f"hello {names}")

greet("ABC","EFG","XYZ")


def sum_numbers(*args):
  return sum(args)

print(sum_numbers(1,2,3,4,5))


def order_summary(customer_name,*items):
  print(f"order for {customer_name}")
  for item in items:
    print(f"- {item}")

order_summary("Abc","apple","orange","mango")


def print_info(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}:{value}")

print_info(name="Abc",age=20,city="New York")



def build_profile(**kwargs):
  profile={}
  for key,value in kwargs.items():
    profile[key]=value
  return profile

user_profile=build_profile(name="ABC",age=30,city="New York")
print(user_profile)



def example_function(args1,args2,*args,**kwargs):
  print(f"args1:{args1}")
  print(f"args2:{args2}")
  print("Additional positional arguments", args)
  print("keyword arguments",kwargs)

example_function(1,2,3,4,5,6,7,8,key1="value1",key2="value2")













