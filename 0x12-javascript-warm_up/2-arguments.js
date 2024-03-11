#!/usr/bin/node
const argNum = process.argv.length;
if (argNum.length == 0)
{
	console.log('No argument');
}
else if (argNum.length == 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
