# Security Policy

This document describes the security policy for coding-policy-prompt-generator.

## Supported Versions

The following versions are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

We recommend always using the latest version.

## Reporting a Vulnerability

**Please do not create a public Issue for security vulnerabilities.**

### How to Report

Please report security vulnerabilities using one of the following methods:

1. **GitHub Security Advisory** (Recommended)
   - Use [GitHub's private security advisory feature](https://github.com/elvez-inc/coding-policy-prompt-generator/security/advisories/new)

2. **Email**
   - Send to: info@elvez.co.jp
   - Subject: `[SECURITY] coding-policy-prompt-generator vulnerability report`

### Information to Include

Please include the following information in your report:

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact and severity
- Suggested fix or mitigation (if available)
- Your contact information (optional)

### Report Example

```
Subject: [SECURITY] Arbitrary file read vulnerability

Description:
A path traversal vulnerability exists in the input file processing that allows reading arbitrary files.

Steps to Reproduce:
1. Create an Excel file containing "../../../etc/passwd" in the path field
2. Run: uv run coding-policy-prompt-generator malicious.xlsx
3. Observe that the file contents are exposed in the output

Impact:
An attacker could read sensitive files on the system through crafted Excel files.

Severity: High

Suggested Fix:
Validate and sanitize file paths before processing.
```

## Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Resolution**: Based on severity
  - Critical: Within 14 days
  - High: Within 30 days
  - Medium: Within 60 days
  - Low: Next release cycle

## Security Considerations

### File Processing

- Only process Excel files (.xlsx) from trusted sources
- VBA macros (.xlsm) are not executed
- Validate file paths to prevent path traversal attacks

### Input Validation

- User-provided column names are sanitized
- Sheet names are validated against Excel constraints (31 characters, forbidden characters)
- Header comparisons use NFC normalization

### Output Security

- Generated prompts and hyperlinks are stored as plain text
- Do not include sensitive data in the rule index
- Output files inherit the security context of the input

### Dependency Security

- Dependencies are managed via `uv` and `pyproject.toml`
- We use Dependabot to monitor for vulnerable dependencies
- Security updates are applied promptly

## Security Best Practices

When using this tool, we recommend:

1. **Use the latest version** - Always update to the latest release
2. **Verify input files** - Only process Excel files from trusted sources
3. **Review generated output** - Check output before sharing externally
4. **Use sandboxed environments** - Run in isolated environments for untrusted inputs
5. **Monitor dependencies** - Keep dependencies up to date

## Known Security Limitations

- The tool processes user-provided Excel files; malformed files could cause unexpected behavior
- Generated prompts may contain sensitive rule information; handle output appropriately
- Template files (Jinja2) from untrusted sources could execute arbitrary code

## Contact

For security questions that are not vulnerabilities:

- Create an Issue with the `security` label
- Email: info@elvez.co.jp

## Acknowledgments

We appreciate security researchers who help improve the security of this project. Contributors who report valid security issues will be acknowledged here (with permission).
