class Book:
    def __init__(self,title,author,isdn,copies):
        self.title=title
        self.author=author
        self.isdn=isdn
        self.copies=copies
    
    def add_book(self):
        lib.append(self)
    @staticmethod
    def remove_book(isdn):
        for i in lib:
            if i.isdn==isdn:
                lib.remove(i)
                print(f'{isdn} removed')
                return
        print(f'{isdn} not found')
    @staticmethod
    def findbook(isdn):
        for i in lib:
            if i.isdn==isdn:
                print(i.title,i.author,i.isdn,i.copies)
        print(f'{isdn} not found')


    @staticmethod
    def display():
        if lib:
           for i in lib:
               
               print(i.title,i.author,i.isdn,i.copies)
        else:
            print('empty')

lib=[]
while True:
    print('1. add book 2. remove book 3. find book 4. display 5.exit')
    option=int(input('enter option'))
    if option==1:
        title=input('enter title')
        author=input('enter author')
        isdn=int(input('enter isdn number'))
        copies=int(input('enter copies'))
        book=Book(title,author,isdn,copies)
        book.add_book()
    elif option==2:
        isdn=int(input('enter isdn of a book to delete'))
        Book.remove_book(isdn)
    elif option==3:
        isdn=int(input('enter isdn of a book to search'))
        Book.findbook(isdn)
    elif option==4:
        Book.display()
    else:
        break


       
    

