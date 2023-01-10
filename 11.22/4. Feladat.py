ez = ["Én", "nem", "vagyok", "egy", "csodabogár"]
az = ["Én", "nem", "vagyok", "egy", "csodabogár"]
print("Test 1:{0}".format(ez is az))
ez = az
print("Test 2:{0}".format(ez is az))
#Test 1: False, mivel a változók nem ugyan azok
#Test 2: True, mivel ez és az a 4. sorban egyenlő lett