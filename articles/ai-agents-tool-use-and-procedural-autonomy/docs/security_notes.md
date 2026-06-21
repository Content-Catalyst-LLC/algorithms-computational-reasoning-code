# Security Notes

Common agentic AI security concerns include:

- prompt injection from retrieved documents or webpages;
- untrusted tool outputs being treated as instructions;
- excessive data access;
- hidden write actions;
- unsafe shell or code execution;
- credential exposure;
- context confusion across users or files;
- action loops and resource overuse.

Safer designs separate instructions from data, limit permissions, sandbox execution, log tool calls, and require human approval for consequential actions.
