//My Personal Library 2

const books = {
    title : 'JavaScript',
    description :  'Intoductiion to JavaScript ',
    numberOfPages: 50,
    authour: 'Elizabeth',
    reading: false,
    toggleReadingStatus: function(){
        if(books.reading===true){
            books.reading = false;
        }
        else{
            books.reading = true;
        }

    }

    
}


books.toggleReadingStatus()

console.log('It is '+ books.reading + ' that Elizabeth is reading')


