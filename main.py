from time import ctime

def save_data(client_name, data):
    DATA.append(
        {
            'Customer_name': client_name, 
            'product': data,
            'time':ctime()
        }
    )

    DATA.append(data)

def end_program(data=None):
    if data is not None:
        save_data(client_name, data)

    print(DATA)
    exit()

def get_number_input(prompt):


    value = None



    while type(value) != float:
        try:
            value = float(input(prompt))
            return value

        except KeyboardInterrupt:
            exit()

        except ValueError as e:
            print("inValid input")
            print(ctime(), e, file=ERROR_FILE)



def main():
    while True:
        client_name = input('what is the customer\'s name:')
    

        if not client_name:
            print('Name must be provided')
            continue

        elif client_name == '-1':
            end_program();

        product_information = []

        while True:
            product_name = input('what is the product name?:')

            if not product_name:
                print('product name must be provided!')
                continue

            elif product_name == '-1':
                #end_program(client_name, data=product_information)
                save_data(client_name,product_information)
                break
            
            product_qty = get_number_input(f'How many {product_name} purchase?:')
            
            if product_qty == -1:
                #end_program(client_name, data=product_information)
                save_data(client_name,product_information)
                break
        
            product_price = get_number_input(f"How much is {product_name}?:")

            if product_price == -1:
                #end_program(client_name, data=product_information)
                save_data(client_name,product_information)
                break

            product_information.append(
                {
                    'product_name' :product_name,
                    'product_quantity' :product_qty,
                    'product_price' :product_price

                }
            )    


if __name__ == '__main__':

    #SUPREGOBALS

    ERROR_FILE = open('error_log.text', 'a')
    DATA = []

    main()

    ERROR_FILE.close()
    
        