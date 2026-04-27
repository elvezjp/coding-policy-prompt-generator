# Security Policy

[English](./SECURITY.md) | [日本語](./SECURITY_ja.md)

This document describes the security policy for coding-policy-prompt-generator.

## Supported Versions

The following versions are eligible for security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| 0.1.x   | :x:                |
| < 0.1   | :x:                |

We recommend always using the latest release.

## Reporting a Vulnerability

**Please do not open a public issue for security vulnerabilities.**

### How to Report

Please report security vulnerabilities through one of the following channels:

1. **GitHub Security Advisory** (recommended)
   - Use the [GitHub private security advisory feature](https://github.com/elvezjp/coding-policy-prompt-generator/security/advisories/new).

2. **Email**
   - To: info@elvez.co.jp
   - Subject: `[SECURITY] coding-policy-prompt-generator vulnerability report`

### Information to Include

Please include the following details in your report:

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact and severity
- Suggested fix or mitigation (if any)
- Contact information (optional)

### Example Report

```
Subject: [SECURITY] Arbitrary file read vulnerability

Description:
The input-file handler is vulnerable to path traversal,
allowing arbitrary files to be read.

Steps to reproduce:
1. Create an Excel file containing "../../../etc/passwd" in a path field.
2. Run: uv run coding-policy-prompt-generator malicious.xlsx
3. Observe that file contents are exposed in the output.

Impact:
A crafted Excel file could allow an attacker to read sensitive
files on the system.

Severity: High

Suggested fix:
Validate and sanitize file paths before processing.
```

## Response Timeline

- **Initial response**: within 48 hours
- **Status updates**: within 7 days
- **Resolution**: depending on severity
  - Critical: within 14 days
  - High: within 30 days
  - Medium: within 60 days
  - Low: in the next release cycle

## Security Considerations

### File Handling

- Process Excel files (.xlsx) only from trusted sources
- VBA macros (.xlsm) are not executed
- File paths are validated to prevent path traversal

### Input Validation

- User-supplied column names are sanitized
- Sheet names are validated against Excel constraints (31-character limit, forbidden characters)
- Header comparisons use NFC normalization

### Output Security

- Generated prompts and hyperlinks are stored as plain text
- Do not include sensitive data in the rule list
- Output files inherit the security context of the input

### Dependency Security

- Dependencies are managed by `uv` and `pyproject.toml`
- Vulnerable dependencies are monitored via Dependabot
- Security updates are applied promptly

## Security Best Practices

When using this tool, we recommend:

1. **Use the latest version** — keep up to date with the most recent release
2. **Verify input files** — only process Excel files from trusted sources
3. **Review generated output** — review output before sharing it externally
4. **Use a sandbox** — run on isolated environments for untrusted input
5. **Monitor dependencies** — keep dependencies up to date

## Known Security Limitations

- This tool processes user-supplied Excel files; malformed files may cause unexpected behavior
- Generated prompts may include sensitive rule information; handle output appropriately
- Template files (Jinja2) from untrusted sources may execute arbitrary code

## Contact

For non-vulnerability security questions:

- Open an issue with the `security` label
- Email: info@elvez.co.jp

## Acknowledgements

We thank the security researchers who help improve the security of this project. With permission, we will credit anyone who reports a valid security issue here.
