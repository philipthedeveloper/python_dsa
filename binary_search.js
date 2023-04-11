console.log("JAVASCRIPT")

function binarySearch(list, target){
  let first = 0
  let last = list.length - 1

  while(first <= last) {
    let midpoint = Math.floor((first + last) / 2)
    if(list[midpoint] === target) {
      return midpoint
    } else if(list[midpoint] < target) {
      first = midpoint + 1
    } else {
      last = midpoint - 1
    } 
  }
  console.log('Done with loop')
  return undefined
}


function verify(index) {
  if (index !== undefined) {
    console.log(`Target found at index: ${index}`);
  } else {
    console.log("Target not found in list.");
  }
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binarySearch(numbers, 1)
verify(result)
