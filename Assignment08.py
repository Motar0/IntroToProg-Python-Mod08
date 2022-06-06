# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Dustin Holland,6/3/22,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Dustin Holland,06/03/22,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
    def __init__(self, product_name:str, product_price: float):
        self.product_name = (product_name)
        self.product_price = (product_price)

        # Product Name
        def product_name(self):
            return str(self.__product_name).title()


        def product_name(self, value):
            if not str(value).isnumeric():
                self.__product_name = value
            else:
                raise Exception("Names cannot be numbers")

        # Product Price
        def product_price(self):  # (getter or accessor)
            return float(self.__product_price)


        def product_price(self, value):
            try:
                self.__product_price = float(value)
            except:
                raise Exception('Prices cannot be letters')

        # -- Methods --
        def __str__(self):
            return self.product_name + ' | ' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Dustin Holland,06/03/22,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file (Save Data)
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Writes data from a list of dictionary rows to a File
        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            file_obj = open(file_name, "w")
            for row in list_of_product_objects:
                file_obj.write(row.__str__() + "\n")
            file_obj.close()
            print("Data Saved!")
        except Exception as e:
            print('Non-specific error.')
            print('Built-In Python error info: ')


        #  TODO: Add Code to process data to a file (read data)
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :return: (list) of rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                product_and_price = line.split(" | ")
                row = Product(product_and_price[0], (product_and_price[1]))
                list_of_rows.append(row)
            file.close()
        except FileNotFoundError:
            print("Error. The file does not exist.")
        except Exception as e:
            print('Non-specific error.')
            print('Built-In Python error info: ')

        return list_of_rows

    @staticmethod
    def remove_data_from_list(product_to_remove, list_of_rows):
        """ Removes data from a list of dictionary rows
        :param product: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        for product in list_of_rows:
            if product.product_name.lower() == product_to_remove.lower():
                list_of_rows.remove(product)
        return list_of_rows



# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ Performs Input and Output tasks """
    pass
    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('----------Product and Price List----------')
        print('''
              Menu of Options
              1) Show current Products
              2) Add a new Product
              3) Remove an existing Product
              4) Save Data to File        
              5) Exit Program
              ''')
        print()  # Add an extra line for looks
    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Products in the list of rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* Your current products are: *******")
        for row in list_of_rows:
            print(row.product_name + " | " + str(row.product_price))  # convert price to str or concatenate error
        print()  # Add an extra line for looks
    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """  Gets product and price values to be added to the list
        :return: (string, string) with product and price
        """
        try:
            product = str(input("Please enter a product: "))
            price = int(input("Please enter its price: "))
            product_and_price = Product(product_name=product, product_price=price)
            return product_and_price

        except Exception as e:
            raise (e)
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
while (True):
    try:
        # Step 3 Show current data
        IO.output_menu_tasks()  # Shows menu


    # Get user's menu option choice
        choice_str = IO.input_menu_choice()  # Get menu option

    # Show user current data in the list of product objects
        if choice_str.strip() == '1':   # Show current products
            IO.output_current_tasks_in_list(lstOfProductObjects)
            continue

    # Let user add data to the list of product objects
        elif choice_str.strip() == '2':  # Add a new product
            lstOfProductObjects.append(IO.input_new_product_and_price())
            continue  # to show the menu

    # Let user remove data from the list of product objects
        elif choice_str.strip() == '3': # Remove a product
            product = IO.input_product_to_remove()
            lstOfProductObjects = FileProcessor.remove_data_from_list(product_to_remove=product, list_of_rows=lstOfProductObjects)

    # let user save current data to file
        elif choice_str == '4':  # Save Data to File
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue  # to show the menu

    # Let user exit
        elif choice_str == '5':  # Exit Program
            print("Goodbye!")
            break  # exiting loop

    except Exception as e:
        print('Non-specific error.')
        print('Built-In Python error info: ')


# Main Body of Script  ---------------------------------------------------- #

