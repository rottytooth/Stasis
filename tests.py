import sys
import unittest
import interpreter
import runtime

class Test_tests(unittest.TestCase):

    def test_hello_floats(self):
        input = interpreter.build_input_array_floats([72, 101, 108, 111])
        #print(input)

        # holder cell
        runtime.set_var("esc",input[0])

        runtime.set_var("H",input[1], str)
        runtime.set_var("e",input[2], str)
        runtime.set_var("l",input[3], str)
        runtime.set_var("o",input[4], str)

        #sys.stdout.write(runtime.get_var("H"))
        #sys.stdout.write(runtime.get_var("e"))
        #sys.stdout.write(runtime.get_var("l"))
        #sys.stdout.write(runtime.get_var("l"))
        #sys.stdout.write(runtime.get_var("o"))

        self.assertEqual(runtime.get_var("H"), "H")
        self.assertEqual(runtime.get_var("e"), "e")
        self.assertEqual(runtime.get_var("l"), "l")
        self.assertEqual(runtime.get_var("o"), "o")


    def test_hello_from_string(self):
        input_set = interpreter.build_input([0, "Hello"])
        runtime.set_var("esc", 0)
        runtime.set_var("h", input_set[1], str)
        self.assertEqual(runtime.get_var("h"), "Hello")

if __name__ == '__main__':
    unittest.main()
