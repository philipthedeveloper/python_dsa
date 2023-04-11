console.log("JAVASCRIPT");

function recursiveBinarySearch(list, target) {
  if (list.length === 0) {
    return false;
  } else {
    let midpoint = Math.floor(list.length / 2);
    if (list[midpoint] === target) {
      return true;
    } else {
      if (list[midpoint] < target) {
        return recursiveBinarySearch(list.slice(midpoint + 1), target);
      } else {
        return recursiveBinarySearch(list.slice(0, midpoint), target);
      }
    }
  }
}

function verify(result) {
  console.log(`Target found: ${result}`);
}

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8];

result = recursiveBinarySearch(numbers, 8);
verify(result);
