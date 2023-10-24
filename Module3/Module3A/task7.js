//Different sides of a triangle

const side1 = 3;
const side2 = 4;
const side3 = 5;

if(side1 === side2 && side2 === side3 ){
    console.log("Equilateral Triangle");
}
else if (side1 === side2 || side1 === side3 || side2 === side3){
    console.log('Isoceles Triangle')
} 
else{
    console.log('Scalene Triangle')
}
