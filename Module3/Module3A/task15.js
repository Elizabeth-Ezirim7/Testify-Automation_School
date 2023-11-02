

const books = [
    
    {
        title: 'Java',
        description: 'Beginners class in Java',
        numberOfPages: 30,
        author: 'Elizabeth Ezirim',
        reading: true
    },

    {
        title: 'Selenium',
        description: 'Beginners class in Selenium',
        numberOfPages: 70,
        author: 'Olamide Oluwole',
        reading: true
    },

    {
        title: 'Appium',
        description: 'Beginners class in Appium',
        numberOfPages: 100,
        author: 'Princess Ronke',
        reading: false
    },
    {
        title: 'Maven',
        description: 'Beginners class in Maven',
        numberOfPages: 100,
        author: 'MaryBlossom Onyeka',
        reading: true
    },

    {
        title: 'Software testing',
        description: 'Intro to Software testing',
        numberOfPages: 100,
        author: 'Kehinde Odunuga ',
        reading: false
    }


];


//Using For loop to log book information

for (let i = 0; i < books.length; i++) {
    if (books[i].reading === true) { //Strong equality check
        console.log("Title: " + books[i].title); //Logs Title
        console.log('Description: '+ books[i].description); //Logs Description
        console.log("Number of Pages: " + books[i].numberOfPages); //Logs Number of pages
        console.log("Author: " + books[i].author); //Logs Author
        console.log("") //A blank line to seperate each book information for readability sake
        
    }
} 

  
    

