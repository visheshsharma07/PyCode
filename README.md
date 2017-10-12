Simple piece of code to demostrate how retry functionality is implemented using backoff decorator.
A Flask service is created, which is consumed at the testing end.
When the connection times out the backoff decorator reinterates through the decorated function.
Only if the result is not acheived within the given iterations, the code will finally give an exception, other will give the desire result.
