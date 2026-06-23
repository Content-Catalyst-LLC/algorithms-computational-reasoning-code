# AI Code Review Notes

Fortran's lesson for AI-generated scientific code:

Abstraction must earn trust.

Ask:

- Does the generated code implement the intended formula?
- Are units, domains, and boundary conditions correct?
- Is the algorithm numerically stable enough for its purpose?
- Does performance scale for expected input sizes?
- Are assumptions documented?
- Are tests included?
- Can future maintainers understand it?
- Who remains responsible for results?

Generated code is not automatically reliable scientific code.
