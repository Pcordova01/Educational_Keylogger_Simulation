# MITRE ATT&CK - Ethical Keylogger Simulation
Inspired By: [CISA Best Practices for MITRE ATT&CK Mapping (2023)](https://www.cisa.gov/sites/default/files/2023-01/Best%20Practices%20for%20MITRE%20ATTCK%20Mapping.pdf)

**This project is intended for educational and ethical purposes only!!** 

## What is MITRE ATT&CK?

MITRE ATT&CK is a popular framework that documents the tactics and techniques that real-world cyber advasaries use to initiate attacks. The idea is to give cybersecurity professionals tools to enhance their threat intelligence to improve their strategies of mitigating attacks.  

## ATT&CK Technique Mapping

| Technique       |  ID | Name                                | Use                                                                  | Recommendation                                                                 |
|--------------|--------------|-------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Collection   | [T1056.001](https://attack.mitre.org/techniques/T1056/001/) | Input Capture: Keylogging                | Logs every keystroke using `pynput`, simulating how adversaries steal credentials | Monitor for suspicious keylogging behavior using EDR, disable unnecessary scripting tools |
| Exfiltration | [T1041](https://attack.mitre.org/techniques/T1041/)         | Exfiltration Over C2 Channel             | Sends captured data via Gmail SMTP with TLS encryption, simulating covert data transfer | Monitor for unusual outbound SMTP traffic or frequent small email sends |

## Resources Used

- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1056.001: Input Capture - Keylogging](https://attack.mitre.org/techniques/T1056/001/)
- [T1041: Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041/)
- [CISA Best Practices for MITRE ATT&CK Mapping (2023)](https://www.cisa.gov/sites/default/files/2023-01/Best%20Practices%20for%20MITRE%20ATTCK%20Mapping.pdf)
