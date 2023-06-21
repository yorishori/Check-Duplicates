import unidecode as u
                 

#Main Function
def matchString(firstString:str, secondString:str) -> bool:
    # The obvious first
    if(firstString==secondString):
        return True
    
    # Format Strings
    str1 = u.unidecode(firstString.casefold())
    str2 = u.unidecode(secondString.casefold())

    if (str1 in str2) or (str2 in str1):
        return True
    
    return False
