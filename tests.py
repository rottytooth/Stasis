import sys
import unittest
import runtime
from runtime import Variable, String
import varloader

class Test_tests(unittest.TestCase):

    def test_hello_floats(self):
        runtime.reset_store()

        input = varloader.build_input_array_floats([72, 101, 108, 111])
        #print(input)

        # holder cell
        esc = Variable("esc", float, 0)
        h = Variable("h", str, input[1])
        e = Variable("e", str, input[2])
        l = Variable("l", str, input[3])
        o = Variable("o", str, input[4])

        self.assertEqual(h.value, "H")
        self.assertEqual(e.value, "e")
        self.assertEqual(l.value, "l")
        self.assertEqual(o.value, "o")


    def test_hello_from_string(self):
        runtime.reset_store()

        input_set = varloader.build_input(["Hello, World!"])
        esc = Variable("esc",float, 0)
        h = String("h", input_set[1])

        self.assertEqual(h.string, "Hello, World!")


    def test_string_and_int(self):
        runtime.reset_store()

        input_set = varloader.build_input(["test", 5])
        esc = Variable("esc",float, 0)
        test = String("test", input_set[1])
        _5 = Variable("5", int, input_set[2])

        self.assertEqual(test.string, "test")
        self.assertEqual(_5.value, 5)


    def test_two_strings(self):
        runtime.reset_store()

        input_set = varloader.build_input(["test", " "])
        esc = Variable("esc",float, 0)
        test = String("test", input_set[1])
        space = String("r", input_set[2])

        self.assertEqual(test.string, "test")
        self.assertEqual(space.value, "r")

if __name__ == '__main__':
    unittest.main()
