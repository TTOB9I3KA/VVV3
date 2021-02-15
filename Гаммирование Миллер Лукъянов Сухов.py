print("Выбирете действие: Зашифровать - 1 , Дешифровать - 2 ")
u=int(input())
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',' ']
text = list(input("Введите строку, которую хотели бы зашфровать используя только буквы нижнего регистра русского алфавита:  "))
a = 7
m = 34
Y = [0] * len(text)
Y[0] = 32
for i in range(1, (len(text))):
   Y[i] = (a * Y[i - 1]) % m
print('Гамма: ',Y)
lst = []
i = 0
for i in range(len(text)):
    lst.append(alphabet.index(text[i]))

if u == 1:
 crypt = []
 for i in range(len(text)):
    x = (lst[i] + Y[i]) % 34
    crypt.append(x)

 gotovo = []
 i = 0
 for i in range(len(crypt)):
    z = crypt[i]
    gotovo.append(alphabet[z])
 print('Зашифрованный текст: ',"".join(gotovo))
if u == 2:

     crypt = []

     for i in range(len(text)):
         x = (lst[i] - Y[i] + 34) % 34
         crypt.append(x)


     gotovo = []
     i = 0
     for i in range(len(crypt)):
         z = crypt[i]
         gotovo.append(alphabet[z])
     print('Расшифрованный текст: ',"".join(gotovo))

