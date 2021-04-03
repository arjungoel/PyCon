Python is not an interpreted language rather it is a compiled language. Before any python code can be executed it first needs to be turned into bytecode and when you write a function, when you define a function that functionis compiled in the bytecode which are then executed.

Returning `None` from a generator function returns a `StopIteration` exception.

**Generator**:

- It implements Python's "iterator" protocol:
    * You get its iterator via "iter" (which is itself)
    * You get each succeeding value with "next"
    * When it gets to the end, it raises "StopIteration"


- In Python, we don't have indexes.

- `next` runs up to and includes the next `yield` statement.


**"next" and generators**:

- "next" tells a generator to run through the next "yield" statement.
- this can be a lot of code, or a tiny bit of code.
- upon hitting "yield", the generator returns the value and goes to sleep.
- the function's state remains across those cells.

**When should we use generators?**

- If we have a potentially large(or infinite) set of values to return.
- Often generators are used because it's easier to express the idea as a function.
- We have to set things up like a `network connection` or `file` and then we want to just keep that state going in our generator and it will stay across our different iterations.


When we use `yield` as an **expression** meaning on the right side of assignment:

- The rules for generators still apply
    * each call to `next` runs the generator through the next `yield`.
    * After `yield` it goes to sleep.

- But now `yield` can be used for two-way communication, now we can inject a value into our function by every time it yields to us then waits to get something from us we can send it a message and that received value replaces yield in the expression and then is assigned to whatever is on the left-hand side 


**How we send a message into our generator?**

By using the `send` method:

- We can advance a generator with the `next` function: `next(g)`
- We can send a value to a generator using the `send` method: `g.send(123)`
- Note: A call to `next(g)` is the same as `g.send(None)`


`Priming` is running through the first yield statement.


**Coroutine**:

A `coroutine` is:

- A generator
- It waits to get input from elsewhere using "send"
- The data is received with "yield" as an expression (typically on the right side of an assigment)
- Local state remains across calls


**  How can I use coroutines?**


**How can I tell the generator that I am completely done?**

- use the **`close`** method. This exits from the generator without raising a **`StopIteration`** exception. If you try to use the generator after closing it, you'll get a StopIteration exception.


**"throw" method**:

- We can raise an exception in a generator using "throw" and this will raise an exception of our choice (custom exception) inside of the generator.


**`yield from`** is a keyword that has been introduced in python 3.3

- It isn't running a "for" loop on the generator.
    * We don't need a new keyword (as of 3.3) for that.

- "yield from" provides bidirectional communication with a coroutine.
    * Sending to the outer is passed to the inner.
    * Data yielded by the inner is passed to the outer.
    * Exceptions raised via "throw" work.
    * We can close the inner one via "close".

- In other words: **`yield from`** is made for sub-routines.



