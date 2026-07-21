## :blue[📋 Week 13: Administrative Controls]

Administrative controls focus on people and rules, guiding employee behavior to enhance security.

### :green[Administrative Controls Definition]

**:green[Definition:]** Security controls concerned with people and rules, such as policies, procedures, and training, to organize employee behavior safely.

-   **:orange[Role:]** Strengthen the "People" pillar of security. Also include governance and compliance.

### :violet[Four Key Administrative Controls]

1.  ### 📜 :green[Policy]
    -   **:green[Definition:]** A general rule that states what is required or not permitted (e.g., "All employees must use strong passwords").
    -   **Key Feature:** Sets the goal, but not the detailed "how."

2.  ### 📝 :green[Procedure]
    -   **:green[Definition:]** A detailed set of steps explaining *exactly how* a policy is to be carried out (e.g., "How to report a suspicious email: 1. Don't click, 2. Send to security, 3. Delete").
    -   **Key Feature:** Provides the method, ensuring consistent correct action.

3.  ### 🧑‍🏫 :green[Security Awareness Training]
    -   **:green[Definition:]** Instruction given to employees to help them recognize threats (like phishing) and respond correctly.
    -   **Key Feature:** Directly addresses human vulnerabilities, making employees the strongest defense. Most effective when continuous.

4.  ### 📏 :green[Standard]
    -   **:green[Definition:]** A specific and mandatory requirement that converts a general policy into a precise condition (e.g., a "strong password" *standard* might be "at least 12 characters, with numbers and symbols").
    -   **Key Feature:** Removes ambiguity from policies by setting exact requirements.

---

## :blue[💻 Technical Controls]

Technical controls are technological tools and programs that directly protect systems and data from attackers.

### :green[Technical Controls Definition]

**:green[Definition:]** Tools and programs that protect systems and data by technological means, standing directly in the path of an attacker.

### :violet[Five Key Technical Controls]

1.  ### 🧱 :green[Firewall]
    -   **Function:** Controls network connections, deciding which are permitted to pass into or out of a network and blocking suspicious ones.
    -   **Defends Against:** Harmful network connections.

2.  ### 🛡️ :green[Antivirus]
    -   **Function:** Detects and removes known malware (viruses, Trojans, spyware) from a device.
    -   **Defends Against:** Known malware and viruses.

3.  ### 💻 :green[EDR (Endpoint Detection and Response)]
    -   **Function:** An advanced system installed on endpoint devices (laptops, phones) that continuously monitors device behavior, detects unusual activity (even from unknown programs), and responds (e.g., isolates an infected device).
    -   **Defends Against:** New and unknown threats, active attacks.
    -   **:orange[Difference from Antivirus:]** EDR goes beyond simple detection/removal to continuous monitoring, investigation, and response.

4.  ### 🔑 :green[MFA (Multi-Factor Authentication)]
    -   **Function:** Requires a second proof of identity beyond a password (e.g., password + phone code or fingerprint).
    -   **Defends Against:** Stolen passwords, unauthorized account access.
    -   **:orange[Importance:]** Highly effective, even if a password is compromised, the second factor blocks entry.

5.  ### 📊 :green[SIEM (Security Information and Event Management)]
    -   **Function:** Collects security records and events from all devices and tools across an organization into one central place and analyzes them together.
    -   **Defends Against:** Hidden or coordinated attacks by linking seemingly unrelated events.
    -   **:orange[Role:]** Supports security analysts by providing a complete picture for investigation.

---

## :blue[🔒 Physical Controls]

Physical controls protect tangible assets and facilities, preventing unauthorized physical access to systems and data.

### :green[Physical Controls Definition]

**:green[Definition:]** Security controls that protect physical objects, facilities, and equipment.

-   **:orange[Why they matter:]** An attacker with physical access can bypass software defenses (e.g., stealing a server).

### :violet[Four Key Physical Controls]

1.  ### 👮 :green[Security Guards]
    -   **Role:** Human line of defense at entrances; they watch, question, and prevent entry of unauthorized or suspicious individuals.
    -   **Related Principle:** Prevention and real-time response.

2.  ### 📸 :green[CCTV (Closed-Circuit Television)]
    -   **Role:** Cameras that record activity for deterrence and to provide evidence if an incident occurs.
    -   **Related Principle:** **Accountability** (records who did what, when).

3.  ### 🔐 :green[Locks]
    -   **Role:** Devices that secure doors and sensitive rooms (e.g., server rooms), directly preventing physical access to valuable devices.
    -   **Related Principle:** **Confidentiality** (protects physical access to data).

4.  ### 🆔 :green[Access Badges]
    -   **Role:** Cards carried by employees that determine exactly where they are permitted to enter. They also record who entered which place and when.
    -   **Related Principles:** **Authorization** (controls who may enter where) and **Accountability** (records entries).

---

## :blue[⚙️ Control Functions]

Controls can also be classified by *what* they do and *when* they act relative to an attack.

### :green[Control Functions Definition]

**:green[Definition:]** A classification of controls based on their purpose and timing in relation to an attack (before, during, or after).

### :violet[Five Control Functions]

1.  ### 🚫 :green[Preventive Control]
    -   **Timing:** **Before** an attack occurs.
    -   **Purpose:** To stop an attack from happening at all.
    -   :yellow[**Examples:**] Locks, firewalls, MFA, employee security training.

2.  ### 🚨 :green[Detective Control]
    -   **Timing:** **During** or **after** an attack has occurred.
    -   **Purpose:** To detect that an attack is taking place or has happened, giving a warning.
    -   :yellow[**Examples:**] CCTV, alerting systems, system logs, SIEM.

3.  ### 🩹 :green[Corrective Control]
    -   **Timing:** **After** an attack has been detected.
    -   **Purpose:** To stop the damage and repair the immediate problem.
    -   :yellow[**Examples:**] Removing malware, isolating an infected device, closing a compromised account.

4.  ### 🔄 :green[Recovery Control]
    -   **Timing:** **After** an attack has been stopped.
    -   **Purpose:** To restore systems and data to their normal state, ensuring **Availability**.
    -   :yellow[**Example:**] Restoring data from a backup after a ransomware attack.
    -   **:orange[Distinction:]** Corrective ends the harm; Recovery restores what was lost.

5.  ### 🛠️ :green[Compensating Control]
    -   **Timing:** Used **when the ideal control cannot be applied**.
    -   **Purpose:** An alternative measure or substitute that makes up for the absence of a primary control.
    -   :yellow[**Example:**] Placing an additional security guard if an alarm system is broken until it can be repaired.

---

## :blue[📡 Monitoring and Detection]

Effective defense relies on continuous monitoring and the systematic detection of threats, differentiating real dangers from false alarms.

### :green[Detection Process]

Detection works through a logical sequence of four steps, from recording events to identifying genuine threats.

### :violet[Four Steps of Detection]

1.  ### ✍️ :green[Logging]
    -   **What it Does:** Records every event that occurs within a system into a **log** file (who entered, when, what was opened, what was done).
    -   **:orange[Key Idea:]** The foundation of detection; nothing can be detected without a record. Connects to **Accountability**.

2.  ### 🔔 :green[Alerting]
    -   **What it Does:** Automatic notification sent by a system when it finds something suspicious in the logs (e.g., 50 incorrect login attempts in one minute).
    -   :yellow[**Analogy:**] A fire alarm that sounds automatically when danger is sensed.

3.  ### 👁️‍🗨️ :green[Security Monitoring]
    -   **What it Does:** The continuous, around-the-clock observation of systems and alerts by a team or system.
    -   :yellow[**Analogy:**] A guard in a control room watching all cameras for unusual movement.

4.  ### 🔍 :green[Threat Detection]
    -   **What it Does:** The analysis of alerts and data to distinguish a genuine threat from a false alarm.
    -   **:orange[Key Skill:]** Judgment is crucial to avoid wasting effort on false alarms while not missing real attacks.
    -   :yellow[**Analogy:**] A doctor examining test results to distinguish normal from urgent.

---

## :blue[🖥️ Security Operations Center (SOC)]

The Security Operations Center (SOC) is the central team and facility where cybersecurity defenses are put into continuous practice.

### :green[SOC Purpose]

A **Security Operations Center (SOC)** is a central team dedicated to **monitoring, detecting, and responding** to cyber threats around the clock.

-   :yellow[**Analogy:**] A central control room or fire station.
-   **:orange[Key Tool:]** The **SIEM** (Security Information and Event Management) system is often central to the SOC, gathering and correlating events from across the organization.

### :violet[SOC Workflow]

The SOC operates through an ordered sequence of steps:

1.  **Monitoring:** Continuously watching screens and logs for activity.
2.  **Detection:** Noticing an alert about suspicious activity.
3.  **Investigation:** Examining the alert to determine if it's a real threat or a false alarm.
4.  **Response:** If a real threat is confirmed, acting to stop the attack and limit damage.
5.  **Recovery:** After the attack is stopped, restoring systems to normal and learning lessons to prevent future incidents.

### :green[Security Analyst Responsibilities]

The **security analyst** is the person working within the SOC, forming the first line of defense.

-   Continuously watches screens and alerts.
-   Sorts alerts to prioritize important ones.
-   Investigates alerts to understand what is happening.
-   Escalates large attacks to specialized teams (e.g., incident response).
-   Documents incidents and helps improve detection rules.
