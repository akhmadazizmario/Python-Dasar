num = 0
last_pos = 0
post_request = 1111

while True:
    num += 1
    str_num = str(num)
    last_pos += len(str_num)
    print(str_num, last_pos)
    if last_pos >= post_request :
        break
    
print()