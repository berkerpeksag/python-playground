* The body begins with a base case, a conditional statement that defines the
  behavior of the function for the inputs that are simplest to process.
* Some recursive functions will have multiple base cases.
* The base cases are then followed by one or more recursive calls. Recursive
  calls always have a certain character: they simplify the original problem.
* Recursive functions express computation by simplifying problems
  incrementally. For example, summing the digits of 7 is simpler than summing
  the digits of 73, which in turn is simpler than summing the digits of 738.
  For each subsequent call, there is less work left to be done.
* A recursive implementation of factorial can express `fact(n)` in terms of
  `fact(n-1)`, a simpler problem. The base case of the recursion is the
  simplest form of the problem: `fact(1)` is 1.
* The iterative function constructs the result from the base case of 1 to the
  final total by successively multiplying in each term. The recursive function,
  on the other hand, constructs the result directly from the final term, `n`,
  and the result of the simpler problem, `fact(n-1)`.
* As the recursion "unwinds" through successive applications of the fact
  function to simpler and simpler problem instances, the result is eventually
  built starting from the base case. The recursion ends by passing the argument
  1 to `fact`; the result of each call depends on the next until the base case
  is reached.
* While we can unwind the recursion using our model of computation, it is often
  clearer to think about recursive calls as functional abstractions. That is,
  we should not care about how `fact(n-1)` is implemented in the body of fact;
  we should simply trust that it computes the factorial of `n-1`. Treating
  a recursive call as a functional abstraction has been called a recursive leap
  of faith. We define a function in terms of itself, but simply trust that the
  simpler cases will work correctly when verifying the correctness of the
  function.
* In general, iterative functions must maintain some local state that changes
  throughout the course of computation. At any point in the iteration, that
  state characterizes the result of completed work and the amount of work
  remaining.
