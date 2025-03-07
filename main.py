def get_bool_and_convert():
    while True:
        user_input = input("Lütfen bir boolean değer girin (1=True, 0=False): ")
        if user_input == "1":
            bool_value = True
            break
        elif user_input == "0":
            bool_value = False
            break
        else:
            print("Lütfen sadece '1' veya '0' girin!")
    
    # Boolean'ı string'e çevirme
    string_value = str(bool_value)
    
    # Sadece string karşılığını gösterme
    print(f"String karşılığı: {string_value}")

if __name__ == "__main__":
    get_bool_and_convert()
