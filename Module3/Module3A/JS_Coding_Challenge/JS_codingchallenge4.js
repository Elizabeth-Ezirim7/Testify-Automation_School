
//multiplication table

let rows = 12
let cols = 12

for (let i = 1; i <= rows; i++) {
      let row = i + '\t|\t';
      for (let j = 1; j <= cols; j++) {
        const result = i * j;
        row += result + '\t';
      }
      console.log(row);
    }


  


















  
  
