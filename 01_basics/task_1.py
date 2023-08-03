import random


# create a list of random integers
random_list = random.sample(range(0, 1000), 100)


# compare element[i] with next elements that have index > i
for i in range(len(random_list)):
    for j in range(i+1, len(random_list)):
        if random_list[i] > random_list[j]:
            # if element[i] > element[j] -> swap those elements
            random_list[i], random_list[j] = random_list[j], random_list[i]


# use filter() method to filter the list with the help of lambda function
# that tests each element in the list whether it odd or even
odd_elements = list(filter(lambda x: x % 2 != 0, random_list))
even_elements = list(filter(lambda x: x % 2 == 0, random_list))


# calculate average values of odd and even elements
avg_odd_elements = sum(odd_elements) / len(odd_elements)
avg_even_elements = sum(even_elements) / len(even_elements)


# output results in the console
print(f'average of odd elements: {avg_odd_elements}', f'average of even elements: {avg_even_elements}', sep='\n')
