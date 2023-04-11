console.log("JAVASCRIPT");

/*
Linear search algorithmm
*/

function linearSearch(list, target) {
  for (let i = 0; i < list.length; i++) {
    if (list[i] === target) {
      return i;
    }
  }
  return -1;
}

function verify(index) {
  if (index !== -1) {
    console.log(`Target found at index: ${index}`);
  } else {
    console.log("Target not found in list.");
  }
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let result = linearSearch(numbers, 15);
verify(result);

result = linearSearch(numbers, 6);
verify(result);
