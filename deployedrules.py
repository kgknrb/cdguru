def avoid_complex_comprehension_non_compliant_1():
    text = [['bar', 'foo', 'fooba'], ['Rome', 'Madrid', 'Houston'], ['aa', 'bb', 'cc', 'dd']]
    text_3 = [y.upper() for x in text if len(x) == 3 for y in x if y.startswith('f')]


def avoid_complex_comprehension_non_compliant_2():
    text = [['bar', 'foo', 'fooba'], ['Rome', 'Madrid', 'Houston'], ['aa', 'bb', 'cc', 'dd']]
    text_3 = [z.upper() for x in text if len(x) == 3 for y in x for z in y]


def nonconformant_string_join_efficient_concentation():
    mylist = ['first', 'second', 'third', 'other']
    result = ''
    for item in mylist:
        result += item + "\n"
    return result


def non_conformant_variable_initialized_within_loop_efficient_concentation():
    mylist = ['first', 'second', 'third', 'other']
    s = ""
    for item in mylist:
        s += "Hello World" + item
        print(s)


def nonconformant_list2_unnecessary_iteration():
    input_list = set([10, "USA", 20, "RSA"])
    x = 0
    while x < len(input_list):
        y = input_list[x]
        if y == 20:
            print("found country code")
        x += 1


def nonconformant_list3_unnecessary_iteration():
    input_list = set([10, "USA", 20, "RSA"])
    for x in range(len(input_list)):
        y = input_list[x]
        if y == 10:
            print("item found")


def non_conformant_case1_socket_connection_timed_out():
    import socket
    s = socket.socket()
    s.connect(('127.0.0.1', 9000))
    print(s.recv(1024))
    s.close()


def non_conformant_case2_socket_connection_timed_out():
    import socket
    s = socket.create_connection(('127.0.0.1', 9000))
    print(s.recv(1024))
    s.close()


class Animals:
    def __init__(self):
        self.lion = 'carnivore'
        self.dog = 'omnivore'
        self.giraffe = 'herbivore'

    def printit(self):
        print("Dictionary from the object fields\
        belonging to the class Animals:")


def nonconformant_case3_do_not_directly_modify_dict():
    # object animal of class Animals
    animal = Animals()

    # calling printit method
    animal.printit()
    animal.__dict__['lion'] = 'omnivore'


def error_prone_multidimensional_list_non_conformant1():
    multi_dim_list = [[None] * 2] * 3


def error_prone_multidimensional_list_non_conformant2():
    multi_dim_list = [[[1] * 2] * 2]


def error_prone_multidimensional_list_non_conformant3():
    multi_dim_list = [[[[7.55] * 2] * 2]] * 3


def nonconformant_case1_subprocess_communicate_timeout_expires_rule():
    import subprocess
    proc = subprocess.Popen("ls -al", shell=True, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        print("Timed out")


class BaseSSLError(BaseException):
    pass
# guru:v1:internal:pythonbestpractices:avoid_complex_comprehension:1.0
# guru:v1:internal:pythonbestpractices:efficient_concatenation_of_immutable_objects_rule:1.0
# guru:v1:internal:pythonbestpractices:unnecessary_iteration_rule:1.0
# guru:v1:internal:pythonbestpractices:create_custom_exception_from_exception_class_rule:1.0
# guru:v1:internal:pythonbestpractices:do_not_directly_modify_dict:1.0
# guru:v1:internal:pythonbestpractices:socket_connection_timeout_rule:1.0
# guru:v1:internal:pythonbestpractices:error_prone_multidimensional_list_init
# guru:v1:internal:pythonbestpractices:subprocess_communicate_timeout_expires_rule:2.0
