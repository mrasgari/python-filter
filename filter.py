# write bad persian word in sub list for Ethical reasons i cant write here 
bad_words=[
'بد',
'زشت',
'...']

#filter bas word in text and replace with ****
def filter_bad_persian_word(text):
    
    for word in bad_words:
        text=text.replace(word,'***')
    
    return text 

#check if text have bad word or not
def check_bad_persian_word(text):
    for word in bad_words:
        if word in text:
            return False

    return True    