print("let's practise everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where thre is none.
"""

print("------------------\\\\\-----")
print(poem)
print("-----------------------")

five = 10 - 2 + 3 -6
print(f"This Should be five: {five}")

def secrate_formula(started):cls
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secrate_formula(start_point)

#Remember that this is the anothere way to format a string
print("With a starting point of : {}".format(start_point))
#it's just like with an F"" string
print(f"We'd jave {beans} beans, {jars} jars, and {crates} crates.")

start_point= start_point / 10

print("We can also do that this way:")
formula = secrate_formula(start_point)

#this is an easy way to apply a list to a format starting
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
