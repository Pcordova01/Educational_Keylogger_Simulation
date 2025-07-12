# MITRE ATT&CK Mapping – Python Keylogger Simulation

This project simulates adversary behavior for educational and ethical purposes, focusing on data collection and exfiltration tactics. The table below maps the behavior of the keylogger to known techniques in the MITRE ATT&CK framework.

| **Tactic**       | **Technique ID** | **Technique Name**               | **Description**                                                                 |
|------------------|------------------|----------------------------------|---------------------------------------------------------------------------------|
| Collection        | T1056.001         | Keylogging                       | Captures keyboard input using Python’s `pynput` to simulate input collection.   |
| Exfiltration      | T1041             | Exfiltration Over C2 Channel     | Sends keystroke logs via encrypted Gmail SMTP connection (TLS) every 10 keys.  |

---

### Notes

- These mappings are based on how adversaries operate in red team/penetration test scenarios.
- This simulation was created for ethical research and security awareness training.
- Real-world attackers may use additional methods for stealth, persistence, and lateral movement.

---

### References

- [MITRE ATT&CK - T1056.001](https://attack.mitre.org/techniques/T1056/001/)
- [MITRE ATT&CK - T1041](https://attack.mitre.org/techniques/T1041/)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
