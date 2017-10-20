import sys
import unittest
import runtime
import varloader

class Test_tests(unittest.TestCase):

    def test_hello_floats(self):
        runtime.reset_store()

        input = varloader.build_input_array_floats([72, 101, 108, 111])
        #print(input)

        # holder cell
        runtime.set_var("esc",input[0])

        runtime.set_var("h",input[1], str)
        runtime.set_var("e",input[2], str)
        runtime.set_var("l",input[3], str)
        runtime.set_var("o",input[4], str)

        self.assertEqual(runtime.get_var("h"), "H")
        self.assertEqual(runtime.get_var("e"), "e")
        self.assertEqual(runtime.get_var("l"), "l")
        self.assertEqual(runtime.get_var("o"), "o")


    def test_hello_from_string(self):
        runtime.reset_store()

        input_set = varloader.build_input(["Hello, World!"])
        runtime.set_var("esc", 0)
        runtime.set_var("h", input_set[1], str)
        self.assertEqual(runtime.get_var("h"), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
