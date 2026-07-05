#Valid Palindrome (ignoring non-alphanumeric) 

def is_valid_pal(s):
    sanitized_text = ''.join(i.lower() for i in s if i.isalnum())
    
    start = 0
    end = len(sanitized_text) - 1 
    print(sanitized_text)
    while start < end:
        if sanitized_text[start] != sanitized_text[end]:
            return False
        start += 1
        end -= 1
    
    return True

sentence = "A man, a plan, a canal: Panama"
is_valid_pal(sentence)