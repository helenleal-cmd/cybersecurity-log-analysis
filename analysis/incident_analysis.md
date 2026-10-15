# Incident Analysis

## Summary

This analysis reviews SSH authentication logs from `server01` to identify suspicious login activity and distinguish it from legitimate administrative access.

## Key Findings

- Multiple failed SSH login attempts were detected from the IP address `203.0.113.45`.
- The source attempted authentication using different accounts, including `admin`, `root` and `test`.
- Additional failed attempts were observed from `198.51.100.23` using the `guest` account.
- A successful login for the user `helen` was recorded from `192.0.2.10`.
- After the successful login, the user executed the command `/usr/bin/apt update` using `sudo`.

## Suspicious Activity

The IP address `203.0.113.45` generated repeated authentication failures within a short period and attempted access using multiple usernames.

This pattern is consistent with a possible SSH brute-force or credential-guessing attempt.

### Indicators

- Source IP: `203.0.113.45`
- Target service: SSH
- Accounts tested: `admin`, `root`, `test`
- Event type: Failed authentication attempts
- Severity: Medium

## Legitimate Activity

The authentication from `192.0.2.10` was successful for the user `helen`.

Shortly afterward, the account executed:

`sudo /usr/bin/apt update`

Based only on the available logs, this activity appears consistent with legitimate system administration. Additional context would be required to confirm the user's identity and authorization.

## Recommended Actions

1. Review additional authentication logs for activity from `203.0.113.45`.
2. Temporarily block or monitor suspicious source IP addresses.
3. Disable direct SSH access for the root account.
4. Use SSH keys instead of password authentication where possible.
5. Implement rate limiting or tools such as Fail2ban.
6. Monitor successful logins that occur after repeated failed authentication attempts.
7. Enable centralized logging and alerting for repeated SSH failures.

## Conclusion

The logs contain evidence of suspicious SSH authentication attempts, particularly from `203.0.113.45`.

No successful authentication from the suspicious IP was identified in the provided sample. The successful login from `192.0.2.10` should be treated separately and validated through normal access-control procedures.
