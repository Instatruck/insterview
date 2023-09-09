# Test response notes

 * I've done some very light refactoring on a few aspects to comply better with PEP8
 * However I've used undifferentiated Exceptions as I'm not entirely clear on the behavior of
   some library calls. Unfortunately the duck typing in python doesn't let those be easily inferred
   via static analysis
 * I've also turned some "blah" + value + "blah" string concatenations into .format() interpolations
   as I feel these are more readable and inline with current community best practices. Its a YMMV 
   refactoring though, many prefer the concatenations.
 * I've swapped a few instances of .get(value) or default to .get(value,default) , as this better uses
   get's capacities to perform an atomic read-or-default on a value
 * I've fixed some file path contructions to either use .joins() or interpolations, ideally I'd just use
   .joins(), but I feel in a couple of instances the interpolation is more readable.
 * I'm not a fan of using classes as simply a container for static methods, this use is better 
   served with pythons module system, however without knowing fully how calling scripts expect 
   the API contract to function, I've declined to perform any big structure refactors.
 * I've used PDOC to generate some simple docs. However, PDOC isn't really the best choice, as it doesnt
   seem to use the standard sphinx style paramater/return markups. However for the context of a simple one page
   script, sphinx is overkill for our purposes.
 * I stubbed out a full suite of tests, however I ommitted a couple (And left one intentionally failing as false)
   as they seem to require a functional AWS system, with a compliant config file and in the context given
   I dont think guessing what is in that file would contribute anything useful to a practical set of tests
 * Thus the test_mfa_serial test is unimplemented and set to assert fail, as I have incomplete information to test this.
 * I have used an MD5 hash based method to compare file contents with expected contents.
 * I was unsure of a particularly robust way to check that that the filename generated was correct without 
   either knowing the value in advance (which would imply knowing the end-users username) or more or less
   verbatim replicating the codes working. This however would mean the test is effectively a white-box instead 
   of a black-box test, and thats bad practice. Instead I simply just checked to see if the requested file name
   corresponded to an actual file on te filesystem
 * I used git-flow to structure the CVS workflow as I coded, this may or may not reflect in the git log.
 
 