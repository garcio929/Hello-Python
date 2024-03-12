# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")#Esta es la mejor por que vemos los datos donde van y donde los queremos poner

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = 'Hola'
stringOtro = 'adios'

print(string + ' ' +  stringOtro)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
#Print the variable company using print().
codingString = 'Coding'
forString = 'For'
allString = 'All'

todojunto = codingString + forString + allString
print (todojunto)

#Print the length of the company string using len() method and print().
print (len(todojunto))
#Change all the characters to uppercase letters using upper() method.
#Change all the characters to lowercase letters using lower() method.
print (todojunto.upper())
print (todojunto.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
ejercicio = 'Coding For All'
print (ejercicio.capitalize()) #Te pone la primera en mayuscula
print (ejercicio.title())
print (ejercicio.swapcase())
#Cut(slice) out the first word of Coding For All string.
cortando = ejercicio[1:]
print(cortando)
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(ejercicio.find('Coding'))
#Replace the word coding in the string 'Coding For All' to Python.
ejercicio = 'Python'
print(ejercicio)
#Change Python for Everyone to Python for All using the replace method or other methods.
print(ejercicio.replace('Python', 'cambiado'))
#Split the string 'Coding For All' using space as the separator (split())
ejercicio = 'Coding For All'
print(ejercicio.split(''))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
ejercicio = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(ejercicio.split(', '))
#What is the character at index 0 in the string Coding For All.
ejercicio = 'Coding For All'
print (ejercicio[0])
#What is the last index of the string Coding For All.
ejercicio = 'Coding For All'
print (ejercicio[-1])
#What character is at index 10 in "Coding For All" string.
print (ejercicio[10])
#Use index to determine the position of the first occurrence of C in Coding For All.
print (ejercicio.index('C',0))
#Use index to determine the position of the first occurrence of F in Coding For All.
print (ejercicio.index('F',0))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
ejercicio = 'Coding For All People'
print (ejercicio.rfind('l'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
ejercicio = 'You cannot end a sentence with because because because is a conjunction'
print (ejercicio.find('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
ejercicio = 'You cannot end a sentence with because because because is a conjunction'
print (ejercicio.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
ejercicio = 'You cannot end a sentence with because because because is a conjunction'
print(ejercicio.replace('because ', ''))
#Does ''Coding For All' start with a substring Coding?
ejercicio = 'Coding For All'
print(ejercicio.startswith('Coding'))
#Does 'Coding For All' end with a substring coding?
print(ejercicio.endswith('Coding'))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
print(ejercicio [1:])
"""Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python"""
ejercicio = '30DaysOfPython'
ejercicio2 = 'thirty_days_of_python'
print(ejercicio.isidentifier)
print(ejercicio2.isidentifier)
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
ejercicio = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = ' '.join(ejercicio)
print(resultado)



