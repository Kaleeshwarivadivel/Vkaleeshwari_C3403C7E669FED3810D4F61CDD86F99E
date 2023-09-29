"""
write a function called linearSearchProduct that takes the list of products and a target product
name as input.The function should perform a linear search to find the target product in the list and
return a list of indices of all occurrences of the product if found,or an empty list if the product is not 
found.
"""


def linearSearchProduct (productList, targetProduct):
  indices = []

  for index,product in enumerate (productList):
    if product == targetProduct: 
      indices.append(index)
    
  return indices 


# Example usage 
products = ["apple", "orange", " mango", "apple", "carrot", "apple"]
target = "apple"
target2 = "shoes"
result = linearSearchProduct (products, target) 
print(result)