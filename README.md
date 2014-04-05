# Knotch: Kye's Number to Text Changer
*Turn literally* any *integer into English... the right way!*

Inspired by [Project Euler's problem 17](https://projecteuler.net/problem=17), I decided to make a script that quickly converts *any* integer into English. Unlike other projects of the kind, this module *fully complies* with standards of British usage (including [placement of the word "and"](http://english.stackexchange.com/questions/111765/how-to-write-out-numbers-in-compliance-with-british-usage) and hyphens ("twenty-three")) and can truly support numbers up to infinity (or as much as Python can handle) by generating words on-the-fly using the [Conway-Wechsler system](http://www.mrob.com/pub/math/largenum.html#conway-wechsler) of large numbers.

---

# Usage
Usage cannot be more simple - **knotch** is accessible from both the command line (UNIX shell) and inside your own Python 3 program. (Sorry for Python 2 - for that, I recommend checking out [sneilan's BigNumberNames](https://github.com/sneilan/BigNumberNames))

From the command line:

	$ knotch -123
	$ knotch 31415926
	$ knotch 271828182845904523536

From Python 3:

	>>> import knotch
	>>> knotch.knot(-123)
	'negative one hundred and twenty-three'
	>>> knotch.knot(31415926)
	'thirty-one million, four hundred and fifteen thousand, nine hundred and twenty-six'
	>>> knotch.knot(271828182845904523536)
	'two hundred and seventy-one quintillion, eight hundred and twenty-eight quadrillion, one hundred and eighty-two trillion, eight hundred and forty-five billion, nine hundred and four million, five hundred and twenty-three thousand, five hundred and thirty-six'

---

# References
- [Sean Neilan's BigNumberNames](https://github.com/sneilan/BigNumberNames), used to validate & check my outputs
- [Wikipedia page on large numbers](http://en.wikipedia.org/wiki/Names_of_large_numbers)
- [Project Euler #17](https://projecteuler.net/problem=17)
- [Robert Munafo's page on the Conway-Wechsler system](http://www.mrob.com/pub/math/largenum.html#conway-wechsler)
