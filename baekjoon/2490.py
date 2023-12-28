while True:
    try:
        result = input()
        bae_count = result.count('0')
        
        if(bae_count == 1):
            print('A')
        elif (bae_count == 2):
            print('B')
        elif (bae_count == 3):
            print('C')
        elif (bae_count == 4):
            print('D')
        else:
            print('E')
    except:
        break
