#!/usr/bin/node

const argument = process.argv;

if (argument.length === 2) {
  console.log(0);
} else {
  const args = argument
    .map(Number)
    .slice(2, argument.length) // start at 2 and ends and argument length number
    .sort((a, b) => a - b); // sort the array in ascending order

  console.log(args[args.length - 2]); // args.length - 2 pick the second last integer
}
