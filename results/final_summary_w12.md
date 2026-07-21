## :blue[💎 Week 12: Threat Landscape and Attack Vectors]

Understanding what assets an organization possesses is the crucial first step in building effective cybersecurity defenses.

### :green[Asset Definition]

An **asset** is anything of value to an organization that requires protection from cyberattacks and security threats.

### :green[Five Main Types of Assets]

1.  ### 📚 :green[Data]
    -   **:green[Definition:]** Information in various forms (text, numbers, images, videos) and is often the primary target for attackers.
    -   **Types:** Personal data (SSN, medical records), Business data (customer lists, trade secrets), Government data (classified info).
    -   **:red[How Data Gets Attacked:]** Theft, corruption, deletion, exposure.

2.  ### 🖥️ :green[Systems]
    -   **:green[Definition:]** The computers, servers, and devices that process and store data.
    -   **Types:** Personal computers, web/database servers, mobile devices, specialized systems (ATMs, IoT devices).
    -   **:red[How Systems Get Attacked:]** Malware infection, exploitation of vulnerabilities, Denial of Service (DoS), physical damage.

3.  ### ⚙️ :green[Applications]
    -   **:green[Definition:]** Software programs that run on systems and perform specific functions.
    -   **Types:** Productivity apps (Word), Business apps (CRM, ERP), Web apps (social media, banking), Security apps (firewalls, antivirus), Custom apps.
    -   **:red[How Applications Get Attacked:]** Code vulnerabilities, SQL Injection, Cross-Site Scripting (XSS), weak authentication.

4.  ### 🔌 :green[Infrastructure]
    -   **:green[Definition:]** The foundational physical and network components that everything else depends on.
    -   **Types:** Network infrastructure (routers, switches, firewalls), Physical infrastructure (data centers, server rooms, power supplies), Cloud infrastructure.
    -   **:red[How Infrastructure Gets Attacked:]** DDoS attacks, network interception, physical attacks (cutting cables), configuration issues.

5.  ### 🧍 :green[Human Assets]
    -   **:green[Definition:]** People are assets because they use and operate systems, make decisions, and can be manipulated.
    -   **Types:** Employees, their knowledge/skills, customers (users).
    -   **:red[How Human Assets Get Compromised:]** Social engineering, phishing, malware (via infected employee devices), blackmail.

### :orange[Asset Inventory and Valuation]

Organizations must list all their assets (**inventory**) and assess their **value** (cost to replace, impact if compromised, regulatory importance) to prioritize protection efforts (e.g., critical, high, medium, low value assets).

---

## :blue[⚠️ Threats, Vulnerabilities, Risks, and Attacks]

These four fundamental cybersecurity concepts are distinct yet interconnected, explaining how harm can occur and how it can be prevented.

-   :orange[**Analogy:**] Think of home security:
    -   **Threat:** A burglar.
    -   **Vulnerability:** An unlocked window.
    -   **Risk:** The possibility the burglar will rob you via the window.
    -   **Attack:** The burglar breaking in through the window.

### :red[Threat]

**:green[Definition:]** Anything that could potentially harm your systems, data, or organization. It's the danger itself, often with malicious intent.

-   **:orange[Key Idea:]** A threat exists whether or not you have defenses.
-   **Examples:** Cybercriminals, nation-state actors, natural disasters (earthquakes), careless employees (accidents), malicious competitors.
-   **Types:** Internal (disgruntled employees, accidental mistakes), External (hackers, foreign governments).

### :red[Vulnerability]

**:green[Definition:]** A weakness or flaw in your systems, applications, or processes that can be exploited by a threat.

-   **:orange[Key Idea:]** A vulnerability exists whether or not anyone exploits it.
-   **Examples:** Unpatched software, weak passwords, misconfigured firewalls, untrained employees, unlocked physical doors, lack of security procedures.
-   :yellow[**Example:**] Unpatched software with a known security flaw is a vulnerability. Applying the patch removes it.

### :red[Risk]

**:green[Definition:]** The probability and impact of a threat exploiting a vulnerability. It combines the likelihood of something bad happening with the damage it would cause.

-   **:orange[Key Idea:]** Risk depends on the presence of a threat, a vulnerability, and the potential impact.
-   **Risk Formula:** `Risk = Threat x Vulnerability x Impact`
-   **Risk Assessment:** Organizations prioritize risks (high, medium, low) to decide where to focus protection.

### :red[Attack]

**:green[Definition:]** When a threat takes active, deliberate action to exploit a vulnerability and attempt to cause harm.

-   **:orange[Key Idea:]** An attack is an active event, an intentional attempt to cause harm.
-   **Examples:** A malware infection, a phishing attempt, a DDoS attack, a data breach.

### :violet[The Relationship & Prevention]

-   A **Threat** (e.g., hacker) looks for a **Vulnerability** (e.g., unpatched software).
-   If a vulnerability exists, there is a **Risk** (e.g., data breach).
-   An **Attack** is the actual exploitation of the vulnerability by the threat.
-   **:orange[Prevention:]** The most effective way to reduce risk is to **eliminate or reduce vulnerabilities** (e.g., apply patches, use strong passwords) rather than trying to eliminate all threats (which is often impossible).

---

## :blue[🎭 Threat Actors]

Behind every cyber threat is a person or group called a threat actor, whose motivations and capabilities dictate defense strategies.

### :green[Threat Actor Definition]

A **threat actor** is the person or group responsible for creating or carrying out a cyber threat. Identifying them helps in defense planning.

### :violet[Types of Threat Actors]

1.  ### 💰 :green[Cybercriminals]
    -   **Motivation:** Primarily **financial gain** (stealing money, selling data, ransomware).
    -   **Note:** Most widespread threat actor due to direct profit motive.

2.  ### 🏛️ :green[Nation-State Actors]
    -   **Motivation:** **Political or military aims** (espionage, sabotage of critical infrastructure, intelligence gathering).
    -   **Note:** Most dangerous and capable, backed by significant resources. Cybersecurity is part of national security because of them.

3.  ### 📢 :green[Hacktivists]
    -   **Motivation:** To support a **cause or deliver a message** (e.g., website defacement, leaking information as protest).
    -   **Note:** Not motivated by money, but their actions are illegal.

4.  ### 👤 :green[Insider Threats]
    -   **Motivation:** Varies; can be **deliberate** (disgruntled employee) or **accidental** (careless employee).
    -   **Note:** Especially dangerous as they already have legitimate access and permissions. Employee awareness training is key protection.

5.  ### 👶 :green[Script Kiddies]
    -   **Motivation:** Usually **curiosity or showing off** their capabilities.
    -   **Note:** Inexperienced attackers who use ready-made tools created by others, often without full understanding. Least dangerous in skill, but numerous.

---

## :blue[🔄 Attack Lifecycle]

An attack unfolds through a series of predictable stages, which defenders study to intercept and stop attacks as early as possible.

### :green[Purpose of Studying the Lifecycle]

Understanding the **attack lifecycle** allows defenders to stop an attack at any stage before completion, reducing potential damage.

### :violet[The Six Stages of an Attack Lifecycle]

1.  ### 🕵️ :green[Reconnaissance]
    -   **:green[Definition:]** The attacker gathers information about the target to find weaknesses.
    -   :yellow[**Burglar Example:**] Watching a building, learning guard schedules, identifying doors.
    -   **:orange[Connection:]** Relates to a target's digital footprint (publicly available information).

2.  ### 🚪 :green[Initial Access]
    -   **:green[Definition:]** The attacker gains the first entry into the system.
    -   :yellow[**Burglar Example:**] Finding and entering through an open door or window.
    -   **:orange[Common Methods:]** Deceiving an employee (phishing), exploiting a weak password. Early detection here is crucial.

3.  ### 🏃 :green[Execution]
    -   **:green[Definition:]** The attacker begins to run malicious programs (malware) or carry out actions within the system.
    -   :yellow[**Burglar Example:**] Searching the building for valuables.

4.  ### 🗝️ :green[Persistence]
    -   **:green[Definition:]** The attacker creates a way to return to the system, even if the initial entry point is closed.
    -   :yellow[**Burglar Example:**] Making a copy of a key for future access.
    -   **:orange[Digital Domain:]** Leaving a hidden back door.

5.  ### 🚶 :green[Lateral Movement]
    -   **:green[Definition:]** The attacker moves from the initially compromised device to other devices and systems within the same network.
    -   :yellow[**Burglar Example:**] Moving from room to room searching for the most valuable items.
    -   **:orange[Importance:]** Monitoring network activity helps detect this unusual spread.

6.  ### 📤 :green[Exfiltration]
    -   **:green[Definition:]** The attacker transfers the stolen data out of the target's network to their own control.
    -   :yellow[**Burglar Example:**] Carrying stolen valuables out of the building.
    -   **:orange[Impact:]** This is where the real harm (data theft, extortion) is realized.

---

## :blue[🎣 Social Engineering Attacks]

Social engineering manipulates people, rather than machines, by exploiting human emotions and trust to gain access or information.

### :green[Social Engineering Definition]

**:green[Definition:]** A method of attack that manipulates a person's emotions and trust, persuading the victim to hand over information or grant access willingly.

-   **:orange[Key Idea:]** Targets people, not technology, making it crucial for users to recognize and defend against.

### :violet[Five Forms of Social Engineering]

1.  ### 📧 :green[Phishing]
    -   **Method:** Fraudulent message (usually email) from a trusted source (e.g., bank, well-known company).
    -   **Purpose:** Deceive recipient into clicking a harmful link or entering credentials on a fake website.
    -   **Warning Signs:** Urgency/fear, spelling mistakes, unfamiliar sender, incorrect links.
    -   **:orange[Protection:]** Never click links in unverified messages; only enter passwords on official websites you open personally.

2.  ### 🎯 :green[Spear Phishing]
    -   **Method:** Phishing specifically aimed at one person, using tailored information about the target.
    -   **Key Feature:** Appears highly convincing due to personalization (e.g., addresses victim by name, refers to their school or interests).

3.  ### 📞 :green[Vishing (Voice Phishing)]
    -   **Method:** Deception carried out through a telephone call.
    -   **Key Feature:** Attacker claims to be from a trusted organization (e.g., bank, tech support) and asks for sensitive info (e.g., card number, password).
    -   **:orange[Protection:]** A genuine organization will *never* ask for your password or secret code over the phone. End the call and contact the official organization directly.

4.  ### 💬 :green[Smishing (SMS Phishing)]
    -   **Method:** Deception through a text message (SMS) containing a harmful link or request for information.
    -   **Key Feature:** Often promises prizes or warns of urgent problems.
    -   **:orange[Protection:]** Similar to phishing: don't click suspicious links in texts, especially if they create urgency or offer something too good to be true.

5.  ### 🎭 :green[Pretexting]
    -   **Method:** The attacker invents a false story or identity to build trust and extract information.
    -   **Key Feature:** Constructs a complete, convincing scenario (e.g., fake IT support calling to "help" with an account problem by asking for a password).
    -   **:orange[Protection:]** Always verify a person's identity through official sources before providing any information, regardless of how convincing their story seems.

---

## :blue[🦠 Malware Attacks]

Malware, or malicious software, refers to harmful programs designed to damage devices or steal data, taking various forms to achieve different objectives.

### :green[Malware Definition]

**:green[Definition:]** Any harmful program (**mal**icious soft**ware**) created to damage a device, disrupt operations, or steal data.

### :violet[Five Forms of Malware]

1.  ### 👾 :green[Virus]
    -   **Behavior:** Attaches itself to a legitimate file or program and spreads when that file is run or passed to others.
    -   **Key Feature:** Requires a user action (e.g., opening an infected file) to spread.

2.  ### 🐛 :green[Worm]
    -   **Behavior:** Spreads by itself across a network without needing a file attachment or user action.
    -   **Key Feature:** Copies itself rapidly from one device to another, making it fast and dangerous.

3.  ### 🐎 :green[Trojan (Trojan Horse)]
    -   **Behavior:** Disguises itself as a legitimate and useful program, tricking users into installing it.
    -   **Key Feature:** Appears safe on the outside but conceals harmful functions (e.g., opens a backdoor for attackers).
    -   **:orange[Protection:]** Download programs and games only from official, trusted sources.

4.  ### 👁️ :green[Spyware]
    -   **Behavior:** Secretly observes user activity and collects information without their knowledge (e.g., records keystrokes, captures screen images, tracks websites).
    -   **Key Feature:** Operates silently in the background; a device may appear normal while being monitored.
    -   **Signs:** Device suddenly slows down, unusual internet activity.
    -   **:orange[Protection:]** Use antivirus software, avoid suspicious programs.

5.  ### 🔒 :green[Ransomware]
    -   **Behavior:** Locks a user's files or entire device by encrypting data and demands a payment (ransom) to unlock them.
    -   **Key Feature:** Openly demands payment and halts operations. One of the most dangerous forms.
    -   **:orange[Protection:]** The most important defense is to **keep regular backup copies of your files** in a separate location.

### :orange[Common Malware Protections]

-   Antivirus software
-   Keeping software updated
-   Downloading only from trusted sources
-   Regular data backups

---

## :blue[🌐 Network-Based Attacks]

These attacks target the connections and infrastructure of networks, threatening the CIA Triad principles.

### :green[Definition]

**Network-based attacks** target the connections and underlying infrastructure of a network, exploiting vulnerabilities in how devices communicate over the internet.

### :violet[Four Forms of Network-Based Attacks]

1.  ### 💥 :red[Denial-of-Service (DoS) / Distributed Denial-of-Service (DDoS) Attack]
    -   **What it Does:** Floods a website or server with an enormous volume of false requests, overwhelming it until it goes offline.
    -   **CIA Principle Threatened:** **Availability** (prevents legitimate users from accessing the service).

2.  ### 🤝 :red[Man-in-the-Middle (MitM) Attack]
    -   **What it Does:** The attacker secretly intercepts and relays communication between two parties, reading and potentially altering information without their knowledge.
    -   **CIA Principles Threatened:** **Confidentiality** (attacker reads messages) and **Integrity** (attacker can change messages).
    -   **:orange[Protection:]** Use websites with **HTTPS** (the 'S' indicates encryption), avoid sensitive activities on public Wi-Fi.

3.  ### 🗺️ :red[DNS Attack (Domain Name System Attack)]
    -   **What it Does:** The attacker tampers with the internet's "telephone directory" (DNS), redirecting users typing a genuine website address to a counterfeit site.
    -   **CIA Principles Threatened:** **Confidentiality** (user enters info on fake site) and **Integrity** (directory altered).
    -   **:orange[Protection:]** Always verify the website address (URL) and look for the HTTPS indicator before entering sensitive information.

4.  ### 📡 :red[Packet Sniffing]
    -   **What it Does:** An attacker captures and reads small pieces of data (**packets**) as they travel across a network.
    -   **CIA Principle Threatened:** **Confidentiality** (if data is unencrypted, attacker can read messages and passwords).
    -   **:orange[Protection:]** **Encryption** (makes captured data unreadable); avoid public Wi-Fi for sensitive tasks.

---

## :blue[🛡️ Defending Organizations Against Cyber Attacks]

Security controls are the primary defense mechanisms organizations use to protect assets and manage risks.

### :green[Security Control Definition]

A **security control** is any measure or means implemented to protect assets and reduce risk. It makes an attacker's task more difficult.

-   **:orange[Purpose:]** To maintain Confidentiality, Integrity, and Availability (CIA) by preventing unauthorized access, detecting harmful activity, and supporting recovery.
-   :yellow[**Examples:**] A password on a phone, a lock on a door, not opening unfamiliar links.

### :green[Risk Reduction]

-   **:orange[Key Idea:]** Controls close vulnerabilities, thereby reducing risk.
-   :red[**Important:**] The goal is **risk reduction**, not elimination; perfect safety is impossible.

### :green[Security Management & Defence in Depth]

-   **Security Management:** The organized process of choosing, applying, monitoring, and updating controls based on asset importance and risk.
-   **Defence in Depth:** A central principle meaning **layered protection**. Multiple security layers are placed one behind another so that if one fails, the next layer can stop the attacker.
    -   :yellow[**Analogy:**] An old castle with a moat, high walls, guards, and gates.
