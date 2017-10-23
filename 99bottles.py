import runtime
import varloader

runtime.reset_store()

input_set = varloader.build_input([
    "bottles of beer",
    " "]),
#    "on the wall",
#    "!"])
#    ,
#    99,
#    "Take one down, pass it around,", 
#    ",",
#    "\n"])
runtime.set_var("esc", 0)
runtime.set_var("bottles", input_set[1], str)
runtime.set_var("space", input_set[2], str)
#runtime.set_var("wall", input_set[2], str)
#runtime.set_var("!", input_set[3], str)
#runtime.set_var("count", input_set[5])
#runtime.set_var("take", input_set[6], str)
#runtime.set_var(",", input_set[7], str)
#runtime.set_var("newline", input_set[8], str)

while (runtime.get_var("count") > 0):
    print(runtime.get_var("count"))
    print(runtime.get_var("bottles"))
    print(runtime.get_var("space"))
    print(runtime.get_var("wall"))
    print(runtime.get_var(","))
    print(runtime.get_var("count"))
    print(runtime.get_var("bottles"))
    print(runtime.get_var("newline"))
    print(runtime.get_var("take"))
    print(runtime.get_var("count"))
    print(runtime.get_var("bottles"))
    print(runtime.get_var("!"))
    runtime.set_var(runtime.get_var("count") - 1)
