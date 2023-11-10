//Return the number of vowels in a string

function vowelsCount(vowStr) {
    let vowels = 'aeiou'
    let count = 0;

  for(let i = 0; i< vowStr.length; i++) {

      if(vowels.includes(vowStr[i])){
          
          count++;
      }
         
  }
   return count

}

const vowelsCountString = 'Return the number of vowels in a string'

console.log('The number of vowels in this string is ' + vowelsCount(vowelsCountString));
