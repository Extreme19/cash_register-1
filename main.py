from time import ctime
def get_int_input(prompt):
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value

        except KeyboardInterrupt:
            exit()

        except ValueError as e:
            print("inValid input")
            print(e, File=ERROR_FILE)
            print(ctime(), e, file = ERROR_FILE)

def main():
    while True:
        client_name = input('what is the customer\'s name:')
        if not client_name:
            break

        while True:
            product_name = input('what is the product name?:')
            if not product_name:
                break

            
            product_qty = get_int_input(f'How many {product_name} purchase?:')
        
            producr_price = input(f"How much is {product_name}?:")

    

if __name__ == '__main__':

    #SUPREGOBALS

    ERROR_FILE = open('error_log.text', 'a')


    main()

    ERROR_FILE.close()
    
        