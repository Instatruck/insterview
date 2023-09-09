# Changelog

## 

 * Refactored Environment constructor to use declaritive defaults.
 * Refactored some Exceptions as per Pep 8: No bare exceptions
 * Note: These are replaced with broad Exception which is a weak warning in PEP8, but
   I'm still new to the codebase so cant anticipate all possible Exception types
 * Removed get('key') or 'default' and replaced with get('key','default)
 * Refactored path join to ose os.path.join for OS agnosticism
 * Added script to gen docs from docstrings
 * Defered file int write return to ensure with block cleans up. Generally unnecessary, but
      can potentially be a problem with non standard pythons (jython, etc)
 * Folded comment to second line to coomply with PEP8
 * Converted this file to MarkDown
 * Stubbed out a full coverage suite of tests. (At this stage, just stubs)
 * Stored AWS response in _response, for testing purposes. Its ugly, but its an artefact of the design.
 * Added MD5 file hashing function to testcases to simplify file test ops
 * Refactored a few more string ops to use .format as per cody hygine standards
 