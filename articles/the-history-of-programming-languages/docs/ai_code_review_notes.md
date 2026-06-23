# AI Code Review Notes

AI code generation adds a new layer to programming-language history.

Generated code still depends on:

- source language syntax;
- language semantics;
- runtime assumptions;
- compiler or interpreter behavior;
- libraries and dependencies;
- package versions;
- tests;
- documentation;
- security review;
- maintainability;
- human accountability.

Review generated code by asking:

- What language and ecosystem does it assume?
- Are dependencies safe and maintained?
- What tests cover behavior?
- Can humans read and maintain it?
- Does the generated code match the intended domain?
- What assumptions did the prompt leave unstated?
