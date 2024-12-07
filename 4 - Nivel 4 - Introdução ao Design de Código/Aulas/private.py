class MyClass:

    #Public Method
    def method_1(self):
        print("Method 1")
        self.__method_2()

    #Private Method
    def __method_2(self):
        print("Method 2")

obj = MyClass()
obj.method_1()


class BankAccount:

    def registry(self):
        print("Start process")
        self.__verify()
        self.__verifyng_data()
        self.__add_DB()

    def __verify(self):
        print("Verifying")

    def __verifyng_data(self):
        print("Verifying data")

    def __add_DB(self):
        print("Adding data to DB")	

clientAccount = BankAccount()
clientAccount.registry()
